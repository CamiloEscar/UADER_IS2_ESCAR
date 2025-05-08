# Implemente una clase que permita a un número cualquiera imprimir su valor, luego agregarle sucesivamente.
# a. Sumarle 2.
# b. Multiplicarle por 2.
# c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a las clases con las diferentes operaciones. 
# Use un patrón decorator para implementar.

class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):
        print("Valor actual:", self.valor)

    def operacion_decorator(self, operacion):
        def wrapper():
            operacion()
            self.imprimir_valor()

        return wrapper

    def sumar_dos(self):
        self.valor += 2

    def multiplicar_por_dos(self):
        self.valor *= 2

    def dividir_por_tres(self):
        self.valor /= 3


if __name__ == "__main__":
    numero = Numero(1)

    print("Sin operaciones:")
    numero.imprimir_valor()

    print("\nAplicando operaciones sumar_dos:")
    numero.sumar_dos()
    numero.imprimir_valor()
    print("\nAplicando operaciones multiplicar_por_dos:")
    numero.multiplicar_por_dos()
    numero.imprimir_valor()
    print("\nAplicando operaciones dividir_por_tres:")
    numero.dividir_por_tres()
    numero.imprimir_valor()