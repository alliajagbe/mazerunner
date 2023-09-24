from mazerunner import MazeState
from dfs import depth_first_search
from bfs import breadth_first_search
from bestfs import best_first_search
from mazegenerator import generate_random_maze
import time
import json
import tracemalloc\


def formatted_path_printing(path):
    for i in range(len(path)):
        if i == len(path) - 1:
            print(path[i])
        else:
            print(f"{path[i]} =>", end=" ")
    print()

with open("maze.json", "r") as f:
    maze_file = json.load(f)


def input_fetcher():
    maze_selector = input("Enter maze number (1 or 2 or 3 for the mazes in the config file. Enter 4 for a random maze) :")
    if maze_selector == "1":
        maze = maze_file["maze1"]
        start_position = tuple(maze_file["start1"])
        goal_position = tuple(maze_file["end1"])
    elif maze_selector == "2":
        maze = maze_file["maze2"]
        start_position = tuple(maze_file["start2"])
        goal_position = tuple(maze_file["end2"])
    elif maze_selector == "3":
        maze = maze_file["maze3"]
        start_position = tuple(maze_file["start3"])
        goal_position = tuple(maze_file["end3"])
    elif maze_selector == "4":
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        num_walls = int(input("Enter number of walls: "))
        maze = generate_random_maze(rows, cols, num_walls)
        start_position = tuple(input("Enter start position (row, col): ").split(","))
        if maze[int(start_position[0])][int(start_position[1])] == 1:
            print("Invalid start position. Please try again.")
            start_position = tuple(input("Enter start position (row, col): ").split(","))
        goal_position = tuple(input("Enter goal position (row, col): ").split(","))
        if maze[int(goal_position[0])][int(goal_position[1])] == 1:
            print("Invalid goal position. Please try again.")
            goal_position = tuple(input("Enter goal position (row, col): ").split(","))
    else:
        print("Invalid input. Please try again.")
    
    return maze, start_position, goal_position

def main():
    maze, start_position, goal_position = input_fetcher()

    initial_state = MazeState(maze, start_position)

    # taking an average of 10 runs
    time_dfs = []
    states_dfs = []
    memory_dfs = []
    dfs_path_lengths = []

    time_bfs = []
    states_bfs = []
    memory_bfs = []
    bfs_path_lengths = []

    time_bestfs = []
    states_bestfs = []
    memory_bestfs = []
    bestfs_path_lengths = []

    for i in range(10):
        # initial_memory_usage = get_memory_usage()
        tracemalloc.start()
        start_time_dfs = time.perf_counter()
        dfs_solution, no_of_states_explored_dfs, dfs_path_length = depth_first_search(initial_state, goal_position)
        end_time_dfs = time.perf_counter()
        # end_memory_usage = get_memory_usage()
        time_dfs.append(end_time_dfs - start_time_dfs)
        states_dfs.append(no_of_states_explored_dfs)
        memory_dfs.append(tracemalloc.get_traced_memory()[0])
        dfs_path_lengths.append(dfs_path_length)
        tracemalloc.stop()

        # initial_memory_usage = get_memory_usage()
        tracemalloc.start()
        start_time_bfs = time.perf_counter()
        bfs_solution, no_of_states_explored_bfs, bfs_path_length = breadth_first_search(initial_state, goal_position)
        end_time_bfs = time.perf_counter()
        # end_memory_usage = get_memory_usage()
        time_bfs.append(end_time_bfs - start_time_bfs)
        states_bfs.append(no_of_states_explored_bfs)
        memory_bfs.append(tracemalloc.get_traced_memory()[0])
        bfs_path_lengths.append(bfs_path_length)
        tracemalloc.stop()

        #initial_memory_usage = get_memory_usage()
        tracemalloc.start()
        start_time_bestfs = time.perf_counter()
        bestfs_solution, no_of_states_explored_bestfs, bestfs_path_length = best_first_search(initial_state, goal_position)
        end_time_bestfs = time.perf_counter()
        # end_memory_usage = get_memory_usage()
        time_bestfs.append(end_time_bestfs - start_time_bestfs)
        states_bestfs.append(no_of_states_explored_bestfs)
        memory_bestfs.append(tracemalloc.get_traced_memory()[0])
        bestfs_path_lengths.append(bestfs_path_length)
        tracemalloc.stop()

    
    avg_time_dfs = sum(time_dfs)/len(time_dfs)
    print("Average time for DFS:", avg_time_dfs)
    avg_states_dfs = sum(states_dfs)/len(states_dfs)
    print("Average number of states explored with DFS:", avg_states_dfs)
    avg_memory_dfs = sum(memory_dfs)/len(memory_dfs)
    print("Average memory usage for DFS:", avg_memory_dfs, "bytes.")
    avg_path_length_dfs = sum(dfs_path_lengths)/len(dfs_path_lengths)
    print("Average path length for DFS:", avg_path_length_dfs)

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
    avg_path_length_bfs = sum(bfs_path_lengths)/len(bfs_path_lengths)
    print("Average path length for BFS:", avg_path_length_bfs)
    
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
    avg_path_length_bestfs = sum(bestfs_path_lengths)/len(bestfs_path_lengths)
    print("Average path length for BestFS:", avg_path_length_bestfs)
    
    if bestfs_solution:
        formatted_path_printing(bestfs_solution)
    else:
        print("No path found with BestFS")

    return maze, avg_time_dfs, avg_states_dfs, avg_memory_dfs, avg_path_length_dfs, avg_time_bfs, avg_states_bfs, avg_memory_bfs, avg_path_length_bfs, avg_time_bestfs, avg_states_bestfs, avg_memory_bestfs, avg_path_length_bestfs, dfs_solution, bfs_solution, bestfs_solution

if __name__ == "__main__":
    main()