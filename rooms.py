# from unit import Unit, Player
# from item import Item, Potion, Shield, BFS

# class MapTile:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def intro_text(self):
#         raise NotImplementedError()

#     def modify_player(self, player):
#         raise NotImplementedError()

# class StartingRoom(MapTile):
#     def intro_text(self):
#         return """
#         You stand at the mouth of a cave and crouch down. The tracks go further in.
#         A flickering torch in the distance reveals four paths. Time to get to work.
#         """

#     def modify_player(self, player):
#         pass

# class LootRoom(MapTile):
#     def __init__(self, x, y, item):
#         self.item = item
#         super().__init__(x, y)

#     def add_loot(self, player):
#         player.inventory.append(self.item)

#     def modify_player(self, player):
#         self.add_loot(player)

# class EnemyRoom(MapTile):
#     def __init__(self, x, y, enemy):
#         self.enemy = enemy
#         super().__init__(x, y)
#     def modify_player(self, player):
#         if self.enemy.is_alive():
#             player.health = player.health - enemy.attack_power
#             print(f"{enemy.name} does {enemy.attack_power} damage. You have {player.health} HP remaining.")

# class EmptyCavePath(MapTile):
#     def intro_text(self):
#         return """
#         The cave streches forward empty and unremarkable. You need to keep moving.
#         """
    
#     def modify_player(self, player):
#         pass

# class GiantSpiderRoom(EnemyRoom):
#     def __init__(self,x. y):
#         super().__init__(x,y, enemies.GiantSpider())

#     def intro_text(self):
#         if self.enemy.is_alive():
#             return """"
#             You wander forward into the room. Dirt and rubble shift suddenly as a massive form rockets toward you.
#             It's a giant spider!
#             """
#         else:
#             return """
#             The corpse of the massive spider lies where you left it.
#             """

class Room:
    def __init__(self, name, description, position):
        self.name = name
        self.description = description
        self.position = position

    def interact(self):
        pass

# Room("start", """
#     The Halloweeners have control of this floor of the Megaplex.
#     You've got work to do.
#     """, [0,0])

