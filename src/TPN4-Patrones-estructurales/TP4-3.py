# Represente la lista de piezas componentes de un ensamblado con sus relaciones jerárquicas. 
# Empiece con un producto principal formado por tres sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. 
# Genere clases que representen esa configuración y la muestren. 
# Luego agregue un sub-conjunto opcional adicional también formado por cuatro piezas. 
# (Use el patrón composite).

from __future__ import annotations
from abc import ABC

class Componente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}- {self.nombre}")


class Pieza(Componente):
    pass


class Ensamblado(Componente):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.componentes = []

    def agregar_componente(self, componente) -> None:
        self.componentes.append(componente)

    def mostrar(self, nivel=0) -> None:
        indentacion = "  " * nivel
        print(f"{indentacion}+ {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)


# Creación de la estructura jerárquica
producto_principal = Ensamblado("Producto Principal")

subconjunto1 = Ensamblado("Subconjunto 1")
subconjunto2 = Ensamblado("Subconjunto 2")
subconjunto3 = Ensamblado("Subconjunto 3")

for i in range(4):
    pieza1 = Pieza(f"Pieza {i+1}")
    subconjunto1.agregar_componente(pieza1)

    pieza2 = Pieza(f"Pieza {i+5}")
    subconjunto2.agregar_componente(pieza2)

    pieza3 = Pieza(f"Pieza {i+9}")
    subconjunto3.agregar_componente(pieza3)

producto_principal.agregar_componente(subconjunto1)
producto_principal.agregar_componente(subconjunto2)
producto_principal.agregar_componente(subconjunto3)

# Mostrar la configuración
producto_principal.mostrar()

# Agregar un subconjunto opcional
subconjunto_opcional = Ensamblado("Subconjunto Opcional")

for i in range(4):
    pieza_opcional = Pieza(f"Pieza Opcional {i+1}")
    subconjunto_opcional.agregar_componente(pieza_opcional)

producto_principal.agregar_componente(subconjunto_opcional)

# Mostrar la configuración actualizada
print("\nConfiguración actualizada:")
producto_principal.mostrar()



# En esta implementación, la clase Componente es la clase base que representa tanto las piezas individuales como los ensamblados. Cada componente tiene un nombre y un método mostrar que imprime su nombre en la consola.
# La clase Pieza hereda de Componente y no tiene ninguna funcionalidad adicional.
# La clase Ensamblado también hereda de Componente, pero además tiene una lista de componentes internos. Tiene un método agregar_componente para agregar un componente a la lista, y un método mostrar que imprime su nombre y luego recorre la lista de componentes para mostrarlos de forma recursiva.
# En el ejemplo proporcionado, se crea un producto principal compuesto por tres subconjuntos, cada uno de ellos formado por cuatro piezas. Luego se agrega un subconjunto opcional también formado por cuatro piezas. Al mostrar la configuración, se imprimirán los componentes jerárquicamente.
# Al agregar el subconjunto opcional y mostrar la configuración actualizada, se ve la estructura ampliada con el nuevo subconjunto.