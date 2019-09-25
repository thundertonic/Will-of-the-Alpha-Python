import sys
from terminal_palette import Palette

# as other packages depend on it, this field must be defined before any packages can be imported
pal = Palette()

from wotapy.util import cli
from wotapy.game.dialogues import intro
from wotapy.world.place import Place

def main():

    print(
        '----------------',
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
    
    def sandbox():

        sandbox = Place('a sandbox', [], [], 'It is an empty and uninteresting place.')

        cli.log('You\'re in ' + sandbox.name)
        cli.log(sandbox.get_full_desc())
        
        while True:
            cli.prompt_string('What would you like to do?', coerse=True)
        
        # game = Game()
        # game.add_commset(commset.core)
        # game.add_commset(commset.conversation)
        # game.add_commset(commset.cheat)
        # game.center_on()

    cli.prompt_choice_tree(
        cli.title('Main Menu'),
        True,
        ('New Game', lambda: new_game()),
        ('Sandbox', lambda: sandbox()),
        ('Exit', lambda: sys.exit(0)),
    )

class Game:

    DAY_CYCLE = 86400

    # commset = [
    #     {
    #         main: 'wait',
    #         args: ['minutes: int'],
    #         action: lambda args: self.wait(args[0])
    #     }
    # ]

    def __init__(self, commset):
        self.time = 0
        self.commset = commset
    
    def wait(self, minutes):
        self.time += minutes
    
    def get_timeofday(self):
        return self.time % self.DAY_CYCLE

    def parse_command(self, comm: str):
        ls = comm.split()
        main = ls[0]

        # does this command exist?
        for c in Game.commset:
            if c['main'] is main:
                args = ls[1:]
                
                try:
                    c['action'](args)
                except ValueError:
                    cli.log('')

        cli.log('The command ' + main + ' does not exist.')

            
    
    
