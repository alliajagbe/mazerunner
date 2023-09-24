import mazerunner


def heuristic(state, goal_position):
    row_distance = abs(state.position[0] - goal_position[0])
    col_distance = abs(state.position[1] - goal_position[1])
    distance = row_distance + col_distance
    return distance

def best_first_search(initial_state, goal_position):
    priority_queue = [(initial_state, [], 0)]
    explored = set()

    while priority_queue:
        current_state, path, cost = priority_queue.pop(0)
        explored.add(current_state.position)

        if mazerunner.goalTest(current_state, goal_position):
            return path + [current_state.position], len(explored), len(path + [current_state.position])
        
        for neighbour in mazerunner.moveGen(current_state):
            if neighbour.position not in explored:
                priority_queue.append((neighbour, path + [current_state.position], cost + heuristic(neighbour, goal_position)))
                priority_queue.sort(key=lambda x: x[2])

    return None

