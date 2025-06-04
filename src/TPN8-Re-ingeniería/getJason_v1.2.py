#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
getJason_v1.2.py - versión argenta

Copyright UADER-FCyT-IS2©2024

Este programa automatiza la selección de cuenta bancaria (token) para pagos,
basándose en el saldo y utilizando patrones de diseño:
- Singleton para lectura del archivo JSON.
- Chain of Responsibility para ruteo de pagos.
- Iterator para listado de pagos.

Uso:
    python getJason_v1.2.py archivo.json [clave]
    python getJason_v1.2.py -v
"""

import json
import sys
import os
from datetime import datetime

VERSION = "1.2"

class LectorJsonSingleton:
    """Singleton para cargar datos JSON desde archivo."""
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.datos_json = {}
        return cls._instancia

    def cargar_archivo(self, ruta):
        """Carga y valida un archivo JSON."""
        if not os.path.isfile(ruta):
            raise FileNotFoundError(f"El archivo '{ruta}' no existe.")

        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                self.datos_json = json.load(archivo)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON inválido: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Error al leer el archivo: {e}") from e

    def obtener_valor(self, clave):
        """Devuelve el valor de una clave."""
        return self.datos_json.get(clave, f"Clave '{clave}' no encontrada.")


class Pago:
    """Representa un pago realizado."""
    def __init__(self, nro_pedido, token, monto):
        self.nro_pedido = nro_pedido
        self.token = token
        self.monto = monto
        self.fecha_hora = datetime.now()

    def __str__(self):
        return f"[{self.fecha_hora}] Pedido {self.nro_pedido} - Token: {self.token} - Monto: ${self.monto}"


class IteradorPagos:
    """Iterador para listar pagos realizados."""
    def __init__(self, lista_pagos):
        self._pagos = lista_pagos
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < len(self._pagos):
            pago = self._pagos[self._indice]
            self._indice += 1
            return pago
        raise StopIteration


class BancoHandler:
    """Manejador base para bancos con saldo."""
    def __init__(self, token, saldo_inicial):
        self.token = token
        self.saldo = saldo_inicial
        self.siguiente = None

    def set_siguiente(self, siguiente):
        """Setea el siguiente banco en la cadena."""
        self.siguiente = siguiente

    def procesar_pago(self, nro_pedido, monto, lista_pagos, lector):
        """Procesa o delega el pago."""
        if self.saldo >= monto:
            self.saldo -= monto
            lista_pagos.append(Pago(nro_pedido, self.token, monto))
        elif self.siguiente:
            self.siguiente.procesar_pago(nro_pedido, monto, lista_pagos, lector)
        else:
            print(f"Pedido {nro_pedido}: saldo insuficiente en todas las cuentas.")


class ProcesadorDePagos:
    """Se encarga de coordinar la cadena de bancos."""
    def __init__(self, lector):
        self.lector = lector
        self.pagos = []

        self.banco1 = BancoHandler("token1", 1000)
        self.banco2 = BancoHandler("token2", 2000)

        self.banco1.set_siguiente(self.banco2)
        self.banco2.set_siguiente(self.banco1)  # alternancia

        self.turno = self.banco1

    def hacer_pago(self, nro_pedido, monto):
        """Manda un pago a procesar, alternando banco."""
        self.turno.procesar_pago(nro_pedido, monto, self.pagos, self.lector)
        self.turno = self.turno.siguiente

    def mostrar_pagos(self):
        """Imprime los pagos hechos."""
        for pago in IteradorPagos(self.pagos):
            print(pago)


def imprimir_uso():
    """Muestra cómo se usa el script."""
    print("Uso: python getJason_v1.2.py archivo.json [clave]")
    print("     python getJason_v1.2.py -v")


def main():
    """Entrada principal del programa."""
    try:
        args = sys.argv

        if len(args) == 2 and args[1] == "-v":
            print(f"getJason.py versión {VERSION}")
            return

        if len(args) < 2 or len(args) > 3:
            print("Error: número de argumentos incorrecto.")
            imprimir_uso()
            return

        archivo_json = args[1]
        clave_json = args[2] if len(args) == 3 else "token1"

        lector = LectorJsonSingleton()
        lector.cargar_archivo(archivo_json)
        print(f"Clave '{clave_json}':", lector.obtener_valor(clave_json))

        print("\n--- Simulación de pagos ---")
        procesador = ProcesadorDePagos(lector)

        for i in range(1, 6):
            procesador.hacer_pago(nro_pedido=i, monto=500)

        print("\n--- Listado de pagos ---")
        procesador.mostrar_pagos()

    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
