#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                         *
#* Calcula el factorial de un número utilizando la programación orientada  *
#* a objetos.                                                              *
#*-------------------------------------------------------------------------*

class Factorial:
    def __init__(self, min_val, max_val):
        """
        Constructor que inicializa el rango de números.
        :param min_val: valor mínimo (inclusive).
        :param max_val: valor máximo (inclusive).
        """
        self.min = min_val
        self.max = max_val

    def factorial(self, num): 
        """
        Calcula el factorial de un número.
        :param num: Número al cual se le calculará el factorial.
        :return: Factorial de 'num'.
        """
        if num < 0: 
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0: 
            return 1
        else: 
            fact = 1
            while num > 1: 
                fact *= num 
                num -= 1
            return fact

    def run(self):
        """
        Ejecuta el cálculo de factorial para todos los números en el rango
        desde 'min' hasta 'max'.
        """
        for num in range(self.min, self.max + 1):
            print(f"Factorial de {num} es {self.factorial(num)}")


def pedir_numero():
    """
    Solicita un número al usuario.
    :return: El número ingresado por el usuario.
    """
    try:
        num = int(input("Ingrese el valor para calcular factorial: "))
        return num
    except ValueError:
        print("Por favor ingrese un número válido.")
        exit()

# Función para manejar rangos
def manejar_rango(arg):
    """
    Maneja los rangos de entrada (desde-hasta, desde-, -hasta).
    :param arg: El argumento de rango a analizar.
    :return: El valor mínimo y máximo del rango.
    """
    if '-' in arg:
        limites = arg.split('-')
        if limites[0] == '':  # Caso -hasta
            return (1, int(limites[1]))
        elif limites[1] == '':  # Caso desde-
            return (int(limites[0]), 60)
        else:  # Caso desde-hasta
            return (int(limites[0]), int(limites[1]))
    else:
        return (int(arg), int(arg))

# Uso de los argumentos de la línea de comando
import sys

if len(sys.argv) == 1:
    print("Debe informar un número o un rango!")
    sys.exit()

if '-' in sys.argv[1]:
    min_num, max_num = manejar_rango(sys.argv[1])
    factorial_obj = Factorial(min_num, max_num)
    factorial_obj.run()
else:
    num = int(sys.argv[1])
    factorial_obj = Factorial(num, num)
    factorial_obj.run()
