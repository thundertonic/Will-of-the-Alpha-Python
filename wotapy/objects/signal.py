from abc import ABC, abstractmethod

class Signal(ABC):
    """
    An abstract game object that is broadcasted by properties within and across Actors. It is listened for by properties.
    It can contain required fields to carry additional data, such as how much damage is dealt, etc.

    Constructor:
    ```
    def __init__(self, **fields)
    ```

    Required functions for inheritance:
    ```
    def get_required_fields(self)
    ```

    """

    def __init__(self, **fields):
        self.fields = fields

        r_fields = self.get_required_fields()
        
        # make sure every required fields exist
        for rf in r_fields:
            exist = False
            for f in fields:
                if f is rf:
                    exist = True
            
            if not exist:
                raise ValueError('The Signal {} requires the field \'{}\', which was not passed during initialization.'.format(str(type(self)), rf))

    def query(self, key):
        try:
            return self.fields[key]
        except KeyError:
            raise KeyError('The Signal {} does not contain the key \'{}\' when queried.'.format(str(type(self)), key))
    
    def twin_to(self, signal):
        return type(self) is type(signal)
    
    @abstractmethod
    def get_required_fields(self):
        pass