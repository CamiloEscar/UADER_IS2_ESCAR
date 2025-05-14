# Imagine una situación donde pueda ser de utilidad el patrón “abstract factory”

# El patrón Abstract Factory se usa cuando se necesita crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.


from abc import ABC, abstractmethod

# Interfaces de los productos
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

# Fábrica abstracta
class FabricaJuguetes(ABC):
    @abstractmethod
    def crear_animal(self) -> Animal:
        pass

    @abstractmethod
    def crear_vehiculo(self) -> Vehiculo:
        pass


# Fábrica de juguetes blandos (para bebés)
class AnimalBebe(Animal):
    def hablar(self):
        print("Osito de peluche")

class VehiculoBebe(Vehiculo):
    def mover(self):
        print("Coche")

class FabricaBebe(FabricaJuguetes):
    def crear_animal(self) -> Animal:
        return AnimalBebe()

    def crear_vehiculo(self) -> Vehiculo:
        return VehiculoBebe()


# Fábrica de juguetes para niños

class AnimalGrande(Animal):
    def hablar(self):
        print("Perro")

class VehiculoGrande(Vehiculo):
    def mover(self):
        print("Bici")

class FabricaGrande(FabricaJuguetes):
    def crear_animal(self) -> Animal:
        return AnimalGrande()

    def crear_vehiculo(self) -> Vehiculo:
        return VehiculoGrande()


# Cliente 
def jugar(fabrica: FabricaJuguetes):
    animal = fabrica.crear_animal()
    vehiculo = fabrica.crear_vehiculo()
    animal.hablar()
    vehiculo.mover()


if __name__ == "__main__":
    edad = int(input("¿Edad del niño?: "))

    if edad <= 3:
        fabrica = FabricaBebe()
    else:
        fabrica = FabricaGrande()

    jugar(fabrica)
