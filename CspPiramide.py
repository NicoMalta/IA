import itertools
import re

from simpleai.search import (backtrack, CspProblem, LEAST_CONSTRAINING_VALUE,
                             min_conflicts, MOST_CONSTRAINED_VARIABLE)


vars = [i+1 for i in range(10)]

domain = {}
restricciones = []
for var in vars:
    domain[var] = [x for x in range(51)]

domain[1] = [5]
domain[2] = [8]
domain[4] = [3]
domain[10] = [48]
#print(domain)

def distinto_valor(vars,vals):
    return vals[0] != vals[1]

def suma_valores(vars, vals):
    # suponemos que las variables van a ser recibidas en el siguiente orden
    valor_superior, valor_izquierda, valor_derecha = vals
    return valor_superior == valor_izquierda + valor_derecha

for var1,var2 in itertools.combinations(vars,2):
    restricciones.append(((var1, var2), distinto_valor))

restricciones.append( ((5,1,2), suma_valores) )
restricciones.append( ((6,2,3), suma_valores) )
restricciones.append( ((7,3,4), suma_valores))
restricciones.append( ((8,5,6), suma_valores))
restricciones.append( ((9,6,7), suma_valores))
restricciones.append( ((10,8,9), suma_valores) )



problem = CspProblem(vars, domain, restricciones)

print('backtrack:')
result = backtrack(problem,
                   variable_heuristic=MOST_CONSTRAINED_VARIABLE,
                   value_heuristic=LEAST_CONSTRAINING_VALUE,
                   inference=True)

print(result)