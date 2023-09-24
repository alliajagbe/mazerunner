from mazerunner import MazeState
from dfs import depth_first_search
from bfs import breadth_first_search
from bestfs import best_first_search
import time
import json
from analytics import get_memory_usage

def formatted_path_printing(path):
    for i in range(len(path)):
        if i == len(path) - 1:
            print(path[i])
        else:
            print(f"{path[i]} =>", end=" ")
    print()

with open("maze.json", "r") as f:
    maze_file = json.load(f)

def main():
    maze = maze_file["dfs_best_maze"]
    start_position = tuple(maze_file["dfs_start"])
    goal_position = tuple(maze_file["dfs_end"])

    initial_state = MazeState(maze, start_position)

    # taking an average of 10 runs
    time_dfs = []
    states_dfs = []
    memory_dfs = []

    time_bfs = []
    states_bfs = []
    memory_bfs = []

    time_bestfs = []
    states_bestfs = []
    memory_bestfs = []

    for i in range(10):
        initial_memory_usage = get_memory_usage()
        start_time_dfs = time.perf_counter()
        dfs_solution, no_of_states_explored_dfs = depth_first_search(initial_state, goal_position)
        end_time_dfs = time.perf_counter()
        end_memory_usage = get_memory_usage()
        time_dfs.append(end_time_dfs - start_time_dfs)
        states_dfs.append(no_of_states_explored_dfs)
        memory_dfs.append(end_memory_usage - initial_memory_usage)

        initial_memory_usage = get_memory_usage()
        start_time_bfs = time.perf_counter()
        bfs_solution, no_of_states_explored_bfs = breadth_first_search(initial_state, goal_position)
        end_time_bfs = time.perf_counter()
        end_memory_usage = get_memory_usage()
        time_bfs.append(end_time_bfs - start_time_bfs)
        states_bfs.append(no_of_states_explored_bfs)
        memory_bfs.append(end_memory_usage - initial_memory_usage)

        initial_memory_usage = get_memory_usage()
        start_time_bestfs = time.perf_counter()
        bestfs_solution, no_of_states_explored_bestfs = best_first_search(initial_state, goal_position)
        end_time_bestfs = time.perf_counter()
        end_memory_usage = get_memory_usage()
        time_bestfs.append(end_time_bestfs - start_time_bestfs)
        states_bestfs.append(no_of_states_explored_bestfs)
        memory_bestfs.append(end_memory_usage - initial_memory_usage)

    
    avg_time_dfs = sum(time_dfs)/len(time_dfs)
    print("Average time for DFS:", avg_time_dfs)
    avg_states_dfs = sum(states_dfs)/len(states_dfs)
    print("Average number of states explored with DFS:", avg_states_dfs)
    avg_memory_dfs = sum(memory_dfs)/len(memory_dfs)
    print("Average memory usage for DFS:", avg_memory_dfs, "bytes.")

    if dfs_solution:
        formatted_path_printing(dfs_solution)
    else:
        print("No path found with DFS")

    avg_time_bfs = sum(time_bfs)/len(time_bfs)
    print("Average time for BFS:", avg_time_bfs)
    avg_states_bfs = sum(states_bfs)/len(states_bfs)
    print("Average number of states explored with BFS:", avg_states_bfs)
    avg_memory_bfs = sum(memory_bfs)/len(memory_bfs)
    print("Average memory usage for BFS:", avg_memory_bfs, "bytes.")
    
    if bfs_solution:
        formatted_path_printing(bfs_solution)
    else:
        print("No path found with BFS")

    avg_time_bestfs = sum(time_bestfs)/len(time_bestfs)
    print("Average time for BestFS:", avg_time_bestfs)
    avg_states_bestfs = sum(states_bestfs)/len(states_bestfs)
    print("Average number of states explored with BestFS:", avg_states_bestfs)
    avg_memory_bestfs = sum(memory_bestfs)/len(memory_bestfs)
    print("Average memory usage for BestFS:", avg_memory_bestfs, "bytes.")
    
    if bestfs_solution:
        formatted_path_printing(bestfs_solution)
    else:
        print("No path found with BestFS")

if __name__ == "__main__":
    main()