#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
getJason_v1.01.py - versión 1.1

Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

Este programa permite leer un archivo JSON y obtener el valor de una clave.
Si no se especifica una clave, se usa "token1" por defecto.
Aplica el patrón Singleton y controla todos los errores de forma segura.

Uso:
    python getJason_v1.01.py sitedata.json [clave]
    python getJason_v1.01.py -v
"""

import json
import sys
import os

VERSION = "1.1"

# (a) Aplicación de programación orientada a objetos.
# (b) Patrón Singleton implementado para asegurar única instancia de JsonReader.
class JsonReaderSingleton:
    """Clase Singleton para lectura de archivos JSON."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.json_data = {}

    def load_file(self, filepath):
        """Carga y valida un archivo JSON."""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"El archivo '{filepath}' no existe.")

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                self.json_data = json.load(file)
        except json.JSONDecodeError as json_error:
            raise ValueError(f"JSON inválido: {json_error}") from json_error
        except Exception as generic_error:
            raise RuntimeError(f"Error inesperado al leer el archivo: {generic_error}") from generic_error

    def get_value(self, key):
        """Retorna el valor de la clave o un mensaje si no existe."""
        return self.json_data.get(key, f"Clave '{key}' no encontrada.")


def print_usage():
    """Muestra cómo se debe usar el script."""
    print("Uso: python getJason_v1.01.py archivo.json [clave]")
    print("       python getJason_v1.01.py -v")


def main():
    """(c) Entrada principal con manejo robusto de argumentos."""

    try:
        args = sys.argv

        if len(args) == 2 and args[1] == "-v":
            # (g) Mostrar versión.
            print(f"getJason.py versión {VERSION}")
            return

        if len(args) < 2 or len(args) > 3:
            # (f) Validación robusta de argumentos.
            print("Error: número incorrecto de argumentos.")
            print_usage()
            return

        json_file = args[1]
        json_key = args[2] if len(args) == 3 else "token1"

        # (d) Branching by abstraction: se delega la lógica a una clase.
        reader = JsonReaderSingleton()
        reader.load_file(json_file)
        result = reader.get_value(json_key)
        print(result)

    except (FileNotFoundError, ValueError, RuntimeError) as controlled_error:
        # (f) Control de errores explícitos y esperados.
        print(f"Error: {controlled_error}")
    except Exception as unexpected:
        # Fallback para cualquier otro error no previsto.
        print(f"Error inesperado: {unexpected}")


if __name__ == "__main__":
    main()
