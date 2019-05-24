from wotapy.card.char_card import CharCard
import wotapy.util.cli as cli

# a lambda function that does nothing. Fits the format of (subject, strength_max)
NO_ACT = lambda su, st: None

# used to display strength

class Ability:

    def __init__ (self, self_do, upon_do, name, dscp, strength_max=1):

        if self_do is None:
            self.self_do = NO_ACT
        else:
            self.selfdo = self_do
        
        if upon_do is None:
            self.upon_do = NO_ACT
        else:
            self.upon_do = upon_do
        
        self.dscp = dscp
        self.strength_max = strength_max

    def do (self, subject, object, strength):
        """Committ the ability with a given strength"""
        strength_max = self.strength_max

        if strength > strength_max:
            self.self_do(subject, strength_max)
            self.upon_do(object, strength_max)
        else:
            self.self_do(subject, strength)
            self.upon_do(object, strength)

def heal(subject, strength):
    try:
        total_health = 2 * strength
        subject.health += total_health
        cli.print_action(subject.name + ' gained ' + cli.health(total_health))
        
    except NameError:
        # the subject does not have a health field. TODO as this feels like a bad practice. I will change health to an entry in a dictionary
        print('Healing did not do anything upon ' + subject.name + ' as they cannot be healed!')

HEAL = Ability(heal, lambda st, su: None, 'Heal', 'Heals', strength_max=8)

