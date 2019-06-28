from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class Profile_imgForm(FlaskForm):
    photo = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
