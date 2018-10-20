orillas = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[2,0],[3,0],[4,0],[5,0],[5,1], [5,2],[5,3],[5,4],[5,5],[4,5],[3,5],[4,5]]

state = ([0,0],[[2,1],[3, 4],[4, 2]],[])

def is_goal(state):
    return len(state[1]) == 0

def cost(s1,action,s2):
    return 1

def actions(state):
    row, col = state[0]
    tuple_actions = []
    if row > 0:
        if is_valid((row -1, col ), state):
            tuple_actions.append((row -1, col ))
    if row < 5:
        if is_valid((row +1, col ), state):
            tuple_actions.append((row+1, col ))
    if col > 0:
        if is_valid((row, col -1), state):
            tuple_actions.append((row, col  -1))
    if col < 2:
        if is_valid((row, col +1), state):
            tuple_actions.append((row, col + 1))

    return tuple(tuple_actions)


def is_valid(pos,state):
    
    for pos_traveled in state[-1]:
        if pos == pos_traveled:
            return False
    return True

def result(state,action):
    row_action, col_action = action
    if [row_action, col_action] in state[1]:
        count = 0
        for people in state[1]:
            if people == [row_action, col_action]:
                del state[1][count]
    state[0][0] = row_action
    state[0][1] = col_action
    if [row_action, col_action] not in orillas:
        state[-1].append([row_action,col_action])
    return tuple(state)

def heuristic(state):
    distances = []
    if len(state[1]) > 0:
        for people in state[1]:
            distances.append(people)
    else:
        for pos in orillas:
            distances.append(pos)
    return max(distances)

print(heuristic(state))