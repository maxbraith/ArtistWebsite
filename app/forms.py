from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    artistName = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Hometown')
    description = TextAreaField('Description')
    submitArtist = SubmitField('Submit New Artist')