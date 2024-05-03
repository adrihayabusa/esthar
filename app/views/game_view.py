from flask import render_template


def game_list(games):
    return render_template('game/list.html', games=games)


def game_detail(game, high_scores):
    return render_template('game/detail.html', game=game, high_scores=high_scores)


def add_game(emulators):
    return render_template('game/add.html', emulators=emulators)
