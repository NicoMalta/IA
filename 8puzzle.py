
import operator
import copy

estado_inicial = [[1,2,3],[4,0,5],[6,7,8]]
#estado_inicial = [[1,2,3],[4,5,6],[7,8,0]]
#objetivo = [[1,2,3],[4,5,6],[7,8,0]]
objetivo = [[0,1,2],[3,4,5],[6,7,8]]


class Nodos():

    def __init__(self):
        self.estado = []
        self.nodo_padre = []
        self.accion = []
        self.ruta_costo = 0


def Posicion(estado, item):
    for fila_index, fila in enumerate(estado):
        for col_index, element in enumerate(fila):
            if element == item:
                return fila_index,col_index
               
def Meta(estado):
    return estado == objetivo

def Accion(estado):
    zero_fila, zero_col = Posicion(estado, 0)
    acciones = []
    Nodos_hijos = [] # Lista de objetos de estado
    Nodo_hijos = Nodo() # Inicializo un nuevo objeto
    if zero_fila > 0:
        acciones.append((zero_fila -1, zero_col ))
    if zero_fila < 0:
        acciones.append((zero_fila+1, zero_col ))
    if zero_col > 0:
        acciones.append((zero_fila, zero_col  -1))
    if zero_col < 2:
        acciones.append((zero_fila, zero_col + 1))

    return acciones

def Resultado(estado, accion):
    zero_fila, zero_col = Posicion(estado, 0)
    destino_fila, destino_col = accion

    estado = copy.deepcopy(estado)
    estado[zero_fila][zero_col] = estado[destino_fila][destino_col]
    estado[destino_fila][destino_col] = 0

    return estado

def costo(estado1, accion, estado2):
    return 1

def estado_inicial(estado):
    return estado

def Busqueda_nodos(estado):
    resultado = False
    nodo = Nodos()
    nodo.estado = estado_inicial(estado)
    nodo.ruta_costo = 0
    
	if Meta(nodo.estado) == True:
		return resultado = True
	frontera.append(nodo)
    explorados = []
	
    while resueltado == False:
		if len(frontera) == 0:
			return Resultado = False
		nodo = frontera.pop()
		explorados.append(nodo.estado)
        lista_acciones = accion(nodo.estado)
		for action in lista_acciones:
            nodo_hijo = Nodos()
			nodo_hijo.estado = Resultado(nodo.estado,action)
			if nodo_hijo is not in explorados or frontera: 
				if Meta(nodo_hijo.estado) == True:
					return resuelto = True
					frontera.append(nodo_hijo)
			
			
print(Resultado(estado_inicial, [2,1]))
