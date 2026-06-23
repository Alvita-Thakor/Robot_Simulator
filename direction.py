from enum import Enum

class Direction(Enum):
    NORTH = (0,1,"^")
    EAST = (1,0,">")
    WEST = (-1,0,"<")
    SOUTH = (0,-1,"v")

    def __init__(self,x,y,symbol):
        self.dx=x
        self.dy=y
        self.symbol=symbol

    def turn(self,step):
        directions=[Direction.NORTH,Direction.EAST,Direction.SOUTH,Direction.WEST]
        i=directions.index(self)
        return directions[(i+step)%4]
