
import operator
import copy

estado_inicial = ([1,3,6],
                  [0,4,2],
                  [7,5,8])
#estado_inicial = [[1,2,3],[4,5,6],[7,8,0]]
#objetivo = [[1,2,3],[4,5,6],[7,8,0]]
objetivo = ([1,2,3],
            [4,5,6],
            [7,8,0])

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
    nivel = 0
    if Meta(nodo_inicial.estado):
        solucionado = True
        return solucionado
    frontera.append(nodo_inicial)
    explorados = []
    while solucionado == False:
        nodo = Nodo()
        nivel += 1
        if len(frontera) == 0:
            solucionado = False
            return solucionado

        nodo = frontera.pop(0) #FIFO
        
        if nodo.estado not in explorados:
            explorados.append(nodo.estado)
            print("====================", nivel ,"=====================")
            for action in Accion(nodo.estado):
                nodo_hijo = Nodo()
                #nodo_hijo.nodo_padre = nodo
                nodo_hijo.estado = Resultado(nodo.estado,action)
                #nodo_hijo.ruta_costo = Costo(nodo, action, nodo_hijo)
                nodo.accion.append(tuple(action))
                Imprimir(nodo_hijo.estado)
                if nodo_hijo.estado not in explorados: 
                    if Meta(nodo_hijo.estado) == True:
                        solucionado = True
                        return solucionado,nivel
                    frontera.append(nodo_hijo)
                    print(len(frontera))	


def Imprimir(estado):
    print(estado[0])
    print(estado[1])
    print(estado[2])
    print("\n")


def Busqueda_Profundidad(estadoInicial):
        frontera = []  
        """Se saca de atras para adelante LIFO"""
        procesados = []
        nodo_inicial = Nodo()
        nodo_inicial.estado = estadoInicial

        frontera.append(nodo_inicial)
        nivel = 0
        
        while len(frontera) != 0 or solucionado == true :
            
            print("====================", nivel ,"=====================")

            nodoActual = Nodo()
            nodoActual = frontera[-1]

            if Meta(nodoActual.estado) == True:
                break
            else:
                procesados.append(nodoActual.estado)
                accionesPosibles = Accion(nodoActual.estado)
                tieneHijos = False
                for accion in accionesPosibles:
                    
                    nodoHijo = Nodo()
                    nodoHijo.estado = Resultado(nodoActual.estado , accion)
                    if (nodoHijo.estado not in procesados):
                        frontera.append(nodoHijo)
                        tieneHijos = True
                        Imprimir(nodoHijo.estado)
                        break
                if tieneHijos == False:
                    frontera.pop()
            
            nivel += 1
         
            			
print(Busqueda_Amplitud(estado_inicial))
