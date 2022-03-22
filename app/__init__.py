import subprocess
import threading

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, request, jsonify, abort, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from webargs.flaskparser import parser


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)


    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='DEMO-TASK',
            version='v1',
            openapi_version="2.0.2",
            plugins=[MarshmallowPlugin()],
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })

    """ config db """
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db = SQLAlchemy(app)

    """Configure base routes."""

    @app.route('/', methods=['GET'])
    def home():
        args = request.args
        out = {
            'home': "Base Flask App: OpenAPI Specification Enter here"
        }
        """ run csv task """
        csv_task()
        if args:
            out = {**out, **args}
        return out, 200, {'Content-Type': 'text/plain'}

    @parser.error_handler
    def handle_request_parsing_error(error, req, schema, status_code, headers):
        abort(status_code, str(error.messages))

    @app.errorhandler(400)
    def bad_request(error):
        error = vars(error)

        message = "The browser (or proxy) sent a request that this server could not understand."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 400, 'message': message}

        response = make_response(jsonify(out), 400)
        return response

    @app.errorhandler(401)
    def unauthorized(error):
        error = vars(error)

        message = "The server could not verify that you are authorized to" \
                  " access the URL requested. You either supplied the wrong" \
                  " credentials (e.g. a bad password), or your browser " \
                  "doesn't understand how to supply the credentials required."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 401, 'message': message}

        response = make_response(jsonify(out), 401)
        return response

    @app.errorhandler(403)
    def forbidden(error):
        error = vars(error)

        message = "You don't have the permission to access the requested " \
                  "resource. It is either read-protected or not readable by " \
                  "the server."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 403, 'message': message}

        response = make_response(jsonify(out), 403)
        return response

    @app.errorhandler(404)
    def not_found(error):
        error = vars(error)

        message = "The requested URL was not found on the server. If you" \
                  " entered the URL manually please check your spelling and" \
                  " try again."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 404, 'message': message}

        response = make_response(jsonify(out), 404)
        return response

    @app.errorhandler(405)
    def method_not_allowed(error):
        error = vars(error)

        message = "The method is not allowed for the requested URL."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 405, 'message': message}

        response = make_response(jsonify(out), 405)
        return response

    @app.errorhandler(500)
    def internal_server(error):
        error = vars(error)

        message = "The server encountered an internal error and was unable" \
                  " to complete your request. Either the server is" \
                  " overloaded or there is an error in the application."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 500, 'message': message}

        response = make_response(jsonify(out), 500)
        return response

    @app.errorhandler(503)
    def service_unavailable(error):
        error = vars(error)

        message = "The server is temporarily unable to service your" \
                  " request due to maintenance downtime or capacity" \
                  " problems. Please try again later."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 503, 'message': message}

        response = make_response(jsonify(out), 503)
        return response

    @app.errorhandler(504)
    def gateway_timeout(error):
        error = vars(error)

        message = "The connection to an upstream server timed out."

        if error.get("description"):
            if error.get("description").get('message'):
                message = error["description"]["message"]

        out = {'code': 504, 'message': message}

        response = make_response(jsonify(out), 504)
        return response



    # """Configure app environment parameters."""
    # settings = os.getenv('SETTING', 'app.config.base.BaseConfig')
    # app.config.from_object(settings)

    """ run csv task """
    # csv_task()

    return app


def csv_task():
    csv_thread = threading.Thread(target=invoke_via_subprocess)
    csv_thread.start()


def invoke_via_subprocess():
    from app.csv_task.helpers.csv_generator import CsvGenerator
    CsvGenerator().main()