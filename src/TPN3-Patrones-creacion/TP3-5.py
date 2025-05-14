# 5. Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar para construir aviones en lugar de vehículos. 
# Para simplificar suponga que un avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.


class Body:
    def __init__(self):
        print("Se construyó el body del avión.")


class Turbina:
    def __init__(self):
        print("Se construyó una turbina del avión.")


class Alas:
    def __init__(self):
        print("Se construyó un ala del avión.")


class TrenAterrizaje:
    def __init__(self):
        print("Se construyó el tren de aterrizaje del avión.")


class Avion:
    def __init__(self):
        self.body = Body()
        self.Turbina_1 = Turbina()
        self.Turbina_2 = Turbina()
        self.Alas_1 = Alas()
        self.Alas_2 = Alas()
        self.TrenAterrizaje = TrenAterrizaje()
        print("Se construyó un avión completo.")

mi_avion = Avion()

