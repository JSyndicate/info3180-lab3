from flask_wtf import FlaskForm
from flask_wtf import StringField
from flask_wtf import EmailField
from flask_wtf import SubmitField
from wtforms.validators import DataRequired




class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    subject = StringField('Subject',validators=[DataRequired()])
    text = StringField('Text',validators=[DataRequired()])
    send = SubmitField('Send')

