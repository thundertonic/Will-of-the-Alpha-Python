from terminal_palette import Palette
import re

pal = Palette()

def print_error(text):
    print(pal.red.bold.bg_default('[X] ' + text))

def format_error(text):
    return pal.red.bold.bg_default('[X] ' + text)

def print_warning(text):
    print(pal.black.bg_yellow.bold('[!] ' + text))

def format_warning(text):
    return pal.black.bg_yellow.bold('[!] ' + text)

def format_key(text):
    return pal.black.bg_white.bold(' ' + text + ' ')

def format_title(text):
    return pal.yellow.bg_default.bold(text)

# TODO moves this to a card class later on
def print_card(name, health, total_health, damage, perk):
    string = '[' + name + '] ' + pal.red.bg_default('♥') * health + pal.red.bg_default('♡') * (total_health - health) + '/' + pal.yellow.bg_default('✶') * damage + '\n' + pal.cyan.bg_default(perk)
    print(string)

def prompt_int(prompt, coerse=False, min=None, max=None):
    """
    Prompts the user for an integer input with the given prompt.
    If `coerse = True`, forces the user to enter a input without an exit option
    """
    if type(min) is int:
        if type(max) is int:
            prompt += ' ' + pal.black.bg_white('[' + str(min) + ' - ' + str(max) + ']')
        else:
            prompt += ' ' + pal.black.bg_white('[' + str(min) + ' - ...]')
    else:
        if type(max) is int:
            prompt += ' ' + pal.black.bg_white('[... - ' + str(max) + ']')
        
    if not coerse:
        prompt += ' or enter ' + format_key('..') + ' to cancel'

    prompt += ': '

    # Coerce loop
    while True:
        answer = input(prompt)

        if answer == '..' and not coerse:
            return None
        
        try:
            answer = int(answer)
            if type(min) is int and int(answer) < min:
                print_error('Your value must be higher than ' + str(min))
            elif type(max) is int and int(answer) > max:
                print_error('Your value must be less than ' + str(max))
            else:
                return answer
        except ValueError:
            print_error('You must enter a valid integer')

def prompt_float(prompt, coerse=False, min=None, max=None):
    """
    Prompts the user for a float input with the given prompt.
    If `coerse = True`, forces the user to enter a input without an exit option
    """
    if type(min) is float:
        if type(max) is float:
            prompt += ' ' + pal.black.bg_white([' + str(min) + ' - ' + str(max) + '])
        else:
            prompt += ' ' + pal.black.bg_white('[' + str(min) + ' - ...]')
    else:
        if type(max) is int:
            prompt += ' ' + pal.black.bg_white('[... - ' + str(max) + ']')
        
    if not coerse:
        prompt += ' or enter ' + format_key('..') + ' to cancel'

    prompt += ': '

    # Coerce loop
    while True:
        answer = input(prompt)

        if answer == '..' and not coerse:
            return None

        try:
            answer = int(answer)
            if type(min) is int and int(answer) < min:
                print_error('Your value must be higher than ' + str(min))
            elif type(max) is int and int(answer) > max:
                print_error('Your value must be less than ' + str(max))
            else:
                return answer
        except ValueError:
            print_error('You must enter a valid integer')

def prompt_string(prompt: str, coerse=False, blacklist_word=None, black_patt=None, white_patt=None):
    """
    Prompts the user for a string input with the given prompt.
    If `coerse = True`, forces the user to enter a input without an exit option.
    `blacklist_word` is not case-sensitive.
    """
    if not coerse:
        prompt += ' or enter ' + format_key('..') + ' to cancel'

    while True:
        forbids = False
        answer = input(prompt)

        if answer == '..' and not coerse:
            return None
        
        # check user input for blacklist pattern
        if black_patt is not None:
            # if the blacklist pattern is found
            if re.match(black_patt, answer) is not None:
                print_error(answer + ' may not be used as a response.')
                continue
        
        # check user input for blacklist pattern
        if white_patt is not None:
            # if the whitelist pattern is not found
            if re.match(white_patt, answer) is None:
                print_error(answer + ' may not be used as a response.')
                continue

        # check for forbidden words
        if blacklist_word is not None:
            # make answer case-insensitive
            lower_ans = answer.lower()
            for w in blacklist_word:
                # make forbidden word case-insensitive
                w = w.lower()
                
                if w in lower_ans:
                    print_error('You may not use the word \'' + w + '\'!')
                    forbids = True
                    break
            
            # if a improper answer is found
            if forbids is True:
                continue      

        return answer

def prompt_choice(prompt, coerse=False, *menu_items):
    """
    Prompts the user for an int input with the given prompt and item list.
    If `coerse = True`, forces the user to enter a input without an exit option
    """
    # Construct the message
    if not coerse:
        prompt += '\nEnter ' + format_key('..') + ' to cancel'
    
    for i in range(len(menu_items)):
        prompt += '\n' + format_key(str(i + 1)) + ' ' + menu_items[i]
    
    prompt += '\nSelect via number: '

    # Coerce loop  
    while True:
        answer = input(prompt)

        if answer == '..' and not coerse:
            return None

        try:
            answer = int(answer)
            if answer <= 0 or answer > len(menu_items):
                print_error('This is not a valid number for a menu item')
                continue

            return menu_items[answer - 1]
        except ValueError:
            print_error('Please type in the number of the item you wish to select')