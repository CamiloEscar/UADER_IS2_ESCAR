# Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho dispone de dos trenes laminadores, 
# uno que genera planchas de 5 mts y otro de 10 mts. Genere una clase que represente a las láminas en forma genérica al
# cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el patrón bridge en la solución).

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "Produciendo lámina de 0,5 de espesor y 1,5 metros de ancho en el tren laminador de 5 metros."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "Produciendo lámina de 0,5 de espesor y 1,5 metros de ancho en el tren laminador de 10 metros."


def client_code(abstraction: Abstraction) -> None:
    # ...

    print(abstraction.operation(), end="")

    # ...

if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

    print("\n")