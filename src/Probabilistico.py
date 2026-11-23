import random

def gringo_juego_piedras(tablero, seed=None):
    if not tablero:
        return []
    n, m = len(tablero), len(tablero[0])
    rng = random.Random(seed)
    piedras_removidas = []

    for j in range(m):
        conservar = rng.choice(['V', 'C'])
        descartar = 'C' if conservar == 'V' else 'V'
        for i in range(n):
            if tablero[i][j] == descartar:
                piedras_removidas.append((i, j))

    return piedras_removidas