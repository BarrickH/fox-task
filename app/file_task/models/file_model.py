import datetime
# from app.config.base.sqlite import SqliteBase
from app.config.base.sqlite import db

# from flask_sqlalchemy import SQLAlchemy
# from app.app import app

# db = SQLAlchemy(app)

# db = SqliteBase.db


class FileModel(db.Model):
    __tablename__ = 'file.db'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))
    data = db.Column(db.LargeBinary)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())
    current_cursor = db.Column(db.Boolean)

    @staticmethod
    def save(upload):
        db.session.add(upload)
        db.session.commit()
