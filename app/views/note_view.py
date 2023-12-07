from flask import render_template, request, redirect


def notes_list(notes):
    return render_template('note/list.html', notes=notes)


def add_note():
    return render_template('note/add.html')


def view_note(note, text):
    return render_template('note/view.html', note=note, text=text)


def update_note(note, text):
    return render_template('note/update.html', note=note, text=text)
