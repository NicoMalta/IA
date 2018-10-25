import itertools
import re

from simpleai.search import (backtrack, CspProblem, LEAST_CONSTRAINING_VALUE,
                             min_conflicts, MOST_CONSTRAINED_VARIABLE)

variables = [1,2,3]
dominio = {
    1: ['Armadura', 'Madera',1,800],
    2: ['Armadura', 'Hierro',3,1000],
    3: ['Armadura', 'Acero',5,1300],
    4: ['Espada Madera',1,500],
    5: ['Espada Hierro',2,700],
    6: ['Espada Acero',4,1000],
    7: ['Garrote Madera',6,1300],
    8: ['Posion Fuego',1,5,1500],
    9: ['Posion Hielo',2,2,800],
    10: ['Posion Acido',3,3,1200]
}
restricciones = []    


def una_armadura(vars, vals):
    cantidad = 0
    if 'Armadura' in vals:
        cantidad += 1
    if cantidad < 2:
        return True
    else:
        return False


restricciones.append((variables, una_armadura))


problem = CspProblem(variables, dominio, restricciones)    
print('backtrack:')
result = backtrack(problem,
                   variable_heuristic=MOST_CONSTRAINED_VARIABLE,
                   value_heuristic=LEAST_CONSTRAINING_VALUE,
                   inference=True)

print(result)