import pygame
from direction import Direction

def place_obstacles_ui(grid):
    pygame.init()

    GRID_SIZE = grid.max_x - grid.min_x + 1
    CELL_SIZE = 40
    LINE_WIDTH = 2
    WINDOW_SIZE = GRID_SIZE * CELL_SIZE

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Click to place obstacles - press ENTER when done")
    clock = pygame.time.Clock()

    placing = True
    while placing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                placing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_x = mouse_x // CELL_SIZE
                cell_y = grid.max_y - (mouse_y // CELL_SIZE)
                if grid.min_x <= cell_x <= grid.max_x and grid.min_y <= cell_y <= grid.max_y:
                    if (cell_x, cell_y) in grid.obstacles:
                        grid.obstacles.remove((cell_x, cell_y))
                    else:
                        grid.obstacles.add((cell_x, cell_y))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    placing = False

        screen.fill("blue")

        for i in range(GRID_SIZE + 1):
            pygame.draw.line(screen, "black", (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH)
        for j in range(GRID_SIZE + 1):
            pygame.draw.line(screen, "black", (0, j * CELL_SIZE), (WINDOW_SIZE, j * CELL_SIZE), LINE_WIDTH)

        for obstacle in grid.obstacles:
            left = obstacle[0] * CELL_SIZE
            top = (grid.max_y - obstacle[1]) * CELL_SIZE
            pygame.draw.rect(screen, (170, 170, 10), (left, top, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        clock.tick(60)

def run_pygame_ui(grid, robot):
    pygame.init()

    GRID_SIZE = grid.max_x - grid.min_x + 1
    CELL_SIZE = 40
    LINE_WIDTH = 2
    WINDOW_SIZE = GRID_SIZE * CELL_SIZE

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Robot Simulator")
    clock = pygame.time.Clock()

    destination = None
    path_animation = None
    animation_timer = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = mouse_x // CELL_SIZE
                grid_y = grid.max_y - (mouse_y // CELL_SIZE)
                if grid.position_valid(grid_x, grid_y):
                    destination = (grid_x, grid_y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    robot.move()
                elif event.key == pygame.K_LEFT:
                    robot.left()
                elif event.key == pygame.K_RIGHT:
                    robot.right()
                elif event.key == pygame.K_b and destination is not None:
                    path_animation = robot.go_to(destination[0], destination[1], "BFS")
                elif event.key == pygame.K_n and destination is not None:
                    path_animation = robot.go_to(destination[0], destination[1], "A_STAR")

        if path_animation is not None:
            animation_timer += 1
            if animation_timer >= 10:
                animation_timer = 0
                try:
                    next(path_animation)
                except StopIteration:
                    path_animation = None
                    destination = None

        screen.fill("blue")

        for i in range(GRID_SIZE + 1):
            pygame.draw.line(screen, "black",(i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH,)

        for j in range(GRID_SIZE + 1):
            pygame.draw.line(screen, "black",(0, j * CELL_SIZE), (WINDOW_SIZE, j * CELL_SIZE), LINE_WIDTH,)

        for obstacle in grid.obstacles:
            left = obstacle[0] * CELL_SIZE
            top = (grid.max_y - obstacle[1]) * CELL_SIZE
            pygame.draw.rect(screen, (170, 170, 10), (left, top, CELL_SIZE, CELL_SIZE))

        if destination is not None:
            dest_left = destination[0] * CELL_SIZE
            dest_top = (grid.max_y - destination[1]) * CELL_SIZE
            pygame.draw.rect(screen, (0, 200, 0), (dest_left, dest_top, CELL_SIZE, CELL_SIZE))

        pixel_x = robot.x * CELL_SIZE + CELL_SIZE // 2
        pixel_y = (grid.max_y - robot.y) * CELL_SIZE + CELL_SIZE // 2

        if robot.direction == Direction.NORTH:
            points = [(pixel_x, pixel_y - 15), (pixel_x - 15, pixel_y + 15), (pixel_x + 15, pixel_y + 15)]
        elif robot.direction == Direction.SOUTH:
            points = [(pixel_x, pixel_y + 15), (pixel_x - 15, pixel_y - 15), (pixel_x + 15, pixel_y - 15)]
        elif robot.direction == Direction.EAST:
            points = [(pixel_x + 15, pixel_y), (pixel_x - 15, pixel_y - 15), (pixel_x - 15, pixel_y + 15)]
        elif robot.direction == Direction.WEST:
            points = [(pixel_x - 15, pixel_y), (pixel_x + 15, pixel_y - 15), (pixel_x + 15, pixel_y + 15)]

        pygame.draw.polygon(screen, (255, 255, 255), points)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()