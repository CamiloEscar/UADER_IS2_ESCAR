# 4. Implemente una clase “factura” que tenga un importe correspondiente al total de la factura pero de acuerdo 
# a la condición impositiva del cliente (IVA Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal condición. 

class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva
    
    def calcular_iva(self):
        if self.condicion_impositiva == "Responsable Inscripto":
            return self.importe * 0.21
        elif self.condicion_impositiva == "No Inscripto":
            return 0
        elif self.condicion_impositiva == "Exento":
            return 0
        else:
            raise ValueError("La condición impositiva ingresada no es válida.")
    
    def imprimir_factura(self):
        iva = self.calcular_iva()
        total = self.importe + iva
        print("Factura")
        print("Importe: ${:.2f}".format(self.importe))
        print("Condición impositiva: {}".format(self.condicion_impositiva))
        print("IVA: ${:.2f}".format(iva))
        print("Total: ${:.2f}".format(total))

print()
numero = int(input("Ingrese un importe: "))

mi_factura = Factura(numero, "Responsable Inscripto")
mi_factura1 = Factura(numero, "No Inscripto")
mi_factura2 = Factura(numero, "Exento")

print()
mi_factura.imprimir_factura()
print()
mi_factura1.imprimir_factura()
print()
mi_factura2.imprimir_factura()
print()

