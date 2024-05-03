from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class AddGameForm(FlaskForm):
    name = StringField('Nom du jeu', validators=[DataRequired(), Length(max=200)])
    genre = StringField('Genre', validators=[DataRequired(), Length(max=200)])
    difficulty = StringField('Difficulté', validators=[DataRequired(), NumberRange(min=0, max=7)])
    release_year = IntegerField('Année de sortie', validators=[DataRequired(), NumberRange(min=1900)])
    platform = StringField('Plateforme', validators=[DataRequired(), Length(max=200)])
