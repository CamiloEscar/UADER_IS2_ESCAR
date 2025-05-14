#3. Genere una clase donde se instancie una comida rápida “hamburguesa” que pueda ser entregada en mostrador, 
# retirada por el cliente o enviada por delivery. A los efectos prácticos bastará que la clase imprima el método de entrega.

class Hamburguesa:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def entrega_en_mostrador(self):
        print("La hamburguesa {} está lista para ser retirada en mostrador.".format(self.tipo))
    
    def entrega_al_cliente(self):
        print("La hamburguesa {} está lista para ser retirada por el cliente.".format(self.tipo))
    
    def entrega_a_domicilio(self):
        print("La hamburguesa {} será entregada por delivery en breve.".format(self.tipo))

Hamb = input("Como quiere su hamburguesa?: ")
mi_hamburguesa = Hamburguesa(Hamb)

print('listo')
mi_hamburguesa.entrega_en_mostrador()
print('o') 
mi_hamburguesa.entrega_al_cliente() 
print()
mi_hamburguesa.entrega_a_domicilio() 
