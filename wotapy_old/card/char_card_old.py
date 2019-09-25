import uuid as uu
from copy import copy

class CardClass:
    """
    A class for the card classes
    """

    def __init__(self, name, prop=[], *super):
        self.name = name
        self.super = super # array of superclasses
        self.prop = prop

def unwrap_classes(cls: 'tuple') -> 'tuple':
    """
    Returns a tuple of classes where all dependencies (superclasses) of tuple `cls` are also listed.
    """
    unwrapped = list(cls)
    for x in unwrapped:
        if len(x.super) > 0:
            supcls = unwrap_classes(x.super)
            for y in supcls:
                if y not in cls:
                    unwrapped.append(y)
                    
    return tuple(unwrapped)

# all defined card classes
UNDEFINED = CardClass('undefined')
ABERRATION = CardClass('aberration')
CONSTRUCT = CardClass('construct')
LIVING = CardClass('living', ['health'])
FIRE = CardClass('fire')
LIGHT = CardClass('light', ['glow_level'])
STEALTH = CardClass('stealth')
FAUNA = CardClass('fauna', ['stamina'], LIVING)
FLORA = CardClass('flora', LIVING)
HUMAN = CardClass('human', FAUNA)
HORROR = CardClass('horror', STEALTH)
SPIRIT = CardClass('spirit', LIGHT)
FEY = CardClass('fey')

classes = [UNDEFINED, HUMAN, SPIRIT]
temp = unwrap_classes(classes)
for i in temp:
    print(i.name)

class CardChar:
    """
    Object that defines a playable character card.

    `name` defines its playable name
    `cls` defines the card class(es) which it belongs
    `archt` accepts an abstract CharCard that is a pre-defined character template
    `abstract` whether the CharCard is abstract (used for instantiation rather than used in the game)
    `**prop` kwarg properties can be added here, like health or strength
    
    The properties which archetypes defines can be overriden by name, cls, prop, or archetype.
    """

    def __init__(self, archt=None, *cls, name=None,  uuid=None, abstract=False, **prop):
        
        # create an unique identifier
        if not abstract:
            if uuid is None:
                self.uuid = uu.UUID()
            else:
                self.uuid = uuid
        
        self.name = name

        # merge the property dictionaries
        self.prop = {**self.prop, **prop}

        self.cls = unwrap_classes(cls)
        
    def mod_prop(self, name, value, nacheck=False):
        """
        Modify a property of this character.

        If `nacheck = True`, raises `KeyError` if the character does not have the property.
        """
        try:
            self.prop[name] = value
        except KeyError:
            if nacheck:
                raise KeyError
    
    def has_prop(self, name):
        """
        Returns `True` if the character does have the property.
        Otherwise, returns `False`.
        """
        try:
            self.prop[name]
        except KeyError:
            return False

        return True

        
# # class OnSummon(ABC):
# #     """Abstract method class for cards that causes actions upon summoning"""

# #     @abstractmethod
# #     def on_summon(self):
# #         pass

# # class Firefly(CharCard):
# #     def __init__(self):
# #         super().__init__()

# #     def coerse(self):
# #         print('bye')


# # firefly = Firefly()
# # firefly.coerse()
