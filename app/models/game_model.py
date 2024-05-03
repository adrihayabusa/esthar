from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    platform = db.Column(db.String(200))
    image = db.Column(db.String(200))
    emulator_id = db.Column(db.Integer)
    bios = db.Column(db.String(200))


class HighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    player_name = db.Column(db.String(200), nullable=False)
