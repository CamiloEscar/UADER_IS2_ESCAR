# 2. Implemente una clase bajo el patrón iterator que almacene una cadena de
# caracteres y permita recorrerla en sentido directo y reverso

# Se importan módulos necesarios para trabajar con tipos de datos y clases de colección
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

# Clase que implementa un iterador para recorrer una cadena en sentido inverso
class ReverseIterator:
    def __init__(self, data):
        self.data = data              # Guarda la cadena de caracteres
        self.index = len(data)        # Inicializa el índice al final de la cadena

    def __iter__(self):
        return self                   # Devuelve el iterador mismo

    def __next__(self):
        if self.index <= 0:           # Si se ha llegado al inicio, se detiene la iteración
            raise StopIteration
        self.index -= 1               # Se mueve un carácter hacia atrás
        return self.data[self.index]  # Devuelve el carácter actual

# Clase que implementa un iterador para recorrer una cadena en sentido directo
class StringIterator:
    def __init__(self, data):
        self.data = data              # Guarda la cadena de caracteres
        self.index = 0                # Inicializa el índice al inicio

    def __iter__(self):
        return self                   # Devuelve el iterador mismo

    def __next__(self):
        if self.index >= len(self.data):  # Si se ha llegado al final, se detiene la iteración
            raise StopIteration
        self.index += 1
        return self.data[self.index - 1]  # Devuelve el carácter actual y avanza el índice

# Clase que permite combinar múltiples iteradores
class CombinedIterator:
    def __init__(self, data: List[Any] = [], collection: List[Any] = []) -> None:
        self.data = data                  # Guarda una lista de iteradores
        self._collection = collection     # Opcional: lista para almacenar otros elementos

    def __iter__(self):
        for iterator in self.data:
            yield from iterator
          # Devuelve un iterador sobre la lista de iteradores
    
    def add_item(self, item: Any):
        self._collection.append(item)     # Permite agregar elementos a la colección adicional

# Ejemplo de uso
cadena = "Ingenieria en Software "

# Recorriendo en sentido directo con StringIterator
iterator = StringIterator(cadena)
for char in iterator:
    print(char)

print("---")

# Recorriendo en sentido inverso con ReverseIterator
reverse_iterator = ReverseIterator(cadena)
for char in reverse_iterator:
    print(char)

print("---")

# Recorriendo en sentido directo y reverso combinados
combined_iterator = CombinedIterator([StringIterator(cadena), ReverseIterator(cadena)])
for char in combined_iterator:
    print(char)

# Se crea una instancia de CombinedIterator como contenedor de datos personalizados
collection = CombinedIterator()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

