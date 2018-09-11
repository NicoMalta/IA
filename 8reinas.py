tamaño = 4
def Resultado(estado):
    for fila in range(tamaño):
        col = Accion(estado, fila)
        estado[fila] = col
        Imprimir(estado)


def Accion(estado, fila_actual):
    for col in range(tamaño):
        if Validar_lugar(estado, fila_actual, col):
            estado[fila_actual] = col
            return col

def Validar_lugar(estado, filas_ocupadas, col):
    for i in range(filas_ocupadas):
        if estado[i] == col or \
            estado[i] - i == col - filas_ocupadas or \
            estado[i] + i == col + filas_ocupadas:
            return False
        return True

def Imprimir(posiciones):
    for row in range(tamaño):
        line = ""
        for column in range(tamaño):
            if posiciones[row] == column:
                line += "Q "
            else:
                line += ". "
            print(line)
            print("\n")


def Costo(estado1, accion, estado2):
    pass

estado = [-1] * tamaño
print(Resultado(estado))

