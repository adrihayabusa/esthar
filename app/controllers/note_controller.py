from flask import current_app, request, redirect, url_for, Markup
from app.models.note_model import Note
from app.views import note_view
from app import db
from datetime import datetime
from itertools import groupby
import os


def get_notes_list():
    # notes = Note.query.order_by(Note.date_created.desc()).paginate(page=page, per_page=5)
    notes = Note.query.order_by(Note.date_created).all()
    grouped_notes = {}
    for key, group in groupby(notes, key=lambda x: (x.date_created.year, x.date_created.month)):
        year, month = key
        if year not in grouped_notes:
            grouped_notes[year] = {}
        grouped_notes[year][month] = list(group)
    return note_view.notes_list(grouped_notes)


def get_note_detail(note_id):
    notes_dir = os.path.join(current_app.root_path, 'files', 'notes')
    os.makedirs(notes_dir, exist_ok=True)

    note = Note.query.get(note_id)
    with open(note.text_file, 'r', encoding='utf-8') as file:
        html_text = file.read()

    return note_view.view_note(note, text=Markup(html_text))


def add_note():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')

        notes_dir = os.path.join(current_app.root_path, 'files', 'notes')
        os.makedirs(notes_dir, exist_ok=True)

        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')
        file_name = f"note_{formatted_datetime}.txt"
        file_path = os.path.join(notes_dir, file_name)

        note = Note(title=title, text_file=file_path, date_created=current_datetime)
        db.session.add(note)
        db.session.commit()

        with open(note.text_file, 'w', encoding='utf-8') as file:
            file.write(text)

        return redirect(url_for('note.note_detail', note_id=note.id))
    return note_view.add_note()


def update_note(note_id):
    note = Note.query.get(note_id)
    if request.method == 'PATCH':
        text = request.form.get('text')
        notes_dir = os.path.join(current_app.root_path, 'files', 'notes')
        os.makedirs(notes_dir, exist_ok=True)

        note.date_updated = datetime.now()
        db.session.add(note)
        db.session.commit()

        with open(note.text_file, 'w', encoding='utf-8') as file:
            file.write(text)

        return 'Ok!'
    with open(note.text_file, 'r', encoding='utf-8') as file:
        html_text = file.read()

    return note_view.update_note(note, html_text)
