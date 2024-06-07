from app import db


class NoteCategory(db.Model):
    __tablename__ = "note_category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    notes = db.relationship('Note', back_populates='category')
