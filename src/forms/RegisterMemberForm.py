from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators

class RegisterMemberForm(FlaskForm):
    first_name      = StringField("Imię*",               [validators.input_required()])
    last_name       = StringField("Nazwisko*",           [validators.input_required()])
    email           = StringField("Email*",              [validators.input_required()
                                                        , validators.email()])
    birth_date      = DateField("Data urodzenia*",       [validators.input_required()])
    pesel           = IntegerField("Pesel*",             [validators.input_required()
                                                        ,validators.NumberRange(min = 10000000000,max=99999999999)]) 
    city            = StringField("Miasto*",             [validators.input_required()])
    street          = StringField("Ulica*",              [validators.input_required()])
    postal_code     = StringField("Kod pocztowy*",       [validators.input_required()])
    house_number    = IntegerField("Numer domu*",        [validators.input_required()])
    apartment_number= IntegerField("Numer lokalu",      [validators.optional()])
    submit          = SubmitField("Zarejestruj")