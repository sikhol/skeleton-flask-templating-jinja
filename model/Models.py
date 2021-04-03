from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config.settings import db
from flask_login import login_user,UserMixin
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    user_type = db.Column(db.Integer,  nullable=True)
    upgrade_status = db.Column(db.Integer, default=0)
    username = db.Column(db.String(150), unique=True)
    domisili = db.Column(db.String(225), nullable=True)
    industry = db.Column(db.String(225), nullable=True)
    type_akun = db.Column(db.String(225), nullable=True)
    phone = db.Column(db.String(225), unique=True, nullable=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()  
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()  
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': f'{num_rows_deleted} row(s) deleted'}
        except:
            return {'message': 'Something went wrong'}
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    @staticmethod
    def verify_hash(password, hash_):
        return sha256.verify(password, hash_)


