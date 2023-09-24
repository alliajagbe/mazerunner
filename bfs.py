import mazerunner

def breadth_first_search(initial_state, goal_position):
    queue = [(initial_state, [])]
    explored = set()

    while queue:
        current_state, path = queue.pop(0)
        explored.add(current_state.position)

        if mazerunner.goalTest(current_state, goal_position):
            return path + [current_state.position], len(explored)
        
        for neighbour in mazerunner.moveGen(current_state):
            if neighbour.position not in explored:
                queue.append((neighbour, path + [current_state.position]))

    return None
