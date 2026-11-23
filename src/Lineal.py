import pulp

def pl_juego_piedras(tablero):
    if not tablero:
        return []
    n, m = len(tablero), len(tablero[0])

    prob = pulp.LpProblem("Juego_de_Piedras", pulp.LpMaximize)
    X = [pulp.LpVariable(f"X_{j}", cat="Binary") for j in range(m)]
    F = [pulp.LpVariable(f"F_{i}", cat="Binary") for i in range(n)]

    prob += pulp.lpSum(F)
    for i in range(n):
        prob += F[i] <= (
            pulp.lpSum(X[j] for j in range(m) if tablero[i][j] == 'V') +
            pulp.lpSum(1 - X[j] for j in range(m) if tablero[i][j] == 'C')
        )

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    piedras_removidas = []
    for j in range(m):
        val = pulp.value(X[j])
        descartar = 'C' if (val is not None and val > 0.5) else 'V'
        for i in range(n):
            if tablero[i][j] == descartar:
                piedras_removidas.append((i, j))

    return piedras_removidas