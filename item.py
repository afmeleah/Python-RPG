
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Credchip(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Credchip",
                         description="A credchip that has {} nuyen loaded onto it.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class Bat(Weapon):
    def __init__(self):
        super().__init__(name="Baseball Bat",
                         description="Knock 'em out of the park with this old fashioned slugger.",
                         value=0,
                         damage=5)
 
class Pistol(Weapon):
    def __init__(self):
        super().__init__(name="Ares Predator",
                         description="The Ares classic is considered a premier heavy pistol.",
                         value=10,
                         damage=10)

class Rifle(Weapon):
    def __init__(self):
        super().__init__(name="Ares Alpha",
                         description="Ares' top of the line assault rifle.",
                         value=30,
                         damage=15)