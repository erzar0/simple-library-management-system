from flask_wtf import FlaskForm 
from wtforms import SubmitField, IntegerField
from wtforms import validators


class ReturnBookForm(FlaskForm):
    id_book     = IntegerField("Id zwracanej kiążki*",       [validators.input_required()])
    id_member   = IntegerField("Id zwracającego członka*",   [validators.input_required()])
    submit      = SubmitField("Zwróć")