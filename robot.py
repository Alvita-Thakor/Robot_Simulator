from direction import Direction
from collections import deque
import heapq

class Robot():
    def __init__(self,x,y,direction,grid):
        self.x=x
        self.y=y
        self.direction=direction
        self.grid=grid
        self.status=""
    
    def move(self):
        new_x= self.x + self.direction.dx
        new_y= self.y + self.direction.dy
        if self.grid.position_valid(new_x,new_y):
            self.x=new_x
            self.y=new_y
        else:
            print("Robot cannot move here")

    def left(self):
        self.direction=self.direction.turn(-1)

    def right(self):
        self.direction=self.direction.turn(1)
    
    def report(self):
        print(f"robot is at ({self.x},{self.y}) facing {self.direction}")

    def go_to(self,x,y,algo):
        if not self.grid.position_valid(x,y):
            self.status= "Destination invalid"
            return None
        
        if (self.x,self.y)==(x,y):
            self.status="Already at Destination"
            return

        if algo=="BFS":
            parent=self.find_path(x,y)
        else:
            parent=self.a_star_path(x,y)
        msg,path=self.reconstruct_path(parent,x,y)
        self.status=msg

        if msg!= "Reached Destination":
            return None
        
        return self.follow_path(path)

    def face_direction(self, req_dir):

        directions = [
            Direction.NORTH,
            Direction.EAST,
            Direction.SOUTH,
            Direction.WEST
        ]

        current = directions.index(self.direction)
        target = directions.index(req_dir)

        clockwise = (target - current) % 4
        anticlockwise = (current - target) % 4

        if clockwise <= anticlockwise:
            for _ in range(clockwise):
                self.right()
        else:
            for _ in range(anticlockwise):
                self.left()

    def find_path(self,x,y):
        explore=deque()
        explore.append((self.x,self.y))
        visited=set()
        visited.add((self.x,self.y))
        parent_dict={}
        ways=[(1,0),(-1,0),(0,1),(0,-1)]
        while len(explore)!=0:
            front=explore.popleft()
            if front==(x,y):
                break
            else:
                for way in ways:
                    if (self.grid.position_valid(front[0]+way[0],front[1]+way[1])) and (front[0]+way[0],front[1]+way[1]) not in visited:
                        visited.add((front[0]+way[0],front[1]+way[1]))
                        explore.append((front[0]+way[0],front[1]+way[1]))
                        parent_dict[(front[0]+way[0],front[1]+way[1])]=(front[0],front[1])
        return parent_dict

    def reconstruct_path(self,parent_dict,x,y):
        path=[]
        child=(x,y)
        path.append(child)
        if child in parent_dict:
            while True:
                if child==(self.x,self.y):
                    path.reverse()
                    return "Reached Destination",path
                parent=parent_dict[child]
                path.append(parent)
                child=parent
        else:
            return "No path valid",path

    def follow_path(self,path):
        find_direction={(0,1):Direction.NORTH , (1,0):Direction.EAST,(0,-1):Direction.SOUTH,(-1,0):Direction.WEST}
        for i in range(len(path)-1):
            current=path[i]
            nxt=path[i+1]
            dx=nxt[0] - current[0]
            dy=nxt[1] - current[1]
            req_dir=find_direction[(dx,dy)]
            self.face_direction(req_dir)
            self.move()
            yield

    def a_star_path(self, x, y):

        priority_queue = []
        parent_dict = {}
        g_cost = {}
        start = (self.x, self.y)
        g_cost[start] = 0

        h = abs(x - self.x) + abs(y - self.y)
        heapq.heappush(priority_queue, (h, 0, start))
        ways = [(1,0), (-1,0), (0,1), (0,-1)]

        while priority_queue:
            f, g, current = heapq.heappop(priority_queue)
            if g != g_cost[current]:
                continue
            if current == (x, y):
                return parent_dict
            
            for dx, dy in ways:
                neighbour = (current[0] + dx,current[1] + dy)
                if not self.grid.position_valid(neighbour[0],neighbour[1]):
                    continue
                new_g = g + 1
                if neighbour not in g_cost or new_g < g_cost[neighbour]:
                    g_cost[neighbour] = new_g
                    parent_dict[neighbour] = current
                    h = abs(x - neighbour[0]) + abs(y - neighbour[1])
                    new_f = new_g + h
                    heapq.heappush(priority_queue,(new_f, new_g, neighbour))

        return {}