#!/usr/bin/env python3
import sys
from src.Backtracking import bt_juego_piedras
from src.Lineal import pl_juego_piedras
from src.Greedy import greedy_juego_piedras
from src.Probabilistico import gringo_juego_piedras
from src.ParserMatriz import cargar_tablero
from src.Printer import imprimir_resultados


def _contar_filas_cubiertas(tablero, piedras_removidas):
    removidas = set(piedras_removidas)
    cubiertas = 0
    for i, fila in enumerate(tablero):
        if any(celda != '.' and (i, j) not in removidas for j, celda in enumerate(fila)):
            cubiertas += 1
    return cubiertas

def _ejecutar_algoritmo(tablero, algoritmo):
    piedras_removidas, filas_cubiertas = None, None;

    if algoritmo == "bt":
        piedras_removidas, filas_cubiertas = bt_juego_piedras(tablero)
    elif algoritmo == "pl":
        piedras_removidas = pl_juego_piedras(tablero)
        filas_cubiertas = _contar_filas_cubiertas(tablero, piedras_removidas)
    elif algoritmo == "greedy":
        piedras_removidas = greedy_juego_piedras(tablero)
        filas_cubiertas = _contar_filas_cubiertas(tablero, piedras_removidas)
    elif algoritmo == "gringo":
        piedras_removidas = gringo_juego_piedras(tablero)
        filas_cubiertas = _contar_filas_cubiertas(tablero, piedras_removidas)
    else:
        print(f"Error: Algoritmo '{algoritmo}' no reconocido. Opciones: bt, pl, greedy, gringo.")

    return piedras_removidas, filas_cubiertas;


def main(ruta_archivo, algoritmo="bt"):
    tablero = cargar_tablero(ruta_archivo)
    piedras_removidas, filas_cubiertas = _ejecutar_algoritmo(tablero, algoritmo);
    if piedras_removidas != None and filas_cubiertas != None:
        print(f"Algoritmo elegido: {algoritmo}")
        imprimir_resultados(tablero, piedras_removidas, filas_cubiertas)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        ruta = sys.argv[1]
        modo = sys.argv[2].lower() if len(sys.argv) >= 3 else "bt"
        main(ruta, modo)
    else:
        print("Uso: python3 tp3.py <ruta_archivo.txt> [bt|pl|greedy|gringo](bt por defecto)")