from flask import g
from app import create_app
from flask_apispec.extension import FlaskApiSpec

import uuid

app = create_app()


@app.before_request
def before_request(*args, **kwargs):
    print('before request', g.__dict__)
    g.event_hash = str(uuid.uuid4())
    print('after request', g.__dict__)


with app.app_context():
    """Configure RESTful views routing"""
    from flask_restful_swagger_2 import Api

    api = Api(app)

    docs = FlaskApiSpec(app)

    from app.file_task.views.file_views import FileView

    api.add_resource(FileView, '/file')

    docs.register(FileView)