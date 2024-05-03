from app.config import ROMS_FOLDER
from app.models.game_model import Game, HighScore
from app.models.emulators_model import Emulators
from app.views import game_view
from app import db
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
import os


def get_all_games():
    games = Game.query.order_by(Game.name.asc()).all()
    return game_view.game_list(games)


def get_game_detail(game_id):
    game = Game.query.get(game_id)
    high_scores = HighScore.query.filter_by(game_id=game_id).all()
    return game_view.game_detail(game, high_scores)


def add_game():
    if request.method == 'POST':
        title = request.form.get('title')
        release_year = request.form.get('release_year')
        genre = request.form.get('genre')
        difficulty = request.form.get('difficulty')
        platform = request.form.get('platform')
        emulator_id = request.form.get('emulator')
        image = request.files['image']

        rom_folder = Emulators.query.get(emulator_id).image_folder
        filename = secure_filename(image.filename)
        fullname = os.path.join(ROMS_FOLDER, rom_folder, filename)

        image.save(fullname)

        game = Game(
            name=title,
            release_year=release_year,
            genre=genre,
            difficulty=difficulty,
            platform=platform,
            image=filename,
            emulator_id=emulator_id
        )
        db.session.add(game)
        db.session.commit()

        return redirect(url_for('game.game_list'))

    emulators = Emulators.query.all()

    return game_view.add_game(emulators)
