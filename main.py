from utils import get_coordinate,clear_screen
from grid import Grid
from robot import Robot
from direction import Direction
from pygame_ui import run_pygame_ui, place_obstacles_ui

def main():
    grid=Grid()
    o_mode=input("name of obstacle file name else for manual leave blank: ")
    if o_mode=="":
        place_obstacles_ui(grid)

    else:
        while True:
            try:
                with open("data/" + o_mode,"r") as file:
                    grid.load_obstacles(file)
                    
            except FileNotFoundError:
                o_mode=input("please give valid file name: ")

            break

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

    run_pygame_ui(grid, robot)

if __name__=="__main__":
    main()