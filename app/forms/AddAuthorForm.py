from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms import validators

class AddAuthorForm(FlaskForm):
    first_name      = StringField("Imię/Pseudonim*",     [validators.input_required()]) 
    last_name       = StringField("Nazwisko",           [validators.optional()]) 
    nationality     = StringField("Narodowość*",         [validators.input_required()])
    submit          = SubmitField("Dodaj")