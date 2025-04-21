#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# AGREGADO DE COMENTARIOS
# ESCAR CAMILO

# iniciamos las variables
lower = 1
upper = 500

# imprimimos los numeros primos entre lower y upper
print("Prime numbers between", lower, "and", upper, "are:")

# iteramos sobre el rango de numeros entre lower y upper
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   
   # si el numero es divisible por algun numero menor que el mismo, no es primo
   if num > 1:
       # checamos si el numero es primo
       for i in range(2, num):
           # si el numero es divisible por algún numero, no es primo, salimos del loop
           if (num % i) == 0:
               break
           # si no se cumple la condicion anterior, el numero es primo, lo imprimimos
       else:
           print(num)

