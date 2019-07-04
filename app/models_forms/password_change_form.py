from flask_wtf import FlaskForm
from wtforms.fields import PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class passwordForm(FlaskForm):

    password = PasswordField('password', validators=[DataRequired(message="The password can't be empty"),
                                                     Length(min=8, max=30, message='The password must have at least 8'
                                                                                   ' characteres and max 30'),
                                                     EqualTo('confirm', message='The passwords must match')])

    confirm = PasswordField('Repeat the password', validators=[DataRequired(
                                                    message="The confirmation password can't be empty")])
