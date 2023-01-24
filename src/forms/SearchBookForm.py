from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, BooleanField
from wtforms import validators



class SearchBookForm(FlaskForm):
    title               = StringField("Tytuł",                      [validators.optional()])
    author_first_name   = StringField("Imię/pseudonim autora",      [validators.optional()])
    author_last_name    = StringField("Nazwisko autora",            [validators.optional()])
    genre               = StringField("Gatunek",                    [validators.optional()])
    submit              = SubmitField("Szukaj")