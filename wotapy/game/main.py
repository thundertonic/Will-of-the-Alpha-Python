import sys

from terminal_palette import Palette

from wotapy.util import cli
from wotapy.game.dialogues import intro

def main():

    # initialize the terminal_palette module
    pal = Palette()

    print('----------------',
        pal.bright_magenta('Will of the Alpha'),
        pal.bg_cyan.black('Created with ❤️ by Veloce Wattwing ⚡🐉⚡'),
        '----------------',
        sep='\n'
        )

    game_state = {}

    def new_game():
        """Create a new game. Populate the game_state dictionary."""
        game_state['name'] = cli.prompt_string('Name your save: ', coerse=True)
        
        intro.begin()

    cli.prompt_choice_tree(
        cli.title('Main Menu'),
        True,
        ('New Game', lambda: new_game()),
        ('Exit', lambda: sys.exit(0))
    )
