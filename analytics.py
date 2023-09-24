import matplotlib.pyplot as plt
from test import main

def path_visualizer(maze, path):
    maze_copy = maze.copy()

    for row, col in path:
        maze_copy[row][col] = 2

    cmap = plt.matplotlib.colors.ListedColormap(["black", "white", "green", "red"])

    plt.matshow(maze_copy, cmap=cmap)
    plt.show()



def visualizer():
    avg_time_dfs, avg_states_dfs, avg_memory_dfs, avg_path_length_dfs, avg_time_bfs, avg_states_bfs, avg_memory_bfs, avg_path_length_bfs, avg_time_bestfs, avg_states_bestfs, avg_memory_bestfs, avg_path_length_bestfs, dfs_solution, bfs_solution, bestfs_solution = main()

    # Plotting time
    time = [avg_time_dfs, avg_time_bfs, avg_time_bestfs]
    labels = ["DFS", "BFS", "BestFS"]
    plt.bar(labels, time)
    plt.title("Average time for each algorithm")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (s)")
    plt.show()

    # Plotting states
    states = [avg_states_dfs, avg_states_bfs, avg_states_bestfs]
    labels = ["DFS", "BFS", "BestFS"]
    plt.bar(labels, states, color="orange")
    plt.title("Average number of states explored for each algorithm")
    plt.xlabel("Algorithm")
    plt.ylabel("Number of states explored")
    plt.show()

    # Plotting memory
    memory = [avg_memory_dfs, avg_memory_bfs, avg_memory_bestfs]
    labels = ["DFS", "BFS", "BestFS"]
    plt.bar(labels, memory, color="green")
    plt.title("Average memory usage for each algorithm")
    plt.xlabel("Algorithm")
    plt.ylabel("Memory (bytes)")
    plt.show()

    # Plotting path length
    path_length = [avg_path_length_dfs, avg_path_length_bfs, avg_path_length_bestfs]
    labels = ["DFS", "BFS", "BestFS"]
    plt.bar(labels, path_length, color="red")
    plt.title("Average path length for each algorithm")
    plt.xlabel("Algorithm")
    plt.ylabel("Path length")
    plt.show()

    # Plotting path
    if dfs_solution:
        dfs_path = dfs_solution
        plt.plot(dfs_path)
        plt.title("Path found with DFS")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    else:
        print("No path found with DFS")

    if bfs_solution:
        bfs_path = bfs_solution
        plt.plot(bfs_path)
        plt.title("Path found with BFS")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    else:
        print("No path found with BFS")

    if bestfs_solution:
        bestfs_path = bestfs_solution
        plt.plot(bestfs_path)
        plt.title("Path found with BestFS")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    else:
        print("No path found with BestFS")

visualizer()