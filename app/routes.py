import os
from flask import current_app, Blueprint, send_from_directory
from app.controllers import \
    anime_controller, user_controller, note_controller, main_controller, \
    game_controller, emulators_controller

main_bp = Blueprint('main', __name__)
anime_bp = Blueprint('anime', __name__)
emulators_bp = Blueprint('emulators', __name__)
game_bp = Blueprint('game', __name__)
note_bp = Blueprint('note', __name__)


@main_bp.route('/', methods=['GET'])
def home():
    return main_controller.home()


@main_bp.route('/resume', methods=['GET'])
def get_resume():
    return main_controller.get_resume()


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    return user_controller.login()


@main_bp.route('/logout')
def logout():
    return user_controller.logout()


@anime_bp.route('/animes')
def anime_list():
    return anime_controller.get_list_animes()


@anime_bp.route('/animes/<int:anime_id>')
def anime_detail(anime_id):
    return anime_controller.get_anime_by_id(anime_id)


@game_bp.route('/games')
def game_list():
    return game_controller.get_all_games()


@game_bp.route('/games/add', methods=['GET', 'POST'])
@user_controller.admin_required
def create_game():
    return game_controller.add_game()


@game_bp.route('/games/<int:game_id>')
def game_detail(game_id):
    return game_controller.get_game_detail(game_id)


@note_bp.route('/notes')
def notes_list():
    return note_controller.get_notes_list()  # TODO Gérer la pagination


@note_bp.route('/notes/<int:note_id>')
def note_detail(note_id):
    return note_controller.get_note_detail(note_id)


@note_bp.route('/notes/add', methods=['GET', 'POST'])
@user_controller.admin_required
def create_note():
    return note_controller.add_note()


@note_bp.route('/notes/<int:note_id>/update', methods=['GET', 'PATCH'])
def update_note(note_id):
    return note_controller.update_note(note_id)


@emulators_bp.route('/emulators/<int:emulator_id>/<string:rom_filename>')
def emulator(emulator_id, rom_filename):
    return emulators_controller.get_emulator(emulator_id, rom_filename)


@emulators_bp.route('/emulators/')
def emulators_list():
    return emulators_controller.get_emulator_list()


@emulators_bp.route('/roms/<string:image_folder>/<path:filename>')
def get_game_image(image_folder, filename):
    roms_directory = os.path.join(current_app.root_path, 'files', 'roms', image_folder)
    return send_from_directory(roms_directory, filename)


@emulators_bp.route('/bios/<string:bios_folder>/<path:filename>')
def get_bios(bios_folder, filename):
    bios_directory = os.path.join(current_app.root_path, 'files', 'bios', bios_folder)
    return send_from_directory(bios_directory, filename)


@main_bp.route('/upload', methods=['POST'])
def upload_file():
    return main_controller.upload()
