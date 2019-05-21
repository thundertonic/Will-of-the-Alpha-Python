# https://github.com/jeongukjae/terminal-palette/blob/master/README.md

from terminal_palette import Palette

pal = Palette()

class Symbol:
    """
    # Symbol
    An object that encapsulates properties of a symbol with color and decorator.
    """
    def __init__ (self, char, fg='default', bg='default', *decos):
        self.char = char
        self.fg = fg
        self.bg = bg
        self.decos = decos
    
    def get(self, char=None, fg=None, bg=None, *decos):
        """
        Returns the symbol as a formatted string. Any properties passed as arguments will override the ones from this symbol.
        """
        if char is None:
            char = self.char
        if fg is None:
            fg = self.fg
        if bg is None:
            bg = self.bg
        if len(decos) == 0:
            decos = self.decos

        # reset formattings before it
        symbol = pal.reset(char)

        # foreground coloring
        foreground = {
            'default': pal.default(symbol),
            'red': pal.red(symbol),
            'black': pal.black(symbol),
            'blue': pal.blue(symbol),
            'cyan': pal.cyan(symbol),
            'green': pal.green(symbol),
            'magenta': pal.magenta(symbol),
            'white': pal.white(symbol),
            'yellow': pal.yellow(symbol),
            'bright_black': pal.bright_black(symbol),
            'bright_blue': pal.bright_blue(symbol),
            'bright_cyan': pal.bright_cyan(symbol),
            'bright_green': pal.bright_green(symbol),
            'bright_magenta': pal.bright_magenta(symbol),
            'bright_red': pal.bright_red(symbol),
            'bright_white': pal.bright_white(symbol),
            'bright_yellow': pal.bright_yellow(symbol)
        }

        # print(foreground[fg])
        symbol = foreground[fg]

        # background coloring
        background = {
            'default': pal.bg_default(symbol),
            'red': pal.bg_red(symbol),
            'black': pal.bg_black(symbol),
            'blue': pal.bg_blue(symbol),
            'cyan': pal.bg_cyan(symbol),
            'green': pal.bg_green(symbol),
            'magenta': pal.bg_magenta(symbol),
            'white': pal.bg_white(symbol),
            'yellow': pal.bg_yellow(symbol),
            'bright_black': pal.bg_bright_black(symbol),
            'bright_blue': pal.bg_bright_blue(symbol),
            'bright_cyan': pal.bg_bright_cyan(symbol),
            'bright_green': pal.bg_bright_green(symbol),
            'bright_magenta': pal.bg_bright_magenta(symbol),
            'bright_red': pal.bg_bright_red(symbol),
            'bright_white': pal.bg_bright_white(symbol),
            'bright_yellow': pal.bg_bright_yellow(symbol),
        }

        # print(background[bg])
        symbol = background[bg]

        # decorations
        if 'bold' in decos:
            pal.bold(symbol)
        if 'underline' in decos:
            pal.underline(symbol)
        if 'reversed' in decos:
            pal.reversed(symbol)

        return symbol