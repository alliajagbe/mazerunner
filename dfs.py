import mazerunner



def depth_first_search(initial_state, goal_position):
    stack = [(initial_state, [])]
    explored = set()

    while stack:
        current_state, path = stack.pop()
        explored.add(current_state.position)

        if mazerunner.goalTest(current_state, goal_position):
            return path + [current_state.position]
        
        for neighbour in mazerunner.moveGen(current_state):
            if neighbour.position not in explored:
                stack.append((neighbour, path + [current_state.position]))

    print("DFS explored a total of",len(explored),"states.")

    return None