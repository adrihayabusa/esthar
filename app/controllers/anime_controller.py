from app.models.anime_model import Anime
from app.views import anime_view
from app.forms import AddAnimeForm
from app import db
from flask import redirect, url_for


def get_list_animes():
    animes = Anime.query.all()
    return anime_view.list_animes(animes)


def get_anime_by_id(anime_id):
    anime = Anime.query.get(anime_id)
    return anime_view.anime_detail(anime)


def add_anime():
    form = AddAnimeForm()
    if form.validate_on_submit():
        anime = Anime(
            name=form.name.data,
            genre=form.genre.data,
            release_year=form.release_year.data,
            violence_level=form.violence_level.data,
            age_restriction=form.age_restriction.data,
            explicit_content=form.explicit_content.data
        )

        db.session.add(anime)
        db.session.commit()

        return redirect(url_for('main.home'))  # TODO redirect to anime.anime_details
    return anime_view.add_anime(form)
