from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.fields.datetime import DateField
from wtforms.validators import DataRequired, Email

class BooksForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    series = StringField('Seria')
    pages = IntegerField('Liczba stron', validators=[DataRequired()])
    age = SelectField('Kategoria wiekowa', choices=['0-4', '5-10', 'all'])
    pictures = BooleanField('Ilustracje')
    cover = SelectField('Okładka', choices=['miękka', 'twarda'], validators=[DataRequired()])
    readings = IntegerField('Liczba przeczytań')
    last_read = StringField('Ostatnio czytane')
