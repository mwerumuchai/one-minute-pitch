from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class PeptalkForm(FlaskForm):
    pitch = TextAreaField('New Pitch')
    submit = SubmitField('Submit')
