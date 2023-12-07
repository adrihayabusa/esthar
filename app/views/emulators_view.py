from flask import render_template


def emulators_list():
    return render_template('emulators/list.html')


def view_emulator(emulator, game, rom_filename):
    return render_template('emulators/view.html', emulator=emulator, game=game, rom_filename=rom_filename)
