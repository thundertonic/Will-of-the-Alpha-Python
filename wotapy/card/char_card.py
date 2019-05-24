from abc import ABC, abstractmethod
import uuid

class CharCard(ABC):
    """Abstract class that enforces properties of character cards."""

    def __init__(self, c_uuid=None):
        if uuid is None:
            self.uuid = c_uuid.UUID()
        else:
            self.uuid = c_uuid
        
# class OnSummon(ABC):
#     """Abstract method class for cards that causes actions upon summoning"""

#     @abstractmethod
#     def on_summon(self):
#         pass

class Firefly(CharCard):
    def __init__(self):
        super().__init__()

    def coerse(self):
        print('bye')


firefly = Firefly()
firefly.coerse()
