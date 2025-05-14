# 6. Dado una clase que implemente el patrón “prototipo” verifique que una clase
# generada a partir de ella permite por su parte obtener también copias de si misma.

import copy

# Clase que implementa el patrón Prototipo
class Producto:
    def __init__(self, nombre):
        self.nombre = nombre

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar(self):
        print(f"Producto: {self.nombre}")

# Instancia original
original = Producto("Producto A")

# Clonamos el original
copia1 = original.clonar()

# Clonamos la copia
copia2 = copia1.clonar()

# Mostramos para verificar
original.mostrar()
copia1.mostrar()
copia2.mostrar()

# Verificamos que todas las instancias son del mismo tipo
print("copia1 es instancia de Producto:", isinstance(copia1, Producto))
print("copia2 es instancia de Producto:", isinstance(copia2, Producto))
