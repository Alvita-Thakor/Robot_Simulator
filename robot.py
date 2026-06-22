class Robot():
    def __init__(self,x,y,direction,grid):
        self.x=x
        self.y=y
        self.direction=direction
        self.grid=grid
    
    def move(self):
        direction=self.direction
        match(direction):
            case "North":
                new_x=self.x
                new_y=self.y+1
            case "South":
                    new_x=self.x
                    new_y=self.y-1
            case "West":
                    new_x=self.x-1
                    new_y=self.y
            case "East":
                    new_x=self.x+1
                    new_y=self.y
        if self.grid.position_valid(new_x,new_y):
            self.x=new_x
            self.y=new_y
        else:
            print("Robot cannot move here")
    
    def left(self):
        match(self.direction):
            case "North":
                self.direction="West"
            case "South":
                self.direction="East"
            case "West":
                self.direction="South"
            case "East":
                self.direction="North"
    
    def right(self):
        direction=self.direction
        match(direction):
            case "North":
                self.direction="East"
            case "South":
                self.direction="West"
            case "West":
                self.direction="North"
            case "East":
                self.direction="South"
    
    def report(self):
        print(f"robot is at ({self.x},{self.y}) facing {self.direction}")
