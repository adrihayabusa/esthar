from flask import render_template


def list_animes(animes):
    return render_template('anime/list.html', animes=animes)


def add_anime(form):
    return render_template('anime/add.html', form=form)


def anime_detail(anime):
    return render_template('anime/view.html', anime=anime)
