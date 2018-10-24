state = [[0,0], 0]
goal = 64
# Estado plantear con control de estados repetidos: ((0,0),((0,0),...))
def is_goal(state):
    return state[-1] == goal
#En actions sacar cantidad de estados ya pintados

def actions(state):
    row, col = state[0]
    aux_actions = []
    list_actions = []
    aux_actions.append([row+2,col+1])
    aux_actions.append([row+1,col+2])
    aux_actions.append([row-2,col-1])
    aux_actions.append([row-1,col-2])

    aux_actions.append([row-1,col+2])
    aux_actions.append([row-2,col+1])
    aux_actions.append([row+1,col-2])
    aux_actions.append([row+2,col-1])
    agrego = True
    for action in aux_actions:
        if action[0] < 0: 
            agrego = False
        elif action[1] < 0:
            agrego = False
        if action[0] > 7:
            agrego = False
        elif action[1] > 7:
            agrego = False
        
        if agrego == True:
            list_actions.append(action)
        else:
            agrego = True
    
    return list_actions
#Agrego estado a la lista
def result(state,action):
    state[0] = action
    state[-1] =+ 1 
    return state

def cost(s1,a,s2):
    return 1
#Cantidad de lo q falta 64- len(estados)
def heuristic(state):
    jumps = state[-1]
    return (goal - jumps) 
print(heuristic(state))