# Modifique el programa IS2_taller_scanner.py para que además la secuencia de barrido de radios que tiene incluya la sintonía de una serie de frecuencias
# memorizadas tanto de AM como de FM. Las frecuencias estarán etiquetadas como M1, M2, M3 y M4. Cada memoria podrá corresponder a una radio de AM
# o de FM en sus respectivas frecuencias específicas. En cada ciclo de barrido se barrerán las cuatro memorias

import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):
		
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)

#*--- Inicialmente en FM

		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()




#*---- sintonización de una serie de frecuencias memorizadas tanto de AM como de FM, etiquetadas como M1, M2, M3 y M4. 
# El programa realizará un ciclo de barrido que cubrirá todas las memorias en cada iteración

import time

def sintonizar_AM(frecuencia):
    print("Sintonizando AM en la frecuencia:", frecuencia)

def sintonizar_FM(frecuencia):
    print("Sintonizando FM en la frecuencia:", frecuencia)

def barrido_radios():
    memorias_AM = ["M1", "M2", "M3", "M4"]
    memorias_FM = ["M1", "M2", "M3", "M4"]
    
    for i in range(len(memorias_AM)):
        memoria_AM = memorias_AM[i]
        memoria_FM = memorias_FM[i]
        
        print("Barrido de memorias AM y FM:")
        print("Memoria AM:", memoria_AM)
        print("Memoria FM:", memoria_FM)
        
        sintonizar_AM(memoria_AM)
        time.sleep(1)  # Esperar 1 segundo entre sintonizaciones de AM
        
        sintonizar_FM(memoria_FM)
        time.sleep(1)  # Esperar 1 segundo entre sintonizaciones de FM

barrido_radios()

# se agregan dos listas memorias_AM y memorias_FM para almacenar las etiquetas de las frecuencias memorizadas tanto para AM como para FM. 
# En cada iteración del ciclo for, se obtienen las etiquetas de las memorias correspondientes para AM y FM.

# Luego, se realiza el barrido de las memorias AM y FM mediante la función sintonizar_AM() y sintonizar_FM(), respectivamente. 
# Se utiliza un retraso de 1 segundo entre cada sintonización para simular el proceso de cambio de frecuencia.
