class MazeState:
    def __init__(self, maze, position):
        self.maze = maze
        self.position = position

def moveGen(current_state):
    neighbours = []

    row, col = current_state.position
    moves = [(0,1), (0,-1), (1,0), (-1,0)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc

    if (
        0 <= new_row < len(current_state.maze) # check if new_row is within the maze
        and 0 <= new_col < len(current_state.maze[0]) # check if new_col is within the maze
        and current_state.maze[new_row][new_col] == 0 # check if the new position is not a wall (0 for path, 1 for wall)
    ):
        new_position = (new_row, new_col)
        neighbours.append(MazeState(current_state.maze, new_position))

    return neighbours

def goalTest(current_state, goal_position):
    return current_state.position == goal_position