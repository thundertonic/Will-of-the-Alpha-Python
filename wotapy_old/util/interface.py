from abc import ABC, abstractmethod
from wotapy.util.interface_handler import InterfaceHandler

class Interface(ABC):
    def __init__(self, handler=None):
        super().__init__()
        
        if handler is not None:
            self.set_handler(handler)

    @abstractmethod
    def __thread(self, kargs):
        pass
    
    def open(self, **kargs):
        self.__thread(kargs) # run the inteface, then when the thread ends, close it
        self.close()

    def set_handler(self, handler: InterfaceHandler):
        self.__handler = handler
    
    def close(self):
        self.__handler.remove(self)
    
    def evoke(self, interface: Interface):
        self.__handler.open(interface)