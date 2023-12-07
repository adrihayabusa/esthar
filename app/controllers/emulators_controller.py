from app.models.game_model import Game
from app.models.emulators_model import Emulators
from app.views import emulators_view


def get_emulator_list():
    return emulators_view.emulators_list()


def get_emulator(emulator_id, rom_filename):
    emulator = Emulators.query.get(emulator_id)
    game = Game.query.filter_by(image=rom_filename).first()
    return emulators_view.view_emulator(emulator, game, rom_filename)
