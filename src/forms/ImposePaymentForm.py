from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators



class ImposePaymentForm(FlaskForm):
    id_member           = IntegerField("Id członka*",     [validators.input_required()])
    id_librarian        = IntegerField("Id pracownika*",  [validators.input_required()])
    to_pay              = IntegerField("Wielkość opłaty*",[validators.input_required()])
    type                = StringField("Rodzaj opłaty*",   [validators.input_required()])
    submit              = SubmitField("Wypożycz")