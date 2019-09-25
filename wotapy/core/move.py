from wotapy.objects.property import Property
from wotapy.objects.signal import Signal

"""
Everything here is related to character actions and turns.
"""

class SActEnded(Signal):
    """
    Sent to every Actor at the end of any character's act, after all the moves' pending effects have been calculated
    """
    def get_required_fields(self):
        return []

class SRoundEnded(Signal):
    """
    Sent to every Actor at the end of every character's turn, after when the slowest Actor's `SActEnded` is fired.
    """
    def get_required_fields(self):
        return []

class SDefenceUsed(Signal):
    """
    Sent to reduce the pending health damage
    """
    def get_required_fields(self):
        return ['def']

class Actable(Property):
    """
    Property of anything that can perform an act. They will have movement points to spend and will have a turn.
    """
    def __init__(self, actor=None, **fields):
        # super().__init__(actor, fields)
        self.mvmt_pt = fields['mvmt_pt']
        self.pending_damage = 0

    def get_required_fields(self):
        return ['mvmt_pt']
    
    def on_signal(self, signal):
        pass