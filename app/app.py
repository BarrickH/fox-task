from app import create_app
# import threading

app = create_app()

# def csv_task():
#     csv_thread = threading.Thread(target=invoke_via_subprocess)
#     csv_thread.start()
#
#
# def invoke_via_subprocess():
#     from app.csv_task.helpers.csv_generator import CsvGenerator
#     CsvGenerator().main()
#
#
# """ run csv task """
# csv_task()

# with app.app_context():
#     """Configure RESTful views routing"""
#     from flask_restful_swagger_2 import Api
#     from flask_apispec.extension import FlaskApiSpec
#
#     api = Api(app)
#
#     docs = FlaskApiSpec(app)
#
#     from app.file_task.views.file_views import FileView
#
#     api.add_resource(FileView, '/file')
#
#     docs.register(FileView)