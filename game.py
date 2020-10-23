from unit import Unit, Player
from item import Item, StimPack, Armor, BFG, Jazz
from rooms import Room
import random
import time
from colors import Colors

# name = input("""
# Oi, chummer! Don't worry. This is going to be a milk run.
# Easy smash and grab on some tweeked out gangers.
# What's your name again, bud?
# """)

name = "Hero"
player = Player(name, [0,0])



enemies = [
    Unit("Street Samurai", [3,1], 10, 4),
    Unit("Halloweener", [1,2], 5, 2),
    Unit("BTL Junkie", [0,1], 2, 3),
    Unit("Kill Me!", [1, 0], 15, 15)
]

items = [
    Item("Paydata", [3, 3]),
    StimPack("StimPack", [-1, 2]),
    Armor("Armored Jacket", [-2, 0]),
    BFG("Ares Alpha",  [1, 2]),
    Jazz("Jazz", [0,1])
]
Rooms = [
    Room("start", """
    The Halloweeners have control of this floor of the Megaplex.
    You've got work to do.
    """, [0,0]),
    Room("drugden", """
    You enter the room. Several bodies lay splayed out around the room.
    You check them and their eyes roll back lost in stupor. """, [0,1]),
    Room("armory", """
    The door opens and you find the gang's armory.
    A thorough search of the room reveals something interesting.
    """, [1,2]),
    Room("lab", """
    The door seals shut behind you and the decontamination spray washes over you.
    The lab doors slide open revealing a few drones diligently cooking up some Jazz.
    """, [3, 1]),
    Room("wrong", """
    Area's clear. Your AR display is telling you
    to head south west instead.
    """, [-3,-2])
]
menu = ["Move north", "Move south", "Move east", "Move west"]
def show_menu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    i+= 2
    for item in player.inventory:
        print(f"{i}. Use {item.name}")
        i += 1
def clear(lines):
    for l in range(lines):
        print()
playing = True
while playing:
    print(player)
    show_menu()
    for room in Rooms:
        if player.position == room.position:
            print(room.description)
            
    try:
        action = int(input("What is your choice?\n"))
    except ValueError:
        print("You must enter a valid entry.")
        action = None
    if action:
        if action == 1:
            player.move("up")
        elif action == 2:
            player.move("down")
        elif action == 3:
            player.move("left")
        elif action == 4:
            player.move("right")
        else:
            if action-4 <= len(player.inventory):
                player.inventory[action-5].use()
    
    
    # for enemy in enemies:
    #     if action != 0 and enemy.health > 0:
    #         emove = random.randint(1,4)
    #         if emove == 1:
    #             enemy.move("up")
    #         elif emove == 2:
    #             enemy.move("down")
    #         elif emove == 3:
    #             enemy.move("left")
    #         else:
    #             enemy.move("right")


    for enemy in enemies:
        if enemy.position == player.position:
            if enemy.health <= 0:
                print(f"You found the corpse of a {enemy.name}.")
            else:
                print(f"You ran into {enemy.name}")
                print(f"You attack! You deal {player.attack_power} damage.")
                player.attack(enemy)
                if enemy.health <= 0:
                    print(f"{enemy.name} has died.")
                else:
                    print(f"Enemy attacks! They deal {enemy.attack_power} damage.")
                    enemy.attack(player)
                    if player.health <= 0:
                        playing = False
                        print(Colors.FAIL + f"{player.name} has died. You lose." + Colors.ENDC)

    for item in items:
        if item.position == player.position:
            if item.name == "Paydata":
                playing = False
                print(Colors.OKGREEN + "You found the Paydata. You won the game." + Colors.ENDC)
            elif len(player.inventory) > 0:
                print(f"You have come across {item.name}, but your hands are full.")
            else:
                print(f"You have come across {item.name}")
                player.pickup_item(item)
    # clear(10)
    # time.sleep(.05)