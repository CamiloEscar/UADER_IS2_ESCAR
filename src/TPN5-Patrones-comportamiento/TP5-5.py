# Modifique el programa IS2_taller_memory.py para que la clase tenga la capacidad 
# de almacenar hasta 4 estados en el pasado y pueda recuperar los mismos en cualquier orden de ser necesario.
 
# El método undo deberá tener un argumento adicional indicando si se desea recuperar el inmediato anterior (0) y los anteriores a el (1,2,3).


import os

#*--------------------------------------------------------------------
#* Design pattern memento, modificado para soportar hasta 4 estados
#*--------------------------------------------------------------------

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def __init__(self):
        self.history = []

    def save(self, writer):
        # Guardar máximo 4 estados, eliminando el más antiguo si es necesario
        if len(self.history) == 4:
            self.history.pop(0)
        self.history.append(writer.save())

    def undo(self, writer, position=0):
        if len(self.history) == 0:
            print("No hay estados para recuperar.")
            return
        if position < 0 or position >= len(self.history):
            print(f"No hay suficiente historial para recuperar la posición {position}.")
            return
        # Se accede al estado contando desde el final (posición 0 es el último)
        index = -(position + 1)
        memento = self.history[index]
        writer.undo(memento)
        print(f"Se recuperó el estado en la posición {position}.")


if __name__ == '__main__':
    os.system("clear")
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    print("Estado 1")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Estado 2")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Estado 3")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Estado 4")
    writer.write("Material adicional III\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Estado 5 (sobre escribe el más viejo)")
    writer.write("Material adicional IV\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("\nSe recupera el último (posición 0):")
    caretaker.undo(writer, 0)
    print(writer.content + "\n")

    print("Se recupera el anterior (posición 1):")
    caretaker.undo(writer, 1)
    print(writer.content + "\n")

    print("Se recupera el segundo anterior (posición 2):")
    caretaker.undo(writer, 2)
    print(writer.content + "\n")

    print("Se recupera el tercero anterior (posición 3):")
    caretaker.undo(writer, 3)
    print(writer.content + "\n")

    print("Intento recuperar una posición inexistente (posición 4):")
    caretaker.undo(writer, 4)
