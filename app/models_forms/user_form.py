from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, DateField, DateTimeField, SelectField, FileField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, NumberRange, Length, EqualTo


class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="Your name can't be empty"), Length(min=1, max=100)])

    username = StringField('username', validators=[DataRequired(message="Your username can't be empty"),
                                                   Length(min=6, max=15, message='The password must have at least 6'
                                                                                   ' characteres and max 15')])

    password = PasswordField('password', validators=[DataRequired(message="The password can't be empty"),
                                                     Length(min=8, max=30, message='The password must have at least 8'
                                                                                   ' characteres and max 30'),
                                                     EqualTo('confirm', message='The passwords must match')])
    confirm = PasswordField('Repeat the password', validators=[DataRequired(message="The confirmation can't be empty"),
                                                     EqualTo('password', message='The passwords must match')])

    email = EmailField('email', validators=[DataRequired(message="The email can't be empty"),
                                            Email(message='Please, insert a valid email. ')])

    gender = SelectField('gender', choices=[(u'M', u'Male'), (u'F', u'Female'), (u'N', u'Neither')])

    born_on = DateField('born_on', validators=[DataRequired(message="The birthday can't be empty")], format='%Y-%m-%d')
