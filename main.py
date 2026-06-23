from utils import get_coordinate
from grid import Grid
from robot import Robot
from direction import Direction

def main():
    grid=Grid()
    obs=get_coordinate("Give number of obstacles: ",1,100)
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
    while True:
        cmd=input("Give a command: ")
        cmd=cmd.upper().strip()
        match(cmd):
            case "MOVE":
                robot.move()
            case "LEFT":
                robot.left()
            case "RIGHT":
                robot.right()
            case "REPORT":
                robot.report()
            case "EXIT":
                break
            case _:
                print("Invalid command")
        grid.display(robot)

if __name__=="__main__":
    main()
