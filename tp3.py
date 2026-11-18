import sys
from collections import deque
from src.AlgoritmoGreedy import eleccion_monedas
from src.ListCreator import leer_listatxt
from src.Printer import imprimir_resultados

def main(ruta_archivo):
    lista = leer_listatxt(ruta_archivo)
    copia = deque(lista)
    lista_sophia = []
    lista_mateo = []
    eleccion_monedas(lista, lista_sophia, lista_mateo)
    imprimir_resultados(copia, lista_sophia, lista_mateo)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta = sys.argv[1]
        main(ruta)
    else:
        print("Error: Tenés que pasar la ruta del archivo (Ej: python3 tp1.py <nombre_archivo>.txt)")