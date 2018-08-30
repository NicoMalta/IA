
import operator
import copy

estado_inicial = [[1,2,3],[4,6,8],[7,5,0]]
#estado_inicial = [[1,2,3],[4,5,6],[7,8,0]]
#objetivo = [[1,2,3],[4,5,6],[7,8,0]]
objetivo = [[1,2,3],[4,5,6],[7,8,9]]


class Nodo:

    def __init__(self):
        self.estado = []
        self.nodo_padre = None
        self.accion = []
        self.ruta_costo = 0

def Posicion(estado, item):
    for fila_index, fila in enumerate(estado):
        for col_index, element in enumerate(fila):
            if element == item:
                return fila_index,col_index
               
def Meta(estado):
    if estado == objetivo:
        return True
    else:
        return False

def Accion(estado):
    zero_fila, zero_col = Posicion(estado, 0)
    acciones = []
    if zero_fila > 0:
        acciones.append((zero_fila -1, zero_col ))
    if zero_fila < 2:
        acciones.append((zero_fila+1, zero_col ))
    if zero_col > 0:
        acciones.append((zero_fila, zero_col  -1))
    if zero_col < 2:
        acciones.append((zero_fila, zero_col + 1))

    return tuple(acciones)

def Resultado(estado, accion):
    zero_fila, zero_col = Posicion(estado, 0)
    destino_fila, destino_col = accion

    estado = copy.deepcopy(estado)
    estado[zero_fila][zero_col] = estado[destino_fila][destino_col]
    estado[destino_fila][destino_col] = 0

    return tuple(estado)

def Costo(estado1, accion, estado2):
    return 1

def Estado_inicial(estado):
    return estado


def Busqueda_Amplitud(estado):
    solucionado = False
    nodo_inicial = Nodo()
    nodo_inicial.estado = Estado_inicial(estado)
    nodo_inicial.ruta_costo = 0
    frontera = []

    if Meta(nodo_inicial.estado):
        return solucionado == True
    frontera.append(nodo_inicial)
    explorados = []

    while solucionado == False:
        nodo = Nodo()
        if len(frontera) == 0:
            return solucionado == False
        nodo = frontera.pop()
        explorados.append(nodo.estado)
        for action in Accion(nodo.estado):
            nodo_hijo = Nodo()
            nodo_hijo.nodo_padre = nodo
            nodo_hijo.estado = Resultado(nodo.estado,action)
            nodo_hijo.ruta_costo = Costo(nodo, action, nodo_hijo)
            nodo.accion.append(tuple(action))
            if nodo_hijo.estado not in explorados or nodo_hijo not in frontera: 
                if Meta(nodo_hijo.estado) == True:
                    return solucionado == True
                frontera.append(nodo_hijo)	

			
print(Busqueda_Amplitud(estado_inicial))
