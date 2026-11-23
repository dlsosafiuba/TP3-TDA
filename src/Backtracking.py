def _busqueda_solucion(tablero, col, filas_cubiertas):
    if col == len(tablero[0]):
        return [], sum(filas_cubiertas)
    
    verdes = []
    celestes = []
    v_filas_cubiertas = filas_cubiertas.copy()
    c_filas_cubiertas = filas_cubiertas.copy()

    for fil in range(0, len(tablero)):
        if(tablero[fil][col] == 'V'):
            verdes.append((fil, col))
            if v_filas_cubiertas[fil] == 0:
                v_filas_cubiertas[fil] += 1

        if(tablero[fil][col] == 'C'):
            celestes.append((fil, col))
            if c_filas_cubiertas[fil] == 0:
                c_filas_cubiertas[fil] += 1

    sol_sin_v, cubiertas_sin_v = _busqueda_solucion(tablero, col + 1, c_filas_cubiertas)
    if cubiertas_sin_v == len(tablero):
        return verdes + sol_sin_v, cubiertas_sin_v
    sol_sin_c, cubiertas_sin_c = _busqueda_solucion(tablero, col + 1, v_filas_cubiertas)
    if cubiertas_sin_c == len(tablero):
        return celestes + sol_sin_c, cubiertas_sin_c

    if cubiertas_sin_c >= cubiertas_sin_v:
        return celestes + sol_sin_c, cubiertas_sin_c
    return verdes + sol_sin_v, cubiertas_sin_v

def bt_juego_piedras(tablero):
    return _busqueda_solucion(tablero, 0, [0] * len(tablero))
