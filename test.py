from mazerunner import MazeState
from dfs import depth_first_search
from bfs import breadth_first_search
from bestfs import best_first_search
import time

def main():
    maze_best_case = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]



    start_position = (0,0)
    goal_position = (9,4)

    initial_state = MazeState(maze_best_case, start_position)

    # taking an average of 10 runs
    time_dfs = []
    states_dfs = []
    for i in range(10):
        start_time = time.perf_counter()
        dfs_solution, no_of_states_explored = depth_first_search(initial_state, goal_position)
        end_time = time.perf_counter()
        time_dfs.append(end_time - start_time)
        states_dfs.append(no_of_states_explored)

    print("Average time for DFS:", sum(time_dfs)/len(time_dfs))
    print("Average number of states explored with DFS:", sum(states_dfs)/len(states_dfs))
    print("Path found with DFS:", dfs_solution)


    start_time = time.perf_counter()
    bfs_solution, no_of_states_explored = breadth_first_search(initial_state, goal_position)
    end_time = time.perf_counter()
    print("Number of states explored with BFS:", no_of_states_explored)
    print("BFS took", end_time - start_time, "seconds")

    start_time = time.perf_counter()
    bestfs_solution, no_of_states_explored = best_first_search(initial_state, goal_position)
    end_time = time.perf_counter()
    print("Number of states explored with BestFS:", no_of_states_explored)
    print("BestFS took", end_time - start_time, "seconds")


    if dfs_solution:
        print("Found a path with DFS:", dfs_solution)
    else:
        print("No path found with DFS")

    if bfs_solution:
        print("Found a path with BFS:", bfs_solution)
    else:
        print("No path found with BFS")

    if bestfs_solution:
        print("Found a path with BestFS:", bestfs_solution)
    else:
        print("No path found with BestFS")

if __name__ == "__main__":
    main()