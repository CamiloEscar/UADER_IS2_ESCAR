# Cree una clase bajo el patrón cadena de responsabilidad donde los números del
# 1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que
# identifique la necesidad de consumir el número lo hará y caso contrario lo
# pasará al siguiente en la cadena. Implemente una clase que consuma números
# primos y otra números pares. Puede ocurrir que un número no sea consumido
# por ninguna clase en cuyo caso se marcará como no consumido.

class NumeroHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def procesar_numero(self, numero):
        if self.next_handler is not None:
            return self.next_handler.procesar_numero(numero)
        else:
            return f"El número {numero} no fue consumido."

class PrimoHandler(NumeroHandler):
    def procesar_numero(self, numero):
        if self.es_primo(numero):
            return f"PrimoHandler consumió el número {numero}."
        else:
            return super().procesar_numero(numero)

    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

class ParHandler(NumeroHandler):
    def procesar_numero(self, numero):
        if numero % 2 == 0:
            return f"ParHandler consumió el número {numero}."
        else:
            return super().procesar_numero(numero)

# Uso de la cadena de responsabilidad
def client_code():
    handler = PrimoHandler()
    handler.set_next(ParHandler())

    for numero in range(1, 101):
        resultado = handler.procesar_numero(numero)
        print(resultado)

if __name__ == '__main__':
    client_code()

# En este ejemplo, hemos creado dos clases, PrimoHandler y ParHandler, que heredan de la clase base NumeroHandler. 
# La clase PrimoHandler se encarga de consumir los números primos, mientras que la clase ParHandler consume los números pares. 
# Si un número no es consumido por ninguna clase, se pasa al siguiente en la cadena hasta llegar al final, donde se muestra un mensaje indicando que el número no fue consumido.

# En la función client_code(), creamos una instancia de PrimoHandler y establecemos ParHandler como el siguiente en la cadena utilizando el método set_next(). 
# Luego, iteramos del 1 al 100 y llamamos al método procesar_numero() en el handler inicial. El resultado se imprime en cada iteración.

