"""
Board tiles, usual game contains Wood, Brick, Hay, Stone
Used as a node in the graph traversal. 
Edges store the tile adjacent to them
Vertices store the three tiles that are next to it
"""
 
class Edge():
    def __init__(self,adjacent_tile):
        self._adjacent      = adjacent_tile
        self._built_on_by   = None

    def build(self,player,item='Road'):
        self._built_on_by = player

    def isBuiltOn(self):
        return self._built_on_by

    def getAdjacent(self):
        return self._adjacent

class Vertice():
    def __init__(self,adacent_tile):
        self.adjacent_tiles = []
        self.MAX_VERTICES   =  3   
        self._is_built_on   = None
        self._item_built    = None
     
    def addTile(self,tile):
        if len(self.adjacent_tiles) < self.MAX_VERTICES:
            self.adjacent_tiles.append(tile)
            return True
        return False

    def getConnectedTiles(self):
        return self.adjacent_tiles
    
    def isBuiltOn(self):
        return self._is_built_on
    
    def build(self,player,item):
        if item == 'Settlement':
            self._item_built = 'Settlement'
        else:
            self._item_built = 'Church'

class Tile():   
    def __init__(self):
        self._vertices   = []
        self._edges      = []

    