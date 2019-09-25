class Place:
    def __init__(self, name: str, links: list, entities: list, *about: str):
        self.links = links
        self.name = name
        self.entities = entities
        self.about = list(about)
    
    def has_link(self, name: str) -> bool:
        for l in self.links:
            if l.name == name:
                return True
        
        return False

    def add_link(self, place) -> None:
        self.links.append(place)
    
    def remove_link(self, place) -> None:
        place_found = False

        for l in self.links:
            if l == place:
                self.links.remove(l)
                place_found = True
        
        if not place_found:
            raise ValueError(self.name + ' is not linked to the specified place ' + place.name)
    
    def add_about(self, *about):
        self.about += about
    
    def get_full_desc(self):
        
        desc = ''

        # describe the setting
        for a in self.about:
            desc += a + '\n'
        
        # list all entities
        if len(self.entities) > 0:
            desc += 'There are:\n'
            for e in self.entities:
                desc += e.about() + '\n'
        else:
            desc += 'There is nothing to be seen.\n'
        
        return desc