from utils import get_coordinate,clear_screen
from grid import Grid
from robot import Robot
from direction import Direction
import time

def command_process(cmd,robot):
    parts=cmd.split()
    if len(parts)==1:
        match(parts[0]):
                case "MOVE":
                    robot.move()
                    return True,None
                case "LEFT":
                    robot.left()
                    return True,None
                case "RIGHT":
                    robot.right()
                    return True,None
                case "REPORT":
                    robot.report()
                    return True,None
                case "EXIT":
                    return False,None
                case _:
                    robot.status=f"Invalid command {cmd}"
                    return True,None
    
    elif len(parts)==3:
        if parts[0] in ["BFS","A_STAR"]:
            animate=robot.go_to(int(parts[1]),int(parts[2]),parts[0])
            return True,animate
        else:
            robot.status=f"Invalid command {cmd}"
            return True,None
        
    else:
        robot.status=f"Invalid command {cmd}"
        return True,None

def main():
    grid=Grid()
    o_mode=input("name of obstacle file name else for manual leave blank: ")
    if o_mode=="":
        obs=get_coordinate("Give number of obstacles: ",0,100)
        if obs>0:
            grid.create_obstacles(obs)

    else:
        while True:
            try:
                with open("data/" + o_mode,"r") as file:
                    grid.load_obstacles(file)
                    
            except FileNotFoundError:
                o_mode=input("please give valid file name: ")

            break

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
    cmd_history=[]
    clear_screen()
    grid.display(robot, cmd_history,"Let's get started!")

    if mode=="":
        while True:
            print()
            print("=" * 70)
            cmd = input("Command > ")

            cmd=cmd.upper().strip()
            cmd_history.append(cmd)

            if len(cmd_history) > 5:
                cmd_history.pop(0)

            running,animate=command_process(cmd,robot)
            if not running:
                break

            if animate is not None:
                for _ in animate:
                    clear_screen()
                    grid.display(robot, cmd_history, robot.status)
                    time.sleep(0.2)
            clear_screen()
            grid.display(robot,cmd_history,robot.status)

    else:
        while True:
            try:
                with open("data/" + mode,"r") as file:
                    for cmd in file:
                        cmd=cmd.upper().strip()
                        
                        cmd_history.append(cmd)

                        if len(cmd_history) > 5:
                            cmd_history.pop(0)

                        running,animate=command_process(cmd,robot)
                        if not running:
                            break

                        if animate is not None:
                            for _ in animate:
                                clear_screen()
                                grid.display(robot, cmd_history, robot.status)
                                time.sleep(0.2)
                        clear_screen()
                        grid.display(robot,cmd_history,robot.status)
                    
            except FileNotFoundError:
                mode=input("please give valid file name: ")

            break

if __name__=="__main__":
    main()
