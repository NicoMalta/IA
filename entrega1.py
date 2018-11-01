
# coding: utf-8
from simpleai.search import astar, breadth_first, SearchProblem,depth_first
from simpleai.search.viewers import WebViewer, BaseViewer

orillas = ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(2,0),(3,0),(4,0),(5,0),(5,1), (5,2),(5,3),(5,4),(5,5),(4,5),(3,5),(4,5))

state = ((0,0),((2,1),(3,4),(4, 2)),())
        #((POS ROBOT),(POS PEOPLE ),(POS BLOQUES YA PASE))
salve_pibe = []
class TpProblem(SearchProblem):

    def is_goal(self, state):
        return len(state[1]) == 0

    def cost(self,s1,action,s2):
        return 1

    def actions(self,state):
        row, col = state[0]
        actions = []
        if row > 0:
            if is_valid((row -1, col), state):
                actions.append((row -1, col ))
        if row < 5:
            if is_valid((row +1, col), state):
                actions.append((row+1, col ))
        if col > 0:
            if is_valid((row, col -1), state):
                actions.append((row, col  -1))
        if col < 2:
            if is_valid((row, col +1), state):
                actions.append((row, col + 1))
        if len(state[1]) != 0 and state[0] != (0,0) :
            for action in actions:
                if action in orillas:
                    actions.remove(action)
        return tuple(actions)


    def result(self,state,action):
        row_action, col_action = action
        support_state = list(state)
        if (row_action, col_action) in state[1]:
            count = 0
            aux_state = list(state[1])
            for people in aux_state:
                if people == (row_action, col_action):
                    salve_pibe.append(len(salve_pibe)+1)
                    del aux_state[count]
                count += 1
            support_state[1] = tuple(aux_state)
        support_state[0] = action
        aux_state = list(state[2])
        if (row_action, col_action) not in orillas:
            aux_state.append(action)
            support_state[2] = tuple(aux_state)
        state = tuple(support_state)
        return state

    def heuristic(self,state):
        distances = []
        people_distance = 0
        first_people = 0
        if len(state[1]) > 0:
            for people in state[1]:
                distances.append(people)
            first_people = min([manhattan(x, state[0]) for x in distances])
            people_distance = sum([manhattan(x, state[0]) for x in distances])
        distances.clear()
        for pos in orillas:
            distances.append(pos)
        minium_distance = min([manhattan(x, state[0]) for x in distances])
        return minium_distance + people_distance + first_people


def is_valid(pos,state):
    for pos_traveled in state[-1]:
        if pos == pos_traveled:
            return False
    return True

def manhattan(pos1,pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2 - x1) + abs(y2 - y1)

def resolver(metodo_busqueda,posiciones_personas:
    result = astar(TpProblem(state), graph_search=True, viewer=my_viewer)
    return result
my_viewer = BaseViewer()

print(my_viewer.stats)
print(salve_pibe)
print(my_viewer.solution_node)