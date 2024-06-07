from flask import render_template


def home(notes):
    return render_template('home.html', notes=notes)


def resume_view(resume_json, resume_data):
    return render_template('resume.html', resume=resume_data, resume_json=resume_json)

