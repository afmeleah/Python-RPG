import item, worldmap, random
from colors import Colors
 
class Player():
    def __init__(self):
        self.inventory = [item.Credchip(15), item.Bat()]
        self.hp = 100
        self.location_x, self.location_y = worldmap.starting_position
        self.victory = False
 
    def is_alive(self):
        return self.hp > 0
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(worldmap.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
            best_weapon = None
            max_dmg = 0
            for i in self.inventory:
                if isinstance(i, item.Weapon): 
                    if i.damage > max_dmg:
                        max_dmg = i.damage
                        best_weapon = i
            #this checks if any items in the inventory are weapons in the item class. It'll grab the best weapon from inv and use it.

            print(f"{Colors.WARNING}You use {best_weapon.name} against {enemy.name}!{Colors.ENDC}")
            enemy.hp -= best_weapon.damage
            if not enemy.is_alive():
                print(f"{Colors.WARNING}You killed {enemy.name}!{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}{enemy.name} HP is {enemy.hp}.{Colors.ENDC}")

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__) #the getattr searches for the method in the action class
        if action_method:
            action_method(**kwargs) #the kwargs is needed if the method that is found needs additional objects like the attack method

    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 # the kwargs is used to grab a certain action of its parameters are met like the attack action or flee.

    def __str__(self):
        return f"{self.hotkey}: {self.name}"

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='w')
 
class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')
 
class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='d')
 
class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='a')
 
class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='r', enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Run", hotkey='f', tile=tile)