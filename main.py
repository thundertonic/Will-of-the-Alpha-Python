from terminal_palette import Palette
import cli
import sys

pal = Palette()

print('----------------', pal.bright_magenta('Will of the Alpha'), pal.bg_cyan.black('Created with ❤️ by Veloce Wattwing ⚡🐉⚡'), '----------------', sep='\n')
game_state = {}
print()
cli.print_card('Will of the Alpha', 5, 12, 2, 'On Summon: The ultimate game begins...')
print()

def new_game():
    """Create a new game. Populate the game_state dictionary."""
    game_state['name'] = cli.prompt_string('Name your save: ', coerse=True)
    cli.print_warning('Currently, you may only play a random given set of cards.')

choice = cli.prompt_choice(cli.format_title('Main Menu'), True, 'New Game', 'Exit')

# a function dictionary for the main menu
run_dict = {
    'New Game': lambda : new_game(),
    'Exit': lambda : sys.exit(0)
}

# run such dict
run_dict[choice]()