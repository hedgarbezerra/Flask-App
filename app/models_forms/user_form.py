from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, DateField, DateTimeField, SelectField, FileField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, NumberRange, Length, EqualTo, ValidationError
import datetime
from ..views import user_view


class userForm(FlaskForm):

    def validate_age(form, field):
        today = datetime.datetime.today().year
        age = today - field.data.year
        if age < 18:
            raise ValidationError("We're sorry, you must be 18 or older to register.")

    def validate_username(form, field):
        if user_view.username_exists(field.data):
            raise ValidationError("We're sorry, this username is in use.")
        else:
            pass

    def validate_email(form, field):
        if user_view.email_exists(field.data):
            raise ValidationError("We're sorry, this email is already registered. ")


    name = StringField('name', validators=[DataRequired(message="Your name can't be empty"), Length(min=1, max=100)])

    username = StringField('username', validators=[DataRequired(message="Your username can't be empty"),
                                                   Length(min=6, max=15, message='The username must have at '
                                                                                 'least 6'
                                                                                   ' characteres and max 15'),
                                                   validate_username])

    password = PasswordField('password', validators=[DataRequired(message="The password can't be empty"),
                                                     Length(min=8, max=30, message='The password must have at least 8'
                                                                                   ' characteres and max 30'),
                                                     EqualTo('confirm', message='The passwords must match')])

    confirm = PasswordField('Repeat the password', validators=[DataRequired(
                                                    message="The confirmation password can't be empty")])

    email = EmailField('email', validators=[DataRequired(message="The email can't be empty"),
                                            Email(message='Please, insert a valid email.'),
                                            validate_email])

    gender = SelectField('gender', choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neither')])

    born_on = DateField('born_on', validators=[DataRequired(message="The birthday can't be empty"),
                                               validate_age], format='%Y-%m-%d')

