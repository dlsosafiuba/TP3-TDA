from src.AlgoritmoGreedy import eleccion_monedas
from src.ListCreator import lista_aleatoria
from src.Printer import imprimir_resultados
from collections import deque
import time

def test_lista_aleatoria(min_tamanio, max_tamanio, max_num):
    lista = lista_aleatoria(min_tamanio, max_tamanio, max_num)
    copia = deque(lista)
    lista_sophia, lista_mateo = [], []

    inicio = time.perf_counter()
    eleccion_monedas(lista, lista_sophia, lista_mateo)
    tiempo = time.perf_counter() - inicio
    imprimir_resultados(copia, lista_sophia, lista_mateo)
    return tiempo

tmp = 0
#Caso: 1 moneda, monedas del 1 al 10
tmp = test_lista_aleatoria(1, 1, 10)
print(tmp)
#Caso: 2 monedas, monedas del 1 al 10
tmp= test_lista_aleatoria(2, 2, 10)
print(tmp)
#Caso: 3 monedas, monedas del 1 al 10
tmp = test_lista_aleatoria(3, 3, 10)
print(tmp)
#Caso: 5 monedas, monedas del 1 al 10
tmp = test_lista_aleatoria(5, 5, 10)
print(tmp)
#Caso: 5 monedas, monedas del 1 al 1000
tmp = test_lista_aleatoria(5, 5, 10000)
print(tmp)
#Caso: 10 monedas, monedas del 1 al 10
tmp = test_lista_aleatoria(10, 10, 10)
print(tmp)
#Caso: 10 monedas, monedas del 1 al 10000
tmp = test_lista_aleatoria(10, 10, 10000)
print(tmp)