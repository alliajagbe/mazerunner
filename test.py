from mazerunner import MazeState
from dfs import depth_first_search

def main():
    maze = [
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,1,1,1,0],
        [0,0,0,1,0]
    ]

    start_position = (0,0)
    goal_position = (4,4)

    initial_state = MazeState(maze, start_position)
    solution = depth_first_search(initial_state, goal_position)

    if solution:
        print("Found a path:", solution)
    else:
        print("No path found")

if __name__ == "__main__":
    main()