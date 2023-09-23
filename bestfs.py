import mazerunner


def heuristic(state, goal_position):
    row_distance = abs(state.position[0] - goal_position[0])
    col_distance = abs(state.position[1] - goal_position[1])
    distance = row_distance + col_distance
    return distance

def best_first_search(initial_state, goal_position):
    pass