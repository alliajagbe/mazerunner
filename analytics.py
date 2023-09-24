import psutil
import matplotlib.pyplot as plt

def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss

def no_of_steps_visualizer():
    pass