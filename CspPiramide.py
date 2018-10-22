import itertools
import re

from simpleai.search import (backtrack, CspProblem, LEAST_CONSTRAINING_VALUE,
                             min_conflicts, MOST_CONSTRAINED_VARIABLE)


vars = [i for i in range(10)]

domain = {}
restricciones = []
for var in vars:
    domain[var] = [x for x in range(51)]

domain[0] = [5]
domain[1] = [8]
domain[3] = [3]
domain[9] = [48]


def distinto_valor(vars,vals):
    return vals[0] != vals[1]

def suma_valores(vars, vals):
    # suponemos que las variables van a ser recibidas en el siguiente orden
    valor_superior, valor_izquierda, valor_derecha = vals
    return valor_superior == valor_izquierda + valor_derecha

for var1,var2 in itertools.combinations(vars,2):
    restricciones.append(((var1, var2), distinto_valor))

restricciones.append( ((4,0,1), suma_valores) )
restricciones.append( ((5,1,2), suma_valores) )
restricciones.append( ((6,2,3), suma_valores))
restricciones.append( ((7,4,5), suma_valores))
restricciones.append( ((8,5,6), suma_valores))
restricciones.append( ((9,7,8), suma_valores) )



problem = CspProblem(vars, domain, restricciones)

print('backtrack:')
result = backtrack(problem,
                   variable_heuristic=MOST_CONSTRAINED_VARIABLE,
                   value_heuristic=LEAST_CONSTRAINING_VALUE,
                   inference=True)

print(result)