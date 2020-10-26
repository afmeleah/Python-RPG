import worldmap, colors
from player import Player
from subprocess import call 
import os 

def clear(): 
    call('clear' if os.name =='posix' else 'cls') 


def play():
    worldmap.load_tiles()
    player = Player()
    room = worldmap.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = worldmap.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("What would you like to do?\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            clear()
            for action in available_actions:
                if action_input == action.hotkey: #Makes it so that the player will only move on if they enter one of their available actions
                    player.do_action(action, **action.kwargs)
                    break
        

play()
