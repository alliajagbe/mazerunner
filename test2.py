from mazerunner import MazeState
from dfs import depth_first_search
from bfs import breadth_first_search
from bestfs import best_first_search
import time

def main():
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]




    start_position = (0,0)
    goal_position = (9,4)

    initial_state = MazeState(maze, start_position)
    start_time = time.time()
    dfs_solution = depth_first_search(initial_state, goal_position)
    end_time = time.time()

    print("DFS took", end_time - start_time, "seconds")

    start_time = time.time()
    bfs_solution = breadth_first_search(initial_state, goal_position)
    end_time = time.time()

    print("BFS took", end_time - start_time, "seconds")

    if dfs_solution:
        print("Found a path with DFS:", dfs_solution)
    else:
        print("No path found with DFS")

    if bfs_solution:
        print("Found a path with BFS:", bfs_solution)
    else:
        print("No path found with BFS")

if __name__ == "__main__":
    main()
    


