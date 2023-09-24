import matplotlib.pyplot as plt
from test import main

def path_visualizer(maze, path, title):
    maze_copy = maze.copy()

    for row, col in path:
        maze_copy[row][col] = 2

    cmap = plt.matplotlib.colors.ListedColormap(["black", "white", "red", "green"])

    plt.matshow(maze_copy, cmap=cmap)

    # annotate start and end positions
    plt.annotate("Start", (path[0][1], path[0][0]), color="white", weight="bold", fontsize=16, ha="center", va="center")
    plt.annotate("End", (path[-1][1], path[-1][0]), color="white", weight="bold", fontsize=16, ha="center", va="center")

    # annotate path taken
    for i, (row, col) in enumerate(path):
        if i == 0 or i == len(path) - 1:
            continue
        else:
            plt.annotate(i, (col, row), color="white", weight="bold", fontsize=16, ha="center", va="center")

    plt.title(title)

    plt.show()



def visualizer():
    maze, avg_time_dfs, avg_states_dfs, avg_memory_dfs, avg_path_length_dfs, avg_time_bfs, avg_states_bfs, avg_memory_bfs, avg_path_length_bfs, avg_time_bestfs, avg_states_bestfs, avg_memory_bestfs, avg_path_length_bestfs, dfs_solution, bfs_solution, bestfs_solution = main()

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

    # showing all plots at once
    fig, axs = plt.subplots(2, 2)
    fig.suptitle("Comparing algorithms")
    axs[0, 0].bar(labels, time)
    axs[0, 0].set_title("Average time for each algorithm")
    axs[0, 0].set_xlabel("Algorithm")
    axs[0, 0].set_ylabel("Time (s)")
    axs[0, 1].bar(labels, states, color="orange")
    axs[0, 1].set_title("Average number of states explored for each algorithm")
    axs[0, 1].set_xlabel("Algorithm")
    axs[0, 1].set_ylabel("Number of states explored")
    axs[1, 0].bar(labels, memory, color="green")
    axs[1, 0].set_title("Average memory usage for each algorithm")
    axs[1, 0].set_xlabel("Algorithm")
    axs[1, 0].set_ylabel("Memory (bytes)")
    axs[1, 1].bar(labels, path_length, color="red")
    axs[1, 1].set_title("Average path length for each algorithm")
    axs[1, 1].set_xlabel("Algorithm")
    axs[1, 1].set_ylabel("Path length")
    plt.tight_layout()
    plt.show()

    path_visualizer(maze, dfs_solution, "Depth First Search Solution")
    path_visualizer(maze, bfs_solution, "Breadth First Search Solution")
    path_visualizer(maze, bestfs_solution, "Best First Search Solution")

visualizer()