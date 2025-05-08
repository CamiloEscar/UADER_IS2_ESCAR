# Provea una clase ping que luego de creada al ser invocada con un método“execute(string)” 
# realice 10 intentos de ping a la dirección IP contenida en “string” (argumento pasado), 
# la clase solo debe funcionar si la dirección IP provista comienza con “192.”. 
# Provea un método executefree(string) que haga lo mismo pero sin el control de dirección. 
# Ahora provea una clase ping proxy cuyo método execute(string) si la dirección es “192.168.0.254” 
# realice un ping a www.google.com usando el método executefree de ping y re-envie a execute
# de la clase ping en cualquier otro caso. (Modele la solución como un patrón proxy).

from abc import ABC, abstractmethod
import os

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")

    def execute(self, address):
        if address.startswith("192."):
            for _ in range(10):
                response = os.system("ping -c 1 " + address)
                if response == 0:
                    print(f"Ping to {address} successful.")
                else:
                    print(f"Ping to {address} failed.")
        else:
            print("Invalid IP address.")

    def executefree(self, address):
        for _ in range(10):
            response = os.system("ping -c 1 " + address)
            if response == 0:
                print(f"Ping to {address} successful.")
            else:
                print(f"Ping to {address} failed.")

def client_code(subject: Subject) -> None:
    subject.request()
    def __init__(self):
        self.RealSubject = RealSubject()

    def execute(self, address):
        if address == "192.168.0.254":
            self.RealSubject.executefree("www.google.com")
        else:
            self.RealSubject.execute(address)

# Uso del patrón Proxy
proxy = RealSubject()
proxy.execute("192.168.0.1")  # Ejecuta el ping a la dirección IP 192.168.0.1 usando Ping
proxy.execute("192.168.0.254")  # Ejecuta el ping a www.google.com usando Ping.executefree
proxy.execute("10.0.0.1")  # IP no válida, se imprime un mensaje de error
