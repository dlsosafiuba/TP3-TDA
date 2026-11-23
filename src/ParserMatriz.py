import random

def cargar_tablero(ruta_archivo):
    tablero = []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            if linea_limpia and not linea_limpia.startswith('#'):
                tablero.append(list(linea_limpia))
    return tablero


def generar_tablero_aleatorio(n, m, seed=None):
    rng = random.Random(seed)
    return [
        rng.choices(['V', 'C', '.'], weights=[0.10, 0.10, 0.80], k=m)
        for _ in range(n)
    ]