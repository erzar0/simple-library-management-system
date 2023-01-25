from flask_wtf import FlaskForm 
from wtforms import SubmitField, IntegerField
from wtforms import validators



class PayFeeForm(FlaskForm):
    id                  = IntegerField("Id opłaty*",            [validators.input_required()])
    id_member           = IntegerField("Id członka*",       [validators.input_required()])
    submit              = SubmitField("Opłać")