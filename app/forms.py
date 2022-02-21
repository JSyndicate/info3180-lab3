
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import EmailField
from wtforms import SubmitField
from wtforms.validators import DataRequired



class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators =[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')
