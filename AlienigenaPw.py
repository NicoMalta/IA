from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer, BaseViewer

state = (0,0,0)
goal = (5,1,8)

class alienigenaProblem(SearchProblem):
    def is_goal(self,state):
        return state == goal

    def cost(self,s1,a,s2):
        return 1

    def actions(self,state):
        list_Actions = []

        aux_state = list(state)
        aux_state[0] = aux_state[0] +3
        if aux_state[0] > 9:
           aux_state[0] = aux_state[0] - 10
        list_Actions.append(tuple(aux_state))

        aux_state = list(state)
        aux_state[0] = aux_state[0] - 2
        if aux_state[0] < 0:
            aux_state[0] = 10 + aux_state[0]
        list_Actions.append(tuple(aux_state))

        aux_state = list(state)
        aux = aux_state[0]
        aux_state[0] = aux_state[1]
        aux_state[1] = aux
        list_Actions.append(tuple(aux_state))

        aux_state = list(state)
        aux = aux_state[2]
        aux_state[2] = aux_state[1]
        aux_state[1] = aux
        list_Actions.append(tuple(aux_state))
        return list_Actions

    def result(self,state,action):
        state = action
        return state

    def heuristic(self,state):
        cant_dist = [(state == goal) for state, goal in zip(state,goal)]
        return cant_dist.count(False)

problema = alienigenaProblem(state)
my_viewer = BaseViewer()
r = astar(problema,graph_search = True, viewer = my_viewer )    

print(my_viewer.stats)

