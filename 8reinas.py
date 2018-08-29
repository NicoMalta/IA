
class Reinas:

    def __init__(self):
        self.tamaño = 4
        self.soluciones = 0
        self.Resolver()

    def Resolver(self):
        posiciones = [-1] * self.tamaño
        self.Accion(posiciones, 0)
        print("Found", self.soluciones, "soluciones.")
    
    def Accion(self, posiciones, fila_actual):
        if fila_actual == self.tamaño:
            self.Imprimir(posiciones)
            self.soluciones += 1
        else:
            for col in range(self.tamaño):
                if self.Validar_lugar(posiciones, fila_actual, col):
                    posiciones[fila_actual] = col
                    self.Accion(posiciones, fila_actual + 1)   
 
    def Validar_lugar(self, posiciones, filas_ocupadas, col):
        for i in range(filas_ocupadas):
            if posiciones[i] == col or \
                posiciones[i] - i == col - filas_ocupadas or \
                posiciones[i] + i == col + filas_ocupadas:

                return False
        return True

    def Imprimir(self, posiciones):
        for row in range(self.tamaño):
            line = ""
            for column in range(self.tamaño):
                if posiciones[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")


    def Costo(self, estado1, accion, estado2):
        pass
    

_ = Reinas()


