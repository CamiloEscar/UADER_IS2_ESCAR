#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys


def factorial(num):
    if num < 0:
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0:
        return 1

    else:
        fact = 1
        while (num > 1):
            fact *= num
            num -= 1
        return fact


def pedir_numero():
    num = input("ingresar un numero: ")
    try:
        return int(num)
    except ValueError:
        print("Debe ingresar un número entero!")
        sys.exit()


def manejar_rango(arg):
    if '-' in arg:
        limites = arg.split('-')
        if limites[0] == '':  # caso -hasta
            return (1, int(limites[1]))
        elif limites[1] == '':  # caso desde-
            return (int(limites[0]), 60)
        else:  # caso desde-hasta
            return (int(limites[0]), int(limites[1]))
    else:
        return (int(arg), int(arg))


if len(sys.argv) == 1:
    print("Debe informar un número o rango!")
    sys.exit()

    # si hay un rango, manejarlo
if '-' in sys.argv[1]:
    min_num, max_num = manejar_rango(sys.argv[1])
    for num in range(min_num, max_num + 1):
        print("Factorial ", num, "! es ", factorial(num))
else:
    # si solo se pasa un numero, calcular el factorail

    num = int(sys.argv[1])
    print("Factorial ", num, "! es ", factorial(num))
