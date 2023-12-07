from app import db


class Emulators(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(255), nullable=False)
    core = db.Column(db.String(255), nullable=False)
    image_folder = db.Column(db.String(255), nullable=False)
    bios_folder = db.Column(db.String(255))
