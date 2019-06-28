from app import db
from sqlalchemy.orm import relationship


class UserImg(db.Model):
    __tablename__ = 'user_img'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    path = db.Column(db.String(100))
    user = relationship('User')
