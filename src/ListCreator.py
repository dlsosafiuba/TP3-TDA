import random
from collections import deque

def leer_listatxt(ruta_archivo):
    lista = []

    with open(ruta_archivo, "r") as f:
        next(f)  

        for linea in f:
            numeros = linea.strip().split(";")

            for numero in numeros:
                lista.append(int(numero))

    return deque(lista)

def lista_aleatoria(inicio, fin, max):
    n = random.randint(inicio, fin)
    lista = []
    for i in range(n):
        num = random.randint(1, max)
        lista.append(num)
        
    return deque(lista)