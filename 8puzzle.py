
import operator
import copy

estado_inicial = [[1,2,3],[4,0,5],[6,7,8]]
#estado_inicial = [[1,2,3],[4,5,6],[7,8,0]]
pila_estados = []
#objetivo = [[1,2,3],[4,5,6],[7,8,0]]
objetivo = [[0,1,2],[3,4,5],[6,7,8]]
resuelto = False

class Estado():

    def __init__(self):
        self.estado = []
        self.piezas_fueraLugar = 0

def Posicion(estados, item):
   return [(ind, estado.index(item)) for ind, estado in enumerate(estados) if item in estado]

def Inicializar(estado_inicial):
    pila_estados.append(estado_inicial)

def CalcularMovimientos(posicion):
	movimientos = ['arriba','abajo','izquierda','derecha']
	if posicion[0][0] == 0:
		movimientos.remove('arriba')
	if posicion[0][0] == 2:
		movimientos.remove('abajo')
	if posicion[0][1] == 0:
		movimientos.remove('izquierda')
	if posicion[0][1] == 2 :
	    movimientos.remove('derecha')
	return movimientos

def ResolverMovimiento(posicion_nueva, posicion, pila_estados):
    copia_estado = []
    copia_estado = copy.deepcopy(pila_estados[-1]) # deepcopy para que la copia no referencie a la lista original
    numero = copia_estado[posicion_nueva[0]][posicion_nueva[1]] # Extraigo el valor que hay en la posicion que se tiene que mover el 0
    copia_estado[posicion[0][0]][posicion[0][1]] = numero # Ciclo Burbuja
    copia_estado[posicion_nueva[0]][posicion_nueva[1]] = 0
    return copia_estado

def EvaluarEstados(nuevos_estados,objetivo): #Evaluar cantidad de piezas fuera de lugar
    piezas_fueraLu = 0
    #Evaluo el tope de pila porque lo hago cada vez que realizo un movimiento 
    for i in range(0,3):
        for j in range(0,3):
            if objetivo[i][j] != nuevos_estados[-1].estado[i][j] and nuevos_estados[-1].estado[i][j] != 0:
                piezas_fueraLu += 1
    nuevos_estados[-1].piezas_fueraLugar = piezas_fueraLu

def OrdenarEstados(nuevos_estados):
    aux = Estado()
    c = 0
    for item in nuevos_estados:
        c1 = 0
        for item2 in nuevos_estados:
            if item.piezas_fueraLugar < item2.piezas_fueraLugar:
                aux = item2
                nuevos_estados[c1] = item
                nuevos_estados[c] = aux
            c1 += 1
        c += 1
    print("hola")
        
        

def Accion(pila_estados, posicion):
    movimientos = CalcularMovimientos(posicion)
    cant_estados = len(movimientos)
    nuevos_estados = [] # Lista de objetos de estado
    for movimiento in movimientos:
        objeto_estado = Estado() # Inicializo un nuevo objeto
        if movimiento == 'arriba':
            posicion_nueva = [] 
            posicion_nueva.append(posicion[0][0] - 1) #Calculo nueva posicion dependiendo donde me tenga que mover
            posicion_nueva.append(posicion[0][1])
            objeto_estado.estado = (ResolverMovimiento(posicion_nueva, posicion, pila_estados))
        elif movimiento == 'abajo':
            posicion_nueva = [] 
            posicion_nueva.append(posicion[0][0] + 1) #Calculo nueva posicion dependiendo donde me tenga que mover
            posicion_nueva.append(posicion[0][1])
            objeto_estado.estado = (ResolverMovimiento(posicion_nueva, posicion, pila_estados))
        elif movimiento == 'izquierda':
            posicion_nueva = [] 
            posicion_nueva.append(posicion[0][0]) #Calculo nueva posicion dependiendo donde me tenga que mover
            posicion_nueva.append(posicion[0][1] - 1)
            objeto_estado.estado = (ResolverMovimiento(posicion_nueva, posicion, pila_estados))
        else:
            posicion_nueva = [] 
            posicion_nueva.append(posicion[0][0]) #Calculo nueva posicion dependiendo donde me tenga que mover
            posicion_nueva.append(posicion[0][1] + 1 )
            objeto_estado.estado = (ResolverMovimiento(posicion_nueva, posicion, pila_estados))
        nuevos_estados.append(objeto_estado)
        EvaluarEstados(nuevos_estados, objetivo)
    OrdenarEstados(nuevos_estados)
    print("hola")
    

def Solucionar(pila_estados):
    global resuelto
    if len(pila_estados) == 0:
        Inicializar(estado_inicial)
    else:
        if pila_estados[-1] == objetivo:
            resuelto = True
        else:
            Accion(pila_estados, Posicion(pila_estados[-1], 0))

while resuelto == False:
    Solucionar(pila_estados)
print(resuelto)


    