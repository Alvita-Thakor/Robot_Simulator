from utils import get_coordinate

class Grid():
    def __init__(self,max_x=10,max_y=10,min_x=0,min_y=0):
        self.max_x=max_x
        self.max_y=max_y
        self.min_x=min_x
        self.min_y=min_y
        self.obstacles=set()

    def position_valid(self,x,y):
        if self.min_x<=x<=self.max_x and self.min_y<=y<=self.max_y:
            if (x,y) not in self.obstacles:
                return True
        return False
    
    def create_obstacles(self,n):
        for i in range(n):
            print(f"Give coordinates for obstacle {i}")

            x=get_coordinate("x= ",self.min_x,self.max_x)
            y=get_coordinate("y= ",self.min_y,self.max_y)
            self.obstacles.add((x,y))

    def display(self,robot):
        dash="-"*((self.max_x+1)*2 +1)
        width =len(str(self.max_y))

        print(" "*(width+2) + "+" + dash + "+")

        for row in range(self.max_y,self.min_y-1,-1):
            drow=f" {row:{width}} |"

            for column in range(self.min_x,self.max_x+1,1):
                if (column,row) in self.obstacles:
                    drow+=" ■"
                elif column==robot.x and row==robot.y:
                    drow+=f" {robot.direction.symbol}"
                else:
                    drow+=" ."

            drow+=" |"
            print(drow)

        dash="-"*((self.max_x+1)*2 +1)
        print(" "*(width+2) + "+" + dash + "+")
        drow="  "

        for column in range(self.min_x,self.max_x+1,1):
            drow=drow+ f" {column}"
        print(drow)

    def load_obstacles(self,file):
        for obs in file:
            try:
                x,y=obs.split(",")
                x=int(x)
                y=int(y)
                if self.position_valid(x,y):
                    self.obstacles.add((x,y))
            except ValueError:
                print("Invalid obstacle")
