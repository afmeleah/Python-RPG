_worldmap = {}
starting_position = (0, 0)
 # grabs the text file that has the breakdown of the grid
def load_tiles():
    with open('resources/map.txt', 'r') as f: #with grabs the file and r states that it's for reading. as lets us use the file below
        row = f.readlines() #returns the lines in the file as a list
    x_max = len(row[0].split('\t')) #helps setup grid by splitting the .txt file string into a list
    for y in range(len(row)):
        col = row[y].split('\t')
        for x in range(x_max):
            tile_name = col[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position #sets Starting Room as the intro for the game
                starting_position = (x, y)
            _worldmap[(x, y)] = None if tile_name == '' else getattr(__import__('rooms'), tile_name)(x, y)
            #makes empty spots on txt file = None and then matches the names of other rooms with text file making my map

def tile_exists(x, y):
    return _worldmap.get((x, y))