from app import db


class Anime(db.Model):
    __tablename__ = 'anime'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    release_year = db.Column(db.DateTime, nullable=False)
    violence_level = db.Column(db.String, nullable=False)
    age_restriction = db.Column(db.String, nullable=False)
    explicit_content = db.Column(db.String, nullable=True)
