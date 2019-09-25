from wotapy.util.palette import palette
from wotapy.objects.actor import Actor

"""
By convention, 2D lists have x-axis on the horizontal axis (sub list index in list), pointing to the right, and y-axis on the vertical axis (list index), pointing down
"""

class Place:
    """
    A 2D plane holding Actors with coordinates. Actors may be in the same coordinate space.
    """

    def __init__(self, list2d, **palette):
        self.xsize, self.ysize = len(list2d[0]), len(list2d)
        self.manifest = []

        # read each char entry, and see if it fits a key in the palette dictionary
        # if is, it creates a new actor based on the id and the coordinate the char is from into the Place
        for y in range(self.ysize):        
            for x in range(self.xsize):
                for key in palette:
                    if list2d[y][x] is key:
                        id = palette[key]
                        coord = (x, y)
                        self.manifest.append(Actor(id, coord)) # TODO: Palette isn't compatible with properties yet
    
    # return a 2d list of chars representing a view of the place
    def illustrate(self):
        # 2d list of chars
        # empty is rep by '.'
        charlist = [['.' for i in range(self.xsize)] for i in range(self.ysize)]
        for actor in self.manifest:
            charlist[actor.get_y()][actor.get_x()] = actor.illustrate()
        
        return charlist

    def spawn(self, *actors):
        for actor in actors:
            self.manifest.append(actor)
            actor.place = self
    
    def despawn(self, *actors):
        for actor in actors:
            self.manifest.remove(actor)
            actor.place = None # remove the attribute that this actor belong to this place, in case it is still referenced somewhere else

    def signal(self, signal):
        """
        This function should be used wisely as it needs to go through conditionals of every property of every actor of this place.
        """
        for a in self.manifest:
            a.signal(signal)
    
def viewport(charlist):
    """
    Turns a 2D list of chars, denoting a view of a Place, into printable string with coordinate numberings on the side
    """
    ysize = len(charlist)
    xsize = len(charlist[0])

    string = ''

    # turn the 2d list of chars into a printable string, with numbering on the side
    # numbering on the top, with yellow zeros
    string += ' ' # space on the side to account for the side numbering
    for x in range(xsize):
        xnum = str(x % 10)
        if xnum == '0':
            xnum = palette.black.bg_yellow(xnum)
        string += xnum

    string += '\n'

    for y in range(ysize):
        # add numbering on the side, with yellow zeros
        ynum = str(y % 10)
        if ynum == '0':
            ynum = palette.black.bg_yellow(ynum)
        string += ynum

        # print row
        for x in range(xsize): 
            string += charlist[y][x]
        string += '\n'

    return string