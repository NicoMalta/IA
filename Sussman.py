
from random import randint
state = [[2],[1,3],[]]
goal = [[],[],[3,2,1]]

def is_goal(state):
    return goal == state

def actions(state):
    list_cubes = available_cubes(state)
    while len(list_cubes) > 1:
        random = randint(0, (len(list_cubes)-1))
        del list_cubes[random]
        
    cube, col = list_cubes[0]
    list_actions = []
    if col == 0:
        list_actions.append([cube,col+1])
        list_actions.append([cube,col+2])
    else: 
        if col == 1:
            list_actions.append([cube,col-1])
            list_actions.append([cube,col+1])
        else:
            list_actions.append([cube,col-1])
            list_actions.append([cube,col-2])
    return list_actions

def available_cubes(state):
    list_cubes = []
    col = 0
    for cubes in state:
        if len(cubes) == 0:
            pass
        else:
            if len(cubes) == 1:
                list_cubes.append([cubes[-1],col])
            else:
                list_cubes.append([cubes[-1],col])
        col += 1        
    return list_cubes
            

def result(state, action):
    cube, col = action
    return (state[col].append(cube))

def cost(s1,action,s2):
    return 1

def heuristic(state):
    count = 0
    for col in range(0, 2):
        for cube in range(0, len(state[col])):
            if 
            if state[col][cube] != goal[col][cube]:
                count += 1
    return count

print(heuristic(state))