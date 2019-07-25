from terminal_palette import Palette
from wotapy.util import cli

def begin():
    pal = Palette()

    print(pal.yellow('*   *   *   *   *   *'))
    print()
    print('Welcome. I\'ve been expecting you. We have much to discuss.')

    name = cli.prompt_string('Now, what is your name? ', coerse=True)

    print(name + '... What a beautiful name! I think it should be put to good use.')
    print('You have the honour to endow a fortunate vessel with your name in this dangerous yet magnificent world.') 
    print('This vessel shall be the Alpha. It will help you fulfill the purpose of your will, while you will help guide it with your wisdom. Together, you are mutually synthesized.')
    print('As such, this Alpha will be of utmost importance to you, so I advice you to choose wisely.')
    print()

    cli.prompt_choice_tree(
        'What shall this vessel be?',
        True,
        ('One created by chance', lambda: random_char()),
        ('One created by my will', lambda: char_creation()),
        ('One created from a template [WIP]', lambda: None)
    )