from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, Length,ValidationError
import datetime
from ..views import user_view


class update_userForm(FlaskForm):

    def validate_age(form, field):
        today = datetime.datetime.today().year
        age = today - field.data.year
        if age < 18:
            raise ValidationError("We're sorry, you must be 18 or older to register.")

    def validate_email(form, field):
        if user_view.email_exists(field.data):
            raise ValidationError("We're sorry, this email is already registered. ")

    name = StringField('name', validators=[DataRequired(message="Your name can't be empty"),
                                           Length(min=1, max=100)])

    email = EmailField('email', validators=[DataRequired(message="The email can't be empty"),
                                            Email(message='Please, insert a valid email.'),
                                            validate_email])

    gender = SelectField('gender', choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neither')])

    born_on = DateField('born_on', validators=[DataRequired(message="The birthday can't be empty"),
                                               validate_age], format='%Y-%m-%d')
