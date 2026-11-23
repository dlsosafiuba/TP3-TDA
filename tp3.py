import sys
from collections import deque
from src.Backtracking import _bt_juego_piedras
from src.ParserMatriz import cargar_tablero
from src.Printer import imprimir_resultados

def main(ruta_archivo):
    tablero = cargar_tablero(ruta_archivo)
    piedras_removidas, filas_cubiertas = _bt_juego_piedras(tablero)
    imprimir_resultados(tablero, piedras_removidas, filas_cubiertas)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta = sys.argv[1]
        main(ruta)
    else:
        print("Error: Tenés que pasar la ruta del archivo (Ej: python3 tp1.py <nombre_archivo>.txt)")