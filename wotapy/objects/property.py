from abc import ABC, abstractmethod

class Property(ABC):
    """
    Held by an Actor and adds responsive properties to an Actor.
    Its main method of communicating with other properties within the same and other Actors is via Signal objects. It is capable of sending and receiving direct signals and relayed signals from the owner Actor as well as affecting the Actor itself.
    
    Constructor:
    ```
    def __init__(self, actor=None, **fields)
    ```

    Required functions for inheritance:
    ```
    def __init__(self, **fields)
    def on_signal(self, signal)
    def get_required_fields(self)
    ```

    Unless debugging, do not have an attribute `actor`. Actor constructor and `Actor.add_property()` will do the work for you.
    """

    def __init__(self, actor=None, **fields):
        self.actor = actor
        
        r_fields = self.get_required_fields()
        
        # make sure every required fields exist
        for rf in r_fields:
            exist = False
            for f in fields:
                if f is rf:
                    exist = True
            
            if not exist:
                raise ValueError('The Property {} requires the field \'{}\', which was not passed during initialization.'.format(str(type(self)), rf))
        
        self.fields = fields
    
    @abstractmethod
    def on_signal(self, signal):
        pass
    
    def local_signal(self, signal, signal_self=False):
        """
        Signal all properties within the actor which this property is in.
        """
        for p in self.actor.get_properties():
            if p is self and not signal_self:
                continue
            
            p.signal(signal)
    
    def areal_signal(self, signal, signal_self_actor=False):
        """
        Signal all actors within the place which the actor of this property is in.
        """
        for a in self.actor.place.manifest:
            if a is self.actor and not signal_self_actor:
                continue

            a.signal(signal)
    
    @abstractmethod
    def get_required_fields(self):
        pass
            