from app.models.user_model import User, Role
from app.views import user_view
from app import login_manager
from flask import redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from functools import wraps
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField("Login", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('You need to be logged in to access this page.', 'danger')
            return redirect(url_for('main.login'))

        admin_role = Role.query.filter_by(name='superadmin').first()
        if not admin_role or admin_role not in current_user.roles:
            flash('You do not have the required permissions to access this page.', 'danger')
            return redirect(url_for('main.home'))

        return f(*args, **kwargs)
    return decorated_function


def login():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')

        user = User.query.filter_by(login=login).first()

        # Vérifiez si l'utilisateur existe et si le mot de passe est correct
        if user and user.verify_password(password):
            login_user(user)
            session.permanent = True
            flash("Logged in successfully!", "success")
            return redirect(url_for('main.home'))

        flash("Invalid credentials", "danger")
        return redirect(url_for('main.login'))

    form_user = LoginForm()
    return user_view.login(form_user)


def logout():
    logout_user()
    return redirect(url_for('main.home'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
