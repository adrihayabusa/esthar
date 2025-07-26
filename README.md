# Esthar - Personal Website  
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
source venv/bin/activate  ; On MacOS and Linux
venv\\Scripts\\activate   ; On Windows
```

- Install dependencies:

pip install -r requirements.txt  # If we consider your dependencies within a TXT file.

- Run the app:

python run.py

📌 Notes

This project is a personal experiment and learning tool. Feel free to ask any questions, take it and adapt as you need, or report any problem.

💥 Issues

From my last commit, I remember that the form to create a note might be broken. To be fixed soon.

📫 Contact

Created by Adrien LEBORGNE — feel free to reach out via GitHub for feedback or collaboration.
