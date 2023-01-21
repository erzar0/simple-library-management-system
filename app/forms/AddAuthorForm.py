from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectMultipleField
from wtforms import validators

class AddAuthorForm(FlaskForm):
    first_name      = StringField("Imię lub pseudonim", [validators.input_required()]) 
    last_name       = StringField("Nazwisko",           [validators.optional()]) 
    nationality     = StringField("Narodowość",         [validators.input_required()])
    submit          = SubmitField("Dodaj")