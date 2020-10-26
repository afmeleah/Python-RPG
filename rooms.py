import item, enemies, worldmap, player
from colors import Colors

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError() #is there because there should never be a MapTile used directly. This'll pop up and stop it.

    def adjacent_moves(self):
        moves = []
        if worldmap.tile_exists(self.x + 1, self.y):
            moves.append(player.MoveEast())
        if worldmap.tile_exists(self.x - 1, self.y):
            moves.append(player.MoveWest())
        if worldmap.tile_exists(self.x, self.y - 1):
            moves.append(player.MoveNorth())
        if worldmap.tile_exists(self.x, self.y + 1):
            moves.append(player.MoveSouth())
        return moves
 
    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(player.ViewInventory())
    
        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        print(f"""{Colors.WARNING}
        The Halloweeners control this level of the Megaplex. It shows. The walls are
        covered in graffiti and scorch marks. Halloweeners do love their fire.
        You have a job to do. Time to get to work.
        {Colors.ENDC}""")

    def modify_player(self, player):
        pass

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(player.ViewInventory())
 
        return moves

class EmptyPath(MapTile):
    def intro_text(self):
        return """
        The halls stretch forward empty and unremarkable. You need to keep moving.
        """
    
    def modify_player(self, player):
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"{Colors.WARNING}Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining.{Colors.ENDC}")

    def available_actions(self):
        if self.enemy.is_alive():
            return [player.Flee(tile=self), player.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class PaydataRoom(MapTile):
    def intro_text(self):
        print(f"""{Colors.OKGREEN}
        You found the paydata, and your job is done.
         
        Good job on that milk run, chummer.
        {Colors.ENDC}""")
 
    def modify_player(self, player):
        player.victory = True

class HalloweenerRoom(EnemyRoom):
    def __init__(self,x, y):
        super().__init__(x,y, enemies.Halloweener())

    def intro_text(self):
        if self.enemy.is_alive():
            print(f"""{Colors.WARNING}
        You enter the run-down apartment. Some trid plays in the background.
            There's a crash as the Halloweener inside scrambles for his gun.
        {Colors.ENDC}""")

        else:
            print(f"""{Colors.WARNING}
        The corpse of the Halloweener lies where you left it.
        {Colors.ENDC}""")

class JunkieRoom(EnemyRoom):
    def __init__(self,x, y):
        super().__init__(x,y, enemies.Junkie())

    def intro_text(self):
        if self.enemy.is_alive():
            print(f"""{Colors.WARNING}
        You enter what looks to be a drug den. Several bodies lay splayed out around the room.
            You check them and their eyes roll back lost in stupor. One of the BTL
            Junkies in the corner leap up and rush at you.
        {Colors.ENDC}""")

        else:
            print(f"""{Colors.WARNING}
        The corpse of the BTL Junkie lies where you left it.
        {Colors.ENDC}""")

        

class StreetSamRoom(EnemyRoom):
    def __init__(self,x, y):
        super().__init__(x,y, enemies.StreetSam())

    def intro_text(self):
        if self.enemy.is_alive():
            print(f"""{Colors.FAIL}
            You see before you the cleanest room that you've come across so far.
            It looks to be the lab where the gangers cook their drugs. Its guard notices you
            and rushes forward. His mechanical arm opening up to reveal a blade.
        {Colors.ENDC}""")

        else:
            print(f"""{Colors.FAIL}
        The corpse of the Street Samurai lies where you left it.
        {Colors.ENDC}""")


class FindRifleRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, item.Rifle())
 
    def intro_text(self):
        print(f"""{Colors.OKBLUE}
        You walk into what appears to be the gang's makeshift armory. 
        As you sift through the room, you find something that stands out.
        It's a rifle! You pick it up.{Colors.ENDC}
        """)

class FindCredsRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, item.Credchip(10))
 
    def intro_text(self):
        print(f"""{Colors.OKBLUE}
        You find a room that seems to hold nothing of importance. 
        Hold on a second. You see something on the ground
        It's a credchip! You pick it up.{Colors.ENDC}
        """)

class FindBatRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, item.Bat())
 
    def intro_text(self):
        print(f""" {Colors.OKBLUE}
        You enter the room and find what looks to be some civilian's room.
        On your way out of the room, you notice something behind the front door.
        It's a bat! You pick it up.{Colors.ENDC}
        """)

class FindPistolRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, item.Pistol())
 
    def intro_text(self):
        print(f"""{Colors.OKBLUE}
        You walk into what appears to be a common room. 
        You notice something shiny in the corner.
        It's a pistol! You pick it up.{Colors.ENDC}
        """)