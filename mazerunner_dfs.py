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
        0 <= new_row < len(current_state.maze) 
        and 0 <= new_col < len(current_state.maze[0])
        and current_state.maze[new_row][new_col] == 0
    ):
        new_position = (new_row, new_col)
        neighbours.append(MazeState(current_state.maze, new_position))

    return neighbours