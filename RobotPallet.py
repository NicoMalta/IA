pallets = { 2 : [1,0] , 3 : [3,0] , 4 : [2,0] , 6: [0,4],1 : [0,1] , 10: [1,1] , 5 : [0,2] , 8: [2,2],9 : [0,4] }

state = ([1,4],[],0)

exit = (2,4)

#for key,val in pallets.items():
#    print(key, "=>", val)

def is_goal(state):
    return len(state[-1]) == 0

def cost(s1,a,s2):
    return 1

def actions(state):
    robot_row, robot_col = state[0]
    list_actions = []
    if (state[0] in state[1]) and state[2] != 1:
        list_actions.append('Agarrar')
    elif (tuple(state[0]) == exit):
        list_actions.append('Dejar')
    else:
        if robot_row > 0:
            list_actions.append((robot_row -1, robot_col ))
        if robot_row < 2:
            list_actions.append((robot_row+1, robot_col ))
        if robot_col > 0:
            list_actions.append((robot_row, robot_col -1))
        if robot_col < 2:
            list_actions.append((robot_row,robot_col + 1))

    return tuple(list_actions)

def result(state,action):
    if action = list(exit) and state[2] == 1:
        state[0] == action
        state[2] = 0
    else: 
        if action == 'Agarrar':
            state[1].remove(state[0])
            state[2] == 1
        else:
            state[0] = action
    return state


print(result(state,'Agarrar'))