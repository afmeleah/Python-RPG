_worldmap = {}
starting_position = (0, 0)
 
def load_tiles():
    with open('resources/map.txt', 'r') as f:
        row = f.readlines()
    x_max = len(row[0].split('\t'))
    for y in range(len(row)):
        col = row[y].split('\t')
        for x in range(x_max):
            tile_name = col[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _worldmap[(x, y)] = None if tile_name == '' else getattr(__import__('rooms'), tile_name)(x, y)

def tile_exists(x, y):
    return _worldmap.get((x, y))