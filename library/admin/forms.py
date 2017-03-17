from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class BooksForm(Form):
   name = TextField("Book Title",[validators.Required("Please enter the book title")])
   author = TextField("Author's name",[validators.Required("Please enter the book author's name.")])
   available = RadioField('available ', choices = [('Y','Yes'),('N','No')])
   category = TextField('Category')
   submit = SubmitField("Send")