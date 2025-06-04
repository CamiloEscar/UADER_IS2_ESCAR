#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Continuando con el programa primes.py previamente utilizado se usará ahora en el
# contexto de un cambio organizacional mas profundo.
# 1. Se utilizará para generar una clave de encriptación, para lo cual deberán
# tomarse dos números primos al azar entre 1 y 100 y retornar la multiplicación
# de ambos.
# 2. Deberá guardar memoria de los últimos 10 pares generados para no repetirlos


import random

# Paso 1: Generar la lista de números primos entre 1 y 100
def generar_primos(numero_inferior, numero_superior):
    primos = []
    for num in range(numero_inferior, numero_superior + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos

# Paso 2: Función para generar un par de primos no repetido
def generar_par_no_repetido(primos, historial):
    intentos = 0
    while intentos < 1000:
        p1 = random.choice(primos)
        p2 = random.choice(primos)
        par = tuple(sorted((p1, p2)))
        if par not in historial:
            historial.append(par)
            if len(historial) > 10:
                historial.pop(0)
            return par
        intentos += 1
    raise Exception("No se pudo generar un par único después de muchos intentos.")

# Programa principal
if __name__ == "__main__":
    primos = generar_primos(1, 100)
    historial_pares = []

    # Ejemplo: generar 5 claves únicas
    for _ in range(5):
        par = generar_par_no_repetido(primos, historial_pares)
        clave = par[0] * par[1]
        print(f"Par primo generado: {par} → Clave de encriptación: {clave}")
