import random
def generate_random_maze(rows, cols, num_walls):
    if rows <= 2 or cols <= 2 or num_walls > rows*cols:
        raise Exception(f"Please ensure that rows > 2, cols > 2 and num_walls < {rows*cols}")
    
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    wall_count = 0
    while wall_count < num_walls:
        row = random.randint(1, rows - 2)
        col = random.randint(1, cols - 2)

        if maze[row][col] == 0:
            maze[row][col] = 1
            wall_count += 1

    return maze