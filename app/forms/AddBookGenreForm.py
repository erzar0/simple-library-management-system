from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms import validators

class AddBookGenreForm(FlaskForm):
    name            = StringField("Nazwa gatunku*", [validators.input_required()]) 
    submit          = SubmitField("Dodaj")