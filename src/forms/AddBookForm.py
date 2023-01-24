from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectMultipleField
from wtforms import validators



class AddBookForm(FlaskForm):
    title               = StringField("Tytuł*",                  [validators.input_required()])
    language            = StringField("Język*",                  [validators.input_required()])      
    publication_date    = DateField("Data publikacji*",          [validators.input_required()])
    physical_location   = StringField("Lokalizacja fizyczna*",   [validators.input_required()])
    price               = IntegerField("Cena katalogowa*",       [validators.input_required()])
    isbn                = StringField("ISBN",                    [validators.optional()
                                                                 ,validators.length(13, 13)])
    authors             = SelectMultipleField("Autorzy* (przytrzymaj ctrl by zaznaczyć wiele)",        [validators.input_required()]
                                                                 ,validate_choice=False) 
    genres              = SelectMultipleField("Gatunki* (przytrzymaj ctrl by zaznaczyć wiele)",        [validators.input_required()]
                                                                 ,validate_choice=False) 
    submit          = SubmitField("Dodaj")