from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators, ValidationError

class AddPersonForm(FlaskForm):
    first_name = StringField("first name", [validators.input_required()])
    last_name = StringField("last name", [validators.input_required()])
    email = StringField("email", [validators.input_required(), validators.email()])
    birth_date = DateField("date of birth", [validators.input_required()])
    pesel = IntegerField("pesel", [validators.input_required(), validators.number_range(min = 10000000000, max=999999999999)])
    submit = SubmitField("add")