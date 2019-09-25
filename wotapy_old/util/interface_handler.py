from wotapy.util.interface import Interface

class InterfaceHandler:
    def __init__(self):
        self.breadcrumb = []
        pass

    def open(self, interface: Interface):
        self.breadcrumb.append(interface)
        interface.set_handler(self)
        interface.open() #TODO implement interface opening
    
    def remove(self, interface):
        try:
            self.breadcrumb.remove(interface)
        except ValueError:
            raise ValueError('The interface handler cannot remove the interface as it doesn\'t have it')
