from unit import Unit, Player
from item import Item, Potion, Shield, BFS
import random

#name = input("What do you want the player to be named?\n")
name = "Hero"
player = Player(name, [5,5])



enemies = [
    Unit("Orc", [4,4], 10, 4),
    Unit("Goblin", [6,6], 5, 2),
    Unit("Kobold", [3,5], 2, 3),
]

items = [
    Item("Treasure", [2,3]),
    Potion("Health Potion", [5,4]),
    Shield("Shield", [5,6]),
    BFS("BF Sword",  [4,4])
]

menu = ["Move up", "Move Down", "Move Left", "Move Right"]

def show_menu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    i+= 2
    for item in player.inventory:
        print(f"{i}. Use {item.name}")
        i += 1

playing = True

while playing:
    print(player)
    show_menu()
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
    
    for enemy in enemies:
        if action != 0 and enemy.health > 0:
            emove = random.randint(1,4)
            if emove == 1:
                enemy.move("up")
            elif emove == 2:
                enemy.move("down")
            elif emove == 3:
                enemy.move("left")
            else:
                enemy.move("right")


    for enemy in enemies:
        if enemy.position == player.position:
            if enemy.health <= 0:
                print(f"You found the corpse of a {enemy.name}.")
            else:
                print(f"You ran into {enemy.name}")
                print("You attack!")
                player.attack(enemy)
                if enemy.health <= 0:
                    print(f"{enemy.name} has died.")
                else:
                    print("enemy attacks!")
                    enemy.attack(player)
                    if player.health <= 0:
                        playing = False
                        print(f"{player.name} has died. You lose.")

    for item in items:
        if item.position == player.position:
            if item.name == "Treasure":
                playing = False
                print("You found the Treasure. You won the game.")
            elif len(player.inventory) > 0:
                print(f"You have come across {item.name}, but your hands are full.")
            else:
                print(f"You have come across {item.name}")
                player.pickup_item(item)