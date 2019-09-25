class Character:
    
    def __init__(self, health, stamina, abilities=[]):
        self.health = health
        self.stamina = stamina
        self.abilities = abilities

    def attack(self, target, strength):
        target.health -= strength

    def heal(self, target, strength):
        target.health += strength
    
char1 = Character(5, 1)
char2 = Character(4, 1)