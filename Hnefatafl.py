from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer, BaseViewer

state = (3,3)
soldiers = ((0,0),(0,1),(0,4),(1,4),(2,0),(3,1),(3,6),(4,0),(6,3),(6,5))
exits = ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(1,0),(2,0),(3,0),(4,0),(5,0),(1,6),(2,6),(3,6),(4,6),(5,6))

class HnefataflProblem(SearchProblem):
    def is_goal(self,state):
        return state in exits

    def cost(self,s1,a,s2):
        return 1

    def actions(self,state):
        row_king, col_king = state
        actions = []
        if (row_king + 2,col_king) not in soldiers and (row_king +1) < 7 and (row_king + 1,col_king-1) not in soldiers and (row_king + 1,col_king+1) not in soldiers:
            actions.append((row_king + 1,col_king))
        if (row_king - 2,col_king) not in soldiers and (row_king -1) > 0 and (row_king - 1,col_king-1) not in soldiers and (row_king - 1,col_king+1) not in soldiers:
            actions.append((row_king - 1,col_king))
        if (row_king,col_king + 2) not in soldiers and (col_king +1) < 7 and (row_king - 1,col_king+1) not in soldiers and (row_king + 1,col_king+1) not in soldiers:
            actions.append((row_king,col_king + 1 ))
        if (row_king ,col_king - 2) not in soldiers and (row_king -1) > 0 and (col_king +1) < 7 and (row_king - 1,col_king-1) not in soldiers and (row_king + 1,col_king-1) not in soldiers:
            actions.append((row_king ,col_king - 1))
        return tuple(actions)

    def result(self,state,action):
        state = action
        return state    

    def heuristic(self,state):
        distancias = []
        for exit in exits:
            distancias.append(exit)
        return min([manhattan(x, state) for x in distancias])

def manhattan(pos1,pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2 - x1) + abs(y2 - y1)



my_viewer = BaseViewer()
r = astar(HnefataflProblem(state),graph_search = True, viewer = WebViewer() )    

#print(my_viewer.stats)