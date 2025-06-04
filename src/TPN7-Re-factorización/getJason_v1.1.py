#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
getJason_v1.1.py - versión argenta 1.1

Copyright UADER-FCyT-IS2©2024

Este programa te permite leer un archivo JSON y sacar el valor de una clave.
Si no pasás una clave, usa "token1" por defecto.
Aplica el patrón Singleton y maneja los errores como corresponde.

Uso:
    python getJason_v1.1.py datos.json [clave]
    python getJason_v1.1.py -v
"""

import json
import sys
import os

VERSION = "1.1"

class LectorJsonUnico:
    """Clase Singleton para leer un JSON sin repetir y sin soplar."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        self.datos_json = {}

    def cargar_archivo(self, ruta_archivo):
        """Carga el archivo JSON y lo valida."""
        if not os.path.isfile(ruta_archivo):
            raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe, maestro.")

        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                self.datos_json = json.load(archivo)
        except json.JSONDecodeError as error_json:
            raise ValueError(f"Che, el JSON está trucho: {error_json}") from error_json
        except Exception as error_generico:
            raise RuntimeError(f"Pasó algo inesperado al leer el archivo: {error_generico}") from error_generico

    def obtener_valor(self, clave):
        """Devuelve el valor de la clave o te avisa si no existe."""
        return self.datos_json.get(clave, f"Clave '{clave}' no encontrada, capo.")


def mostrar_uso():
    """Explica cómo se usa este script."""
    print("Uso: python getJason_v1.1.py datos.json [clave]")
    print("       python getJason_v1.1.py -v")


def main():
    """Punto de entrada al script, todo bajo control."""

    try:
        argumentos = sys.argv

        if len(argumentos) == 2 and argumentos[1] == "-v":
            print(f"getJason.py versión {VERSION}")
            return

        if len(argumentos) < 2 or len(argumentos) > 3:
            print("Error: pasaste mal los argumentos.")
            mostrar_uso()
            return

        archivo_json = argumentos[1]
        clave_json = argumentos[2] if len(argumentos) == 3 else "token1"

        lector = LectorJsonUnico()
        lector.cargar_archivo(archivo_json)
        resultado = lector.obtener_valor(clave_json)
        print(resultado)

    except (FileNotFoundError, ValueError, RuntimeError) as error_conocido:
        print(f"Error: {error_conocido}")
    except Exception as error_desconocido:
        print(f"Error inesperado: {error_desconocido}")


if __name__ == "__main__":
    main()
