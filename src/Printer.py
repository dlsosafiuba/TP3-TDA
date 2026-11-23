def imprimir_resultados(tablero, piedras_removidas, filas_cubiertas):
    if not tablero:
        return
    print("Tablero original:")
    for fila in tablero:
        print("[ " + " ".join(fila) + " ]")

    n = len(tablero)
    m = len(tablero[0])
    removidas_set = set(piedras_removidas)

    tablero_resultante = []
    for i in range(n):
        nueva_fila = []
        for j in range(m):
            if (i, j) in removidas_set:
                nueva_fila.append('.')
            else:
                nueva_fila.append(tablero[i][j])
        tablero_resultante.append(nueva_fila)

    colores_columna = []
    for j in range(m):
        color = '-'
        for i in range(n):
            if tablero_resultante[i][j] != '.':
                color = tablero_resultante[i][j]
        colores_columna.append(color)

    print("\nColores por columna:", " ".join(colores_columna))

    if piedras_removidas:
        print("Piedras removidas:", ", ".join(str(p) for p in piedras_removidas))
    else:
        print("Piedras removidas: -")

    print("\nTablero resultante:")
    for fila in tablero_resultante:
        print("[ " + " ".join(fila) + " ]")

    indices_vacias = [
        i for i in range(n) if all(celda == '.' for celda in tablero_resultante[i])
    ]
    cant_vacias = n - filas_cubiertas

    if cant_vacias > 0:
        print(f"\nFilas vacías: {cant_vacias} -> {indices_vacias}")
    else:
        print("\nFilas vacías: 0")