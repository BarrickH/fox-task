# from flask import current_app
# from flask_sqlalchemy import SQLAlchemy
# from app.app import app
#
# with app.app_context():
#     """ config db """
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db = SQLAlchemy(current_app)
#
#     @app.before_first_request
#     def first_request():
#         try:
#             db.create_all()
#         except Exception as e:
#             print(str(e))
#
#     @app.after_request
#     def after_request(response):
#         try:
#             db.session.remove()
#             return response
#         except Exception as e:
#             print(str(e))