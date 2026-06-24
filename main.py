from utils import get_coordinate
from grid import Grid
from robot import Robot
from direction import Direction

def command_process(cmd,robot):
    match(cmd):
            case "MOVE":
                robot.move()
                return True
            case "LEFT":
                robot.left()
                return True
            case "RIGHT":
                robot.right()
                return True
            case "REPORT":
                robot.report()
                return True
            case "EXIT":
                return False
            case _:
                print(f"Invalid command {cmd}")
                return True

def main():
    grid=Grid()
    obs=get_coordinate("Give number of obstacles: ",0,100)
    if obs>0:
        grid.create_obstacles(obs)
    print("There are four commands to make the robot move:\n MOVE,REPORT,LEFT,RIGHT \n The gridis 100x100 ")

    while True:
        x=get_coordinate("Give x coordinate of robot: ",grid.min_x,grid.max_x)
        y=get_coordinate("Give y coordinate of robot: ",grid.min_y,grid.max_y)
        if grid.position_valid(x,y):
            break
        print("Obstacle exists here, give new coordinates")
        
    while True:
        direction=input("Give direction of robot: ")
        if direction.isalpha() and direction.capitalize() in ["North","South","West","East"]:
            direction=direction.upper()
            break
        else:
            print("Please give valid direction")

    direction=Direction[direction]
    robot=Robot(x,y,direction,grid)
    
    mode=input("Give file name for file mode else leave blank: ")
    if mode=="":
        while True:
            cmd=input("Give a command: ")
            cmd=cmd.upper().strip()
            if not command_process(cmd,robot):
                break
            grid.display(robot)

    else:
        while True:
            try:
                with open("data/" + mode,"r") as file:
                    for cmd in file:
                        cmd=cmd.upper().strip()
                        if not command_process(cmd,robot):
                            break
                        grid.display(robot)
                    
            except FileNotFoundError:
                mode=input("please give valid file name: ")

            break

if __name__=="__main__":
    main()
