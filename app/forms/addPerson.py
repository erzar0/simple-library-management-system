from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

class AddPersonForm(FlaskForm):
    first_name = StringField("first name")
    last_name = StringField("last name")
    pesel = StringField("pesel")
    birth_date = StringField("date of birth")
    email = StringField("email")
    submit = SubmitField("add")