class Place:
    def __init__(self, name: str, links: list):
        self.links = links
        self.name = name
    
    def has_link(self, name: str) -> bool:
        for l in self.links:
            if l.name == name:
                return True
        
        return False

    def add_link(self, place: Place) -> None:
        self.links.append(place)
    
    def remove_link(self, place: Place) -> None:
        place_found = False

        for l in self.links:
            if l == place:
                self.links.remove(l)
                place_found = True
        
        if not place_found:
            raise ValueError(self.name + ' is not linked to the specified place ' + place.name)
        
