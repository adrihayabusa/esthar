from flask import render_template


def login(form_user):
    return render_template('user/login.html', form_user=form_user)
