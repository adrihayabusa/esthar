# Personal Website using Flask
A minimalist personal portfolio and blog built with Flask and SQLAlchemy.

The purpose was to discover how to build a webapp with Python, by using a module which would allow me to create a MVC architecture.

This project is part of my initial personal training related to Python.

## Overview
Esthar is a lightweight web application designed to showcase my personal projects and share articles about IT trainings, animes, and general IT culture.
It has been built with Python, using Flask as a backend and SQLAlchemy for ORM, it serves as a digital space to express ideas and document work.

I hesitated between Flask and Django. Because of the limited scope of this project, I have decided to go with Flask as it seems very fast to put in production.

## 🛠️ Tech Stack
- **Python 3**
- **Flask** — micro web framework
- **SQLAlchemy** — ORM for database management
- **Jinja2** — templating engine
- **HTML/CSS/JS** — frontend structure and styling. JS includes popular modules: jQuery, Prism, emulatorJS.

## 📁 Project Structure

```bash
esthar/
├── app/              # Core application logic 
├── static/           # Static assets (CSS, JS, images)
├── templates/        # HTML templates 
├── run.py            # Entry point to launch the app 
└── .gitignore        # Git configuration
```

## 📝 Features
- Personal portfolio homepage
- Article/blog section
- Category tagging for notes
- Responsive design (basic styling) handling 
- Easy to extend and customize

## 🧪 Setup & Run
- Clone the repository:
   ```bash
   git clone https://github.com/adrihayabusa/esthar.git
   cd esthar
   ```

- Create a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate  ; On MacOS and Linux
env\\Scripts\\activate   ; On Windows
```

- Install dependencies:

`pip install -r requirements.txt  # If we consider your dependencies within a TXT file.`

Here is the list : `flask flask_babel flask_login flask_sqlalchemy flask_wtf werkzeug`

Also, I have been using MariaDB for the database. You will have to install it, or to adapt the config file if you want to use another applicaion, like MongoDB or NoSQL for example.

If you want to go with mariaDb, please refeer to the official documentation available here : https://mariadb.com/get-started-with-mariadb

- Add a config.py file inside the \app folder

This file will be used to setup a login session, and it also contains your login information to access the database.

Here is a template:

```python
SQLALCHEMY_DATABASE_URI = ""
SECRET_KEY = ""
UPLOAD_FOLDER = ""
RESUME_DATA = ""
```
You only need the four global constants above.

- Run the app:

`python run.py`

## 📌 Notes

This project is a personal experiment and learning tool. Feel free to ask any questions, take it and adapt as you need, or report any problem.

## 💥 Issues

25/07/2024 - Since my last commit, the form to create a note might be broken. To be fixed soon.

## 📫 Contact

Created by Adrien LEBORGNE — feel free to reach out via GitHub for feedback or collaboration.
