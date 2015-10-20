"""


!!!DEPRECATED FOR THE MOST PART!!!


"""


"""
Standard imports
"""
from queue import PriorityQueue
from enum import Enum
from math import sqrt

"""
Empire of code imports
"""
from battle import commander
from battle import ROLE


"""
Constants
"""

    
    
"""
Definitions
"""

class Map(object):
    def __init__(self, enemy_items, diagonal_movement=True):
        self.diags = diagonal_movement
        self.width = 50
        self.height = 50
        self._data = [[TILE.EMPTY for y in range(self.height)]for x in range(self.width)]
        self.populate_map(enemy_items)
        self.evil_callback = 0
        
    def populate_map(self, enemy_items):
        valid = lambda w:  any([isinstance(w, int), isinstance(w, float)]) 
        for entity in enemy_items:
            size = entity.get('size', 0)
            x,y = entity['coordinates']
            role = entity['role']
            if x+size>=self.width or y+size>=self.height:
                self.extend_map((x+size,y+size))
            if not valid(x) or not valid(y):
                self.evil_callback+=1
                continue
            
            x = int(x)
            y = int(y)
            # for x0, y0 in self.get_rect_from_center((x,y), size):
            #     self._data[x0][y0] = MappedRoles.get(role, TILE.UNKNOWN)

    def extend_map(self,point):
        w,h = point
        if h>self.height:
            for y in self._data:
                y.extend([TILE.EMPTY for _ in range(h-self.height)])
            self.height = h        
        if w>self.width:
            for _ in range(w-self.width):
                self._data.append([TILE.EMPTY for _ in range(self.height)])
            self.width = w

            
    def find_path(self, start, end, size=1, heuristic=None): 
        """
        A*
        """
        if not heuristic:
            heuristic = lambda x,y:abs(x-end[0])+abs(y-end[1])

        dest = set(self.get_rect_from_center(end, size))
        start = tuple(start)
        fringe = PriorityQueue()
        fringe.put(start, 0)
        total_cost = {start:0}

        origin = {start:None}
        while not fringe.empty():
            current = fringe.get()
            if current in dest:
                break
            cost = total_cost[current]+1
            nodes = self.get_adjacent(current[0], current[1])
            for node in nodes:
                x,y = node
                node_type = self._data[x][y]
                if (node_type == TILE.EMPTY or node in dest) and (node not in total_cost or cost < total_cost[node]):
                    total_cost[node] = cost 
                    origin[node] = current
                    fringe.put(node, cost+heuristic(x, y))
        else:     
            return []

        path = []
        n = current
        while n is not None:
            path.append(n)
            n = origin[n]
        path.reverse()
        print(path)
        return path

    def update(self, info):
        self.init_map(info)
        
    def get_bounds(self, x0,y0,x1,y1):
        xmin, xmax = (max(0, x0), min(self.width, x1))
        ymin, ymax = (max(0, y0), min(self.height, y1))
        return(xmin,ymin, xmax,ymax)
    
    def get_rect_from_center(self, pos, size): ## dist 0: single-point
        if size < 2:                        ## and single-tile bulidings are 
            return [pos]                    ## handled in the same manner as of now
            
        even = size %2 == 0
        dist = int(size/2)
        px,py = pos
        if even: ##x/ymax will be exclusive in the for loop!
            xmin, ymin, xmax, ymax = self.get_bounds(px-dist+1, py-dist+1, px+dist+1, py+dist+1)            
        else:
            xmin, ymin, xmax, ymax = self.get_bounds(px-dist, py-dist, px+dist+1, py+dist+1)            
        # print('for {} dist:{} we get a rect ({})'.format(pos, size, (xmin, ymin, xmax-1, ymax-1)))
        cells = []
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                cells.append((x,y))
        return cells
        
    def get_rect(self, top_left, size):
        cells = []
        x0,y0 = top_left
        xmin,ymin, xmax,ymax = self.get_bounds(x0,y0,x0+size, y0+size)
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                cells.append((x,y))
        return cells

    def get_adjacent(self, x0,y0, diag = True):
        """
        Returns a list of tuples of coords adjacent to (x0,y0)
            7 8 9
            4 @ 6
            1 2 3   
        """
        res =[]
        if x0>0:
            res.append((x0-1,y0))       # 4
            if y0>0 and diag:
              res.append((x0-1,y0-1))   # 7
            if y0 < self.height-1 and diag:
              res.append((x0-1,y0+1))   # 1

        if y0>0:
            res.append((x0,y0-1))       # 8

        if x0 < self.width-1:
            res.append((x0+1,y0))       # 6
            if y0 < self.height-1 and diag:
                res.append((x0+1,y0+1)) # 3
        if y0>0 and diag:
            res.append((x0+1,y0-1))     # 9
    
        if y0 < self.height-1:
            res.append((x0,y0+1))       # 2
        
        return [tuple(x) for x in res]
          
    # def get_info(self):
    #     for x in range(self.width):
    #         for y in range(self.height):
    #             a = self._data[x][y]
    #             if a != TILE.EMPTY :
    #                 print("[{},{}],{}".format(x,y,a)) 
                    
    def __getitem__(self, index):
        return self._data[index]                    


class Brain(object):
    """
    (0,0) is located in the northen corner of the map.
    X N->SE
    Y N-SW
    """
    def __init__(self,client, init_terrain=True):
        self.me = client
        self.update()
        if init_terrain:
            self.terrain = Map(self.me.ask_enemy_items())
    
    def update(self):
        info = self.me.ask_my_info()
        self.fire_range = info['firing_range']
        self.pos = info['coordinates']
        self.size = info.get('size', 0)
        
    def goto(self, pos, size = 1):
        return self.terrain.find_path(self.pos, pos, size)

def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    
def dist(p1, p2):
    x,y = p1
    ox,oy = p2
    return sqrt((ox-x)*(ox-x) + (oy-y)*(oy-y))
    
def search_role(array,role):
    for e in array:
        if e['role'] == role:
            return True
    return False

def search_and_destroy(data=None, *args, **kawargs):
    brain.update()
    
    center = unit.ask_center()
    cpos = center['coordinates']
    assert brain.terrain[cpos[0]][cpos[1]] == TILE.CENTER, 'CENTER NOT FOUND'
    mypos = unit.ask_my_info()['coordinates']
    # if center["hit_points"]>0:
    #     if dist(cpos, mypos) < brain.fire_range:
    #         print('attacking center')
    #         unit.attack_item(center['id'])
    #         unit.subscribe_the_item_is_dead(center['id'], search_and_destroy)
    #     else:
    #         print('walking')
    #         # p = path.pop()
    #         # print(p)
    #         # unit.move_to_point(p)
            
    #         unit.move_to_point(midpoint(cpos, mypos))
            
    #         unit.subscribe_im_idle(search_and_destroy)
    # else:
    #     print('attacking other')
    #     eid=  unit.ask_nearest_enemy()['id']
    #     unit.attack_item(eid)
    #     unit.subscribe_the_item_is_dead(eid, search_and_destroy)
    unit.move_to_point((mypos+(0,brain.terrain.evil_callback)))

#######
TILE = Enum('TileContent', 'EMPTY UNIT ROCK BUILDING TURRET CENTER UNKNOWN')
STATE = Enum("State", "ATTACKING FLEEING MOVING")
MappedRoles = {
    ROLE.UNIT:TILE.UNIT,
    ROLE.BUILDING:TILE.BUILDING,
    ROLE.OBSTACLE:TILE.ROCK,
    ROLE.TOWER:TILE.TURRET,
    ROLE.CENTER:TILE.CENTER
    }
    
# if __name__ == "run":
unit = commander.Client()
brain = Brain(unit, True)
cx,cy=unit.ask_center()['coordinates']
# path = brain.goto((cx,cy),4)
# path.reverse()

# brain.terrain.get_rect_from_center((2,2),0)
# brain.terrain.get_rect_from_center((2,2),1)
# brain.terrain.get_rect_from_center((2,2),-1)
# brain.terrain.get_rect_from_center((2,2),2)
# brain.terrain.get_rect_from_center((5,5),3)

search_and_destroy()