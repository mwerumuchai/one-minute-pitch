from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class PeptalkForm(FlaskForm):
    content = TextAreaField('New Pitch')
    submit = SubmitField('Submit')
