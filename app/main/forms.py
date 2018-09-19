from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('About me')
    submit = SubmitField('Submit')