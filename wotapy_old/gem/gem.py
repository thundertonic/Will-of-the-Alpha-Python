from wotapy.game.main import pal

class Element:

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return 'element:' + self.name

FIRE = Element('fire', pal.yellow.bg_red.bold('F'))
WATER = Element('water', pal.white.bg_blue.bold('~'))
EARTH = Element('earth', pal.black.bg_green.bold('#'))
DEATH = Element('death', pal.white.bg_black.bold('%'))
CELESTIAL = Element('celestial', pal.yellow.bg_magenta.bold('*'))
IMPURITY = Element('impurity', pal.rgb(0, 0, 0).bg_rgb(84, 84, 84).bold('/'))

class Gem:
    
    def __init__(self, comp: list):
        self.comp = comp
    
    def __str__(self):
        self.graphics

    def graphics(self):
        s = ''
        for r in self.comp:
            for e in r:
                s += e.symbol
            s += '\n'
        return s
    
    @staticmethod
    def gen_random(purity, size, dominant_ele=None):
        pass
    
    @staticmethod
    def gen_random_normal(puritymu, puritysigma, sizemu, sizesigma, dominant_ele=None):
        import numpy.random as ran

        return Gem.gen_random(ran.normal(puritymu, puritysigma), ran.normal(sizemu, sizesigma), dominant_ele=dominant_ele)