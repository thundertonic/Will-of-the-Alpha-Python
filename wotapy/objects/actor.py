from wotapy.util.palette import palette

actorset = {
    'wall': {
        'symbol': '#',
        'color': 'white',
        'bg_color': 'bright_black'
    },

    'nomad': {
        'symbol': 'N',
        'color': 'white',
        'bg_color': 'default'
    }
}

fg_color_fn = {
    'white': lambda x: palette.white(x),
    'bright_white': lambda x: palette.bright_white(x),
    'red': lambda x: palette.red(x),
    'bright_red': lambda x: palette.bright_red(x),
    'green': lambda x: palette.green(x),
    'bright_green': lambda x: palette.bright_green(x),
    'yellow': lambda x: palette.yellow(x),
    'bright_yellow': lambda x: palette.bright_yellow(x),
    'cyan': lambda x: palette.cyan(x),
    'bright_cyan': lambda x: palette.bright_cyan(x),
    'magenta': lambda x: palette.magenta(x),
    'bright_magenta': lambda x: palette.bright_magenta(x),
    'black': lambda x: palette.black(x),
    'bright_black': lambda x: palette.bright_black(x),
    'default': lambda x: palette.default(x)
}

bg_color_fn = {
    'white': lambda x: palette.bg_white(x),
    'bright_white': lambda x: palette.bg_bright_white(x),
    'red': lambda x: palette.bg_red(x),
    'bright_red': lambda x: palette.bg_bright_red(x),
    'green': lambda x: palette.bg_green(x),
    'bright_green': lambda x: palette.bg_bright_green(x),
    'yellow': lambda x: palette.bg_yellow(x),
    'bright_yellow': lambda x: palette.bg_bright_yellow(x),
    'cyan': lambda x: palette.bg_cyan(x),
    'bright_cyan': lambda x: palette.bg_bright_cyan(x),
    'magenta': lambda x: palette.bg_magenta(x),
    'bright_magenta': lambda x: palette.bg_bright_magenta(x),
    'black': lambda x: palette.bg_black(x),
    'bright_black': lambda x: palette.bg_bright_black(x),
    'default': lambda x: palette.bg_default(x)
}

class Actor:
    """
    A game object with a coordinate in a Place. It can hold properties and an object ID, `id`.
    
    Constructor:
    ```
    def __init__(self, id, coord2d, properties=[], tags=[], place=None)
    ```

    Unless debugging, do not have an attribute `place`. `Place.spawn()` will do the work for you.
    """
    def __init__(self, id, coord2d, properties=[], tags=[], place=None):
        self.x, self.y = coord2d[0], coord2d[1]
        self.id = id
        self.place = place

        # initiated the fact that these properties belong to this Actor
        for p in properties:
            p.actor = self
        
        self.properties = properties
        self.tags = tags
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_place(self):
        if self.place is None:
            raise AttributeError('The actor with ID \'{}\' does not belong to a place.'.format(self.id))
        else:
            return self.place
    
    def add_property(self, *properties):
        for p in properties:
            p.actor = self
            self.properties.append(property)
    
    def get_properties(self):
        return self.properties
    
    def get_property(self, prop_class):
        """
        Returns the first occurence of the property with type `prop_class` in the Actor.
        
        If there are no property with type `prop_class`, returns `None`.

        Note: This is such a common function that there is a shorthand: `prop(self, prop_class)`.
        """
        for p in self.properties:
            if type(p) is prop_class:
                return p
        
        return None
    
    def prop(self, prop_class):
        """
        Shorthand for get_property(self, prop_class).
        """

        self.get_property(prop_class)
    
    def has_tag(self, tag):
        for t in self.tags:
            if type(tag) is type(t):
                return True
        return False

    def destroy(self):
        self.get_place().despawn(self)

    def illustrate(self):
        symbol = actorset[self.id]['symbol']
        color = actorset[self.id]['color']
        bg_color = actorset[self.id]['bg_color']

        # the color functions are lambda fns held inside of a dictionary
        return fg_color_fn[color](bg_color_fn[bg_color](symbol))

    def signal(self, signal):
        """
        Pass the signal to every one of the actor's properties.
        Signal should be used wisely, and if possible, use target_signal() instead. TODO: implement target_signal
        Signaling every properties in an Actor is resource-intensive and goes through a lot of conditionals just to do one task.
        """
        for p in self.properties:
            p.on_signal(signal)
    
    def signal_to(self, signal, *actor):
        for a in actor:
            a.signal(signal)