from datetime import datetime
from app import db


class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text_file = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('note_category.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = db.relationship('NoteCategory', back_populates='notes')
