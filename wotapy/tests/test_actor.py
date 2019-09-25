from wotapy.objects.actor import Actor
from wotapy.objects.place import Place
from wotapy.core.room_gen import empty_room
from wotapy.objects.property import Property
from wotapy.objects.signal import Signal

from wotapy.core.damagable import Damagable, SAssault

import pytest

def test_spawn_death():
    place = empty_room((15, 15))
    nomad = Actor('nomad', (5, 8), properties=[Damagable(health=12)], tags=['wild'])
    place.spawn(nomad)
    place.signal(SAssault(dmg=15))

    for actor in place.manifest:
        if actor.id is nomad:
            assert False
    
    assert True