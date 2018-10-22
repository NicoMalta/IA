import itertools
import re

from simpleai.search import (backtrack, CspProblem, LEAST_CONSTRAINING_VALUE,
                             min_conflicts, MOST_CONSTRAINED_VARIABLE)

variables = [1,2,3]
armaduras = []
armas = []
pocion = []
armaduras.append(['Armadura',1,1,800])
armaduras.append(['Armadura',2,3,1000])
armaduras.append(['Armadura',3,5,1300])
armas.append(['Espada',1,1,500])
armas.append(['Espada',1,2,700])
armas.append(['Espada',2,4,1000])
armas.append(['Garrote',3,6,1300])
pocion.append(['Poción',1,5,1500])
pocion.append(['Poción',2,2,800])
pocion.append(['Poción',3,3,1200])
dominio = {}
restricciones = []    
dominio[1] = [x for x in armaduras]
dominio[2] = [x for x in armas]
dominio[3] = [x for x in pocion]

def una_armadura(vars, vals):
    carta1 = vals
    return len(carta1) == 1

restricciones.append((variables, una_armadura))


problem = CspProblem(variables, dominio, restricciones)    
print('backtrack:')
result = backtrack(problem,
                   variable_heuristic=MOST_CONSTRAINED_VARIABLE,
                   value_heuristic=LEAST_CONSTRAINING_VALUE,
                   inference=True)

print(result)