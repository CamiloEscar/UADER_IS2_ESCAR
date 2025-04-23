# 1. Provea una clase que dado un número entero cualquiera retorne el factorial del mismo, 
# debe asegurarse que todas las clases que lo invoquen utilicen la misma instancia de clase

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# class SingletonFact(metaclass = SingletonMeta):
#     def getfact(self,n):
#         if n == 0:
#             return 1
#         else:
#             return n * self.getfact(n-1)

class Factorial:
    __instance = None
    
    def __init__(self):
        if Factorial.__instance is not None:
            raise Exception
        Factorial.__instance = self
    
    def get_instance():
        if Factorial.__instance is None:
            Factorial()
        return Factorial.__instance
    
    def getfact(self, n):
        if n == 0:
            return 1
        else:
            return n * self.getfact(n-1)

numero = int(input("Ingresa un número entero: "))

f = Factorial.get_instance()
print("su factorial es de:",f.getfact(numero)) 



