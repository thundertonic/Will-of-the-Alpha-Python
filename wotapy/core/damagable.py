from wotapy.objects.property import Property
from wotapy.objects.signal import Signal
from wotapy.core.move import SActEnded

"""
This namespace contains all implements related to health, damage, and defence
"""

class SAssault(Signal):
    """
    Sent by an attacker to the defender, dealing health damage
    """
    def get_required_fields(self):
        return ['dmg']

class SDefenceUsed(Signal):
    """
    Sent to reduce the pending health damage
    """
    def get_required_fields(self):
        return ['def']

class Damagable(Property):
    """
    Property of anything that has health and can be damaged
    """
    def __init__(self, actor=None, **fields):
        # super().__init__(actor, fields)
        self.health = fields['health']
        self.pending_damage = 0

    def get_required_fields(self):
        return ['health']
    
    def on_signal(self, signal):
        sigcls = type(signal)

        if sigcls is SAssault:
            self.pending_damage += signal.query('dmg')
        
        if sigcls is SDefenceUsed:
            self.pending_damage -= signal.query('def')
            if self.pending_damage < 0: # ramp function so pending damage don't become negative
                self.pending_damage = 0
        
        if sigcls is SActEnded:
            # apply the pending damage and reset it
            self.health -= self.pending_damage
            self.pending_damage = 0
        
        if self.health <= 0:
            # Rest In Potato
            self.actor.destroy() 