from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange


class AddAnimeForm(FlaskForm):
    name = StringField('Nom de l\'anime', validators=[DataRequired(), Length(max=100)])
    genre = StringField('Genre', validators=[DataRequired(), Length(max=50)])
    release_year = IntegerField('Année de sortie', validators=[DataRequired(), NumberRange(min=1900)])
    violence_level = IntegerField('Niveau de violence (0 à 20)', validators=[NumberRange(min=0, max=20)])
    age_restriction = StringField('Limite d\'âge')
    explicit_content = StringField('Contenu explicite')
