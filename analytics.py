import matplotlib.pyplot as plt
from test import main



def visualizer():
    avg_time_dfs, avg_states_dfs, avg_memory_dfs, avg_time_bfs, avg_states_bfs, avg_memory_bfs, avg_time_bestfs, avg_states_bestfs, avg_memory_bestfs, dfs_solution, bfs_solution, bestfs_solution = main()

    # Plotting time
    time = [avg_time_dfs, avg_time_bfs, avg_time_bestfs]
    labels = ["DFS", "BFS", "BestFS"]
    plt.bar(labels, time)
    plt.title("Average time for each algorithm")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (s)")
    plt.show()

visualizer()