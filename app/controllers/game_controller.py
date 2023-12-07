from app.models.game_model import Game, HighScore
from app.views import game_view


def get_all_games():
    games = Game.query.all()
    return game_view.game_list(games)


def get_game_detail(game_id):
    game = Game.query.get(game_id)
    high_scores = HighScore.query.filter_by(game_id=game_id).all()
    return game_view.game_detail(game, high_scores)
