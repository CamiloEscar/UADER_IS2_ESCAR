import sys
import os

MAX_RANGO = 65535

NUEVO = False # Cambiamos a true para usar la nueva clase

# ----------------------------------------------------------------------------

# Re-ingenieria

# Genere una clase “classPrimes” que implemente un método compute()
# devolviendo un valor lógico verdadero si el número pasado por argumento es
# primo. Para hacer la convergencia entre el programa original y su versión re
# factorizada utilice una estrategia “Branching by abstraction”.

class ClassPrimes:
    def __init__(self):
        return
        
    
    def compute(self, n):
        """Retorna True si n es un número primo, False en caso contrario."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1): # Optimización: hasta raíz cuadrada de n
            if n % i == 0:
                return False
        return True
    
    def obtener_primos_en_rango(self, inf, sup):
        """Devuelve una lista de números primos entre inf y sup (inclusive)."""
        return [n for n in range(inf, sup + 1) if self.compute(n)]
    
class BranchingByAbstraction:
    """Clase para manejar la abstraccion de la logica """
    def __init__(self):
        if NUEVO == True:
            self.pepe = ClassPrimes()
        
        return
    
    def obtener_primos_en_rango(self, inf, sup):
        if NUEVO == False:
            resultado = obtener_primos_en_rango(inf, sup)
            return resultado
        else:
            resultado = self.pepe.obtener_primos_en_rango(inf, sup)
            return resultado
                


# -------------------------------------------------------------------------------------------------------
def es_primo(n):
    """Retorna True si n es un número primo, False en caso contrario."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Optimización: hasta raíz cuadrada de n
        if n % i == 0:
            return False
    return True

def obtener_primos_en_rango(inf, sup):
    """Devuelve una lista de números primos entre inf y sup (inclusive)."""
    return [n for n in range(inf, sup + 1) if es_primo(n)]

def limpiar_pantalla():
    """Limpia la pantalla en forma multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_argumentos(args):
    """Valida que los argumentos de línea de comando sean enteros correctos y estén dentro del rango permitido."""
    if len(args) != 3:
        raise ValueError("Debe proporcionar exactamente dos argumentos: inicio y fin del rango.")
    
    try:
        inf = int(args[1])
        sup = int(args[2])
    except ValueError:
        raise ValueError("Ambos argumentos deben ser números enteros válidos.")
    
    if inf > sup:
        raise ValueError("El límite inferior no puede ser mayor que el superior.")
    if sup > MAX_RANGO:
        raise ValueError(f"El límite superior no puede exceder {MAX_RANGO}.")
    if inf < 0:
        raise ValueError("El límite inferior no puede ser negativo.")
    
    return inf, sup

def main():
    try:
        b = BranchingByAbstraction()
        inf, sup = validar_argumentos(sys.argv)
        limpiar_pantalla()
        print(f"Números primos entre {inf} y {sup} son:\n")
        primos = b.obtener_primos_en_rango(inf, sup)
        print(" ".join(map(str, primos)))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

