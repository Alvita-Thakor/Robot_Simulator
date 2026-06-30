from direction import Direction
from collections import deque
from grid import Grid

class Robot():
    def __init__(self,x,y,direction,grid):
        self.x=x
        self.y=y
        self.direction=direction
        self.grid=grid
    
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

    def go_to(self,x,y):
        if not self.grid.position_valid(x,y):
            return "Destination invalid"
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

        path=[]
        child=(x,y)
        path.append(child)
        if child in parent_dict:
            while True:
                if child==(self.x,self.y):
                    break
                parent=parent_dict[child]
                path.append(parent)
                child=parent
        else:
            return "No path valid"

        path.reverse()

        find_direction={(0,1):Direction.NORTH , (1,0):Direction.EAST,(0,-1):Direction.SOUTH,(-1,0):Direction.WEST}
        for i in range(len(path)-1):
            current=path[i]
            nxt=path[i+1]
            dx=nxt[0] - current[0]
            dy=nxt[1] - current[1]
            req_dir=find_direction[(dx,dy)]
            self.face_direction(req_dir)
            self.move()

        return "Reached destination"

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