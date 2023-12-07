from app.views import main_view
from app.config import RESUME_DATA, UPLOAD_FOLDER
from app.models.note_model import Note
from flask import request, jsonify, url_for
from datetime import datetime
import json
import os
from PIL import Image

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'gif', 'png'}
MAX_FILE_SIZE = 5 * 1024 * 1024


def home():
    notes = Note.query.order_by(Note.date_created.desc()).all()

    for note in notes:
        with open(note.text_file, 'r', encoding='utf-8') as file:
            note.body = file.read()

    return main_view.home(notes)


def get_resume():
    formatted_resume = json.dumps(RESUME_DATA, indent=4)
    
    return main_view.resume_view(formatted_resume, RESUME_DATA)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        try:
            img = Image.open(file.stream)

            file.seek(0, os.SEEK_END)
            size = file.tell()
            file.seek(0)

            if size <= MAX_FILE_SIZE:
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')
                filename = f"{formatted_datetime}_{file.filename}"
                fullname = os.path.join(UPLOAD_FOLDER, filename)

                file.save(fullname)

                url = url_for('static',  filename=f'uploads/{filename}')

                return jsonify({'location': url})
            else:
                return "Le fichier est trop gros. La taille maximale autorisée est de 5 Mo."

        except Exception as e:
            return f"Erreur lors de l'ouverture de l'image : {e}"
    else:
        return "Type de fichier non autorisé. Seuls jpg, jpeg, gif et png sont autorisés."
