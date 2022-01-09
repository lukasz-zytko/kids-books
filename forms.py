from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email

class BooksForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    pages = IntegerField('Liczba stron', validators=[DataRequired()])
    age = SelectField('Kategoria wiekowa', choices=['0-3', '4-6', '7-10', 'all'], validators=[DataRequired()])