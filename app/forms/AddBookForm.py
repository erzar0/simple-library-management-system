from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectMultipleField
from wtforms import validators, widgets
import sys
sys.path.append(".")

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


from ..models.BookModel import BookModel

Book = BookModel()
authors = [(author["id"], author["first_name"]) for author in Book.getAllAuthors()]
print(authors)

class AddBookForm(FlaskForm):
    title               = StringField("Tytuł",                  [validators.input_required()])
    language            = StringField("Język",                  [validators.input_required()])      
    publication_date    = DateField("Data publikacji",          [validators.input_required()])
    physical_location   = StringField("Lokalizacja fizyczna",   [validators.input_required()])
    price               = IntegerField("Cena katalogowa",       [validators.input_required()])
    isbn                = StringField("ISBN",                   [validators.optional()
                                                                ,validators.length(13, 13)])
    authors             = MultiCheckboxField("Autorzy",        [validators.input_required()]
                                                                ,choices=authors) 
    genres              = SelectMultipleField("Gatunkki",       [validators.input_required()]) 
    
    submit          = SubmitField("Dodaj")