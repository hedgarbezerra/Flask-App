import datetime
from sqlalchemy_utils import ChoiceType
from app import db


class User(db.Model):
    __tablename__ = 'user'

    genders = [
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'N', u'Neither')
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), unique=True,  nullable=False)
    gender = db.Column(ChoiceType(genders))
    born_on = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
