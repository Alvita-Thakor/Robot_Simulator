from direction import Direction

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
