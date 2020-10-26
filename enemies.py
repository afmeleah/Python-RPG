class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Halloweener(Enemy):
    def __init__(self):
        super().__init__(name="Halloweener", hp=20, damage=10)
 
class StreetSam(Enemy):
    def __init__(self):
        super().__init__(name="Street Samurai", hp=40, damage=15)

class Junkie(Enemy):
    def __init__(self):
        super().__init__(name="BTL Junkie", hp=10, damage=5)