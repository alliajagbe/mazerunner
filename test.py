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

    time_bfs = []
    states_bfs = []

    time_bestfs = []
    states_bestfs = []
    for i in range(10):
        start_time_dfs = time.perf_counter()
        dfs_solution, no_of_states_explored_dfs = depth_first_search(initial_state, goal_position)
        end_time_dfs = time.perf_counter()
        time_dfs.append(end_time_dfs - start_time_dfs)
        states_dfs.append(no_of_states_explored_dfs)

        start_time_bfs = time.perf_counter()
        bfs_solution, no_of_states_explored_bfs = breadth_first_search(initial_state, goal_position)
        end_time_bfs = time.perf_counter()
        time_bfs.append(end_time_bfs - start_time_bfs)
        states_bfs.append(no_of_states_explored_bfs)

        start_time_bestfs = time.perf_counter()
        bestfs_solution, no_of_states_explored_bestfs = best_first_search(initial_state, goal_position)
        end_time_bestfs = time.perf_counter()
        time_bestfs.append(end_time_bestfs - start_time_bestfs)
        states_bestfs.append(no_of_states_explored_bestfs)

    
    print("Average time for DFS:", sum(time_dfs)/len(time_dfs))
    print("Average number of states explored with DFS:", sum(states_dfs)/len(states_dfs))

    if dfs_solution:
        for i in range(len(dfs_solution)):
            print(dfs_solution[i], end=" ")
        print()
    else:
        print("No path found with DFS")

    print("Average time for BFS:", sum(time_bfs)/len(time_bfs))
    print("Average number of states explored with BFS:", sum(states_bfs)/len(states_bfs))
    
    if bfs_solution:
        for i in range(len(bfs_solution)):
            print(bfs_solution[i], end=" ")
        print()
    else:
        print("No path found with BFS")

    print("Average time for BestFS:", sum(time_bestfs)/len(time_bestfs))
    print("Average number of states explored with BestFS:", sum(states_bestfs)/len(states_bestfs))
    
    if bestfs_solution:
        for i in range(len(bestfs_solution)):
            print(bestfs_solution[i], end=" ")
        print()
    else:
        print("No path found with BestFS")





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