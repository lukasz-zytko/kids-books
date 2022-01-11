from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.fields.numeric import IntegerRangeField
from wtforms.validators import DataRequired, Email

class BooksForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    series = StringField('Seria')
    pages = IntegerField('Liczba stron', default=0)
    age = SelectField('Kategoria wiekowa', choices=['', '0-4', '5-10', 'all'])
    pictures = BooleanField('Ilustracje')
    cover = SelectField('Okładka', choices=['','miękka', 'twarda'])
    readings = IntegerField('Liczba przeczytań', default=0)
    last_read = StringField('Ostatnio czytane')
