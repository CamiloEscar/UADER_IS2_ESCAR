#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* Calcula el número de iteraciones de la conjetura de Collatz (2n+1) para *
#* números entre 1 y 10000.                                                *
#*-------------------------------------------------------------------------*

import matplotlib.pyplot as plt

def collatz_iterations(n):
    """
    Calcula el número de iteraciones necesarias para que el número n
    llegue a 1 según la conjetura de Collatz.
    :param n: El número inicial
    :return: El número de iteraciones.
    """
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

def generate_collatz_data(limit):
    """
    Genera los datos de Collatz para los números entre 1 y 'limit'.
    :param limit: El número máximo hasta donde se desea calcular
    :return: Dos listas: números iniciales y las iteraciones para cada uno.
    """
    numbers = []
    iterations = []
    for n in range(1, limit + 1):
        numbers.append(n)
        iterations.append(collatz_iterations(n))
    return numbers, iterations

# Generamos los datos para los números entre 1 y 10000
limit = 10000
numbers, iterations = generate_collatz_data(limit)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(iterations, numbers, color='blue', s=1, alpha=0.5)
plt.title('Conjetura de Collatz: Número de Iteraciones vs Número Inicial')
plt.xlabel('Número de Iteraciones')
plt.ylabel('Número Inicial')
plt.grid(True)
plt.show()

# Guardamos los resultados en un archivo de texto
with open('collatz_results.txt', 'w') as f:
    for n, iter_count in zip(numbers, iterations):
        f.write(f"{n}: {iter_count} iteraciones\n")
