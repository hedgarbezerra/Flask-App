from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class loginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message="Please, insert your username.")])

    password = PasswordField('password', validators=[DataRequired(message="Please, insert your password.")])

    remember = BooleanField('remember')
