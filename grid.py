from utils import get_coordinate

class Grid():
    def __init__(self,max_x=5,max_y=5,min_x=0,min_y=0):
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
        for row in range(self.max_y,self.min_y-1,-1):
            drow=""
            for column in range(self.min_x,self.max_x+1,1):
                if (column,row) in self.obstacles:
                    drow=drow+"X"
                elif column==robot.x and row==robot.y:
                    drow=drow+"R"
                else:
                    drow=drow+"."
            print(drow)