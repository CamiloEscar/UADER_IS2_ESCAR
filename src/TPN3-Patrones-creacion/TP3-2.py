# 2. Elabore una clase para el cálculo del valor de impuestos a ser utilizado por todas las clases que necesiten realizarlo. 
# El cálculo de impuestos simplificado deberá recibir un valor de importe base imponible y deberá retornar la suma
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre esa base imponible.

numero = int(input("Ingresa un valor para obtener el calculo de impuestos: "))

class CalculadoraImpuestos:
    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        ImpuestoTotal = iva + iibb + contribuciones
        return ImpuestoTotal

ci = CalculadoraImpuestos()
impuestos = ci.calcular_impuestos(numero)
print('El monto total de impuestos simplificados es de :',impuestos)
