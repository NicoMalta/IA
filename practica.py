import itertools
from simpleai.search import (backtrack, CspProblem, LEAST_CONSTRAINING_VALUE,
                             min_conflicts, MOST_CONSTRAINED_VARIABLE)
variables = [x+1 for x in range(9)]
restricciones = []
dominio = {
    1: [x+1 for x in range(30)],
    2: [x+1 for x in range(30)],
    3: [x+1 for x in range(30)],
    4: [x+1 for x in range(30)],
    5: [x+1 for x in range(30)],
    6: [x+1 for x in range(30)],
    7: [x+1 for x in range(30)],
    8: [x+1 for x in range(30)],
    9: [x+1 for x in range(30)],
}

def minimos(vars,vals):
    if abs(vars[1] - vars[0]) == 1 and abs(vars[1] - vars[2])  == 1 and abs(vars[1] - vars[3]) == 3:
        cantidad = 0
        if vals[1] < vals[0]:
            cantidad += 1
        if vals[1] < vals[2]:
            cantidad += 1
        if vals[1] < vals[3]:
            cantidad += 1
        if cantidad < 2:
            return False
    else:
        return True

for (var1,var2,var3,var4) in itertools.combinations(variables,4):
    restricciones.append(((var1,var2,var3,var4),minimos))


def distinto_valor(vars,vals):
    if abs(vars[0] - vars[1]) <= 2:
        if vals[0] == vals[1]:
            return False
        else:
            return True
    return True

for (var1,var2) in itertools.combinations(variables,2):
    restricciones.append(((var1,var2),distinto_valor))


problem = CspProblem(variables, dominio, restricciones)

print('backtrack:')
result = backtrack(problem,
                   variable_heuristic=MOST_CONSTRAINED_VARIABLE,
                   value_heuristic=LEAST_CONSTRAINING_VALUE,
                   inference=True)

print(result)