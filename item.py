class Item:
    def __init__(self, name, position):
        self.position = position
        self.name = name
    
class StimPack(Item):
    def __init__(self, name, position):
        super().__init__(name,position)
        self.owner = None
    
    def use(self):
        self.owner.health += 10
        for i in range(len(self.owner.inventory)):
            if self.owner.inventory[i] == self:
                del self.owner.inventory[i]
        self.owner = None

    
    def get_picked_up(self,owner):
        self.owner = owner
        self.position = [-555555,-555555]

class Jazz(Item):
    def __init__(self, name, position):
        super().__init__(name,position)
        self.owner = None
    
    def use(self):
        self.owner.health -= 2
        self.owner.attack_power +=5
        for i in range(len(self.owner.inventory)):
            if self.owner.inventory[i] == self:
                del self.owner.inventory[i]
        self.owner = None

    
    def get_picked_up(self,owner):
        self.owner = owner
        self.position = [-3333,-3333]

class Armor(Item):
    def __init__(self, name, position):
        super().__init__(name,position)
        self.owner = None

    def use(self):
        self.owner.defense += 2
        for i in range(len(self.owner.inventory)):
            if self.owner.inventory[i] == self:
                del self.owner.inventory[i]
        self.owner = None

    def get_picked_up(self, owner):
        self.owner = owner
        self. position = [-999, -999]

class BFG(Item):
    def __init__(self, name, position):
        super().__init__(name,position)
        self.owner = None

    def use(self):
        self.owner.attack_power += 5
        for i in range(len(self.owner.inventory)):
            if self.owner.inventory[i] == self:
                del self.owner.inventory[i]
        self.owner = None

    def get_picked_up(self, owner):
        self.owner = owner
        self. position = [-999, -999]