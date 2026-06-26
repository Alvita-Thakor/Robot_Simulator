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

    def display(self, robot, cmd_history):

        print("=" * 70)
        print(f"{'ROBOT SIMULATOR':^70}")
        print("=" * 70)
        print()

        dash = "-" * ((self.max_x + 1) * 2 + 1)
        width = len(str(self.max_y))

        status = [
            "SYSTEM STATUS",
            "------------",
            f"Position : ({robot.x}, {robot.y})",
            f"Facing   : {robot.direction.name:<5} {robot.direction.symbol}",
            f"Obstacles: {len(self.obstacles)}",
            "",
            "RECENT COMMANDS",
            "---------------"
        ]

        for i, cmd in enumerate(reversed(cmd_history)):
            prefix = ">" if i == 0 else " "
            status.append(f"{prefix} {cmd}")

        total_rows = self.max_y - self.min_y + 1

        while len(status) < total_rows:
            status.append("")

        print()

        print(
            " " * (width + 1)
            + "+"
            + dash
            + "+"
            + "   "
            + "+"
            + "-" * 24
            + "+"
        )

        for i, row in enumerate(range(self.max_y, self.min_y - 1, -1)):

            grid_row = f"{row:>{width}} |"

            for column in range(self.min_x, self.max_x + 1):

                if (column, row) in self.obstacles:
                    grid_row += " ■"

                elif column == robot.x and row == robot.y:
                    grid_row += f" {robot.direction.symbol}"

                else:
                    grid_row += " ."

            grid_row += " |"

            status_text = status[i] if i < len(status) else ""

            print(f"{grid_row}   | {status_text:<22}|")

        print(
            " " * (width + 1)
            + "+"
            + dash
            + "+"
            + "   "
            + "+"
            + "-" * 24
            + "+"
        )

        axis = " " * (width + 2)

        for column in range(self.min_x, self.max_x + 1):
            axis += f" {column}"

        print(axis)  

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
