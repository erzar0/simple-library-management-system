from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators

class RegisterMemberForm(FlaskForm):
    first_name      = StringField("imie",           [validators.input_required()])
    last_name       = StringField("nazwisko",       [validators.input_required()])
    email           = StringField("email",          [validators.input_required(), validators.email()])
    birth_date      = DateField("data urodzenia",   [validators.input_required()])
    pesel           = IntegerField("pesel",         [validators.input_required(), validators.number_range(min = 10000000000, max=999999999999)])
    city            = StringField("miasto",         [validators.input_required()])
    street          = StringField("ulica",          [validators.input_required()])
    postal_code     = StringField("kod pocztowy",   [validators.input_required()])
    house_number    = StringField("numer domu",    [validators.input_required()])
    apartment_number= StringField("numer lokalu")
    submit          = SubmitField("zarejestruj")