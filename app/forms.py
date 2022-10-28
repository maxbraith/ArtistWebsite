from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, SelectField, SelectMultipleField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.models import Artist, User

class artistForm(FlaskForm):
    artistName = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Hometown')
    description = TextAreaField('Description')
    submitArtist = SubmitField('Submit New Artist')

    def validate_artistName(self, name):
        name1 = Artist.query.filter_by(name=name.data).first()
        if name1 is not None:
            raise ValidationError("Artist already submitted.")


class eventForm(FlaskForm):
    eventName = StringField("Event Name", validators=[DataRequired()])
    date = DateField("Event Date", format='%Y-%m-%d')
    venue = SelectField("Venue", coerce=int)
    a2e = SelectMultipleField("Artist", coerce=int)
    submitEvent = SubmitField("Submit New Event")

class venueForm(FlaskForm):
    venueName = StringField("Venue Name", validators=[DataRequired()])
    address = StringField("Venue Address", validators=[DataRequired()])
    submitVenue = SubmitField("Submit New Venue")


class loginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')

