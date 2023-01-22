from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators



class LoanBookForm(FlaskForm):
    id_member           = IntegerField("Id członka",                    [validators.input_required()])
    id_librarian        = IntegerField("Id pracownika",                 [validators.input_required()])
    id_book             = IntegerField("Id kiążki",                     [validators.input_required()])
    submit              = SubmitField("Wypożycz")