from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import Artist
class artistForm(FlaskForm):
    artistName = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Hometown')
    description = TextAreaField('Description')
    submitArtist = SubmitField('Submit New Artist')

    def validate_artistName(self, name):
        name1 = Artist.query.filter_by(name=name.data).first()
        if name1 is not None:
            raise ValidationError("Artist already submitted.")
