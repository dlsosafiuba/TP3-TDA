def greedy_juego_piedras(tablero):
    if not tablero:
        return []
    n, m = len(tablero), len(tablero[0])
    cubiertas = [False] * n
    piedras_removidas = []

    for j in range(m):
        v_j = 0
        c_j = 0
        for i in range(n):
            if not cubiertas[i]:
                if tablero[i][j] == 'V':
                    v_j += 1
                elif tablero[i][j] == 'C':
                    c_j += 1

        conservar = 'V' if v_j >= c_j else 'C'
        descartar = 'C' if conservar == 'V' else 'V'

        for i in range(n):
            if tablero[i][j] == conservar:
                cubiertas[i] = True
            elif tablero[i][j] == descartar:
                piedras_removidas.append((i, j))

    return piedras_removidas