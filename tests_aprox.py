import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import src.ParserMatriz as pm
from src.Backtracking import bt_juego_piedras
from src.Greedy import greedy_juego_piedras
from src.Probabilistico import gringo_juego_piedras

sns.set_theme(style="whitegrid")


def contar_filas_cubiertas(tablero, piedras_removidas):
    removidas = {tuple(p) for p in piedras_removidas}
    cubiertas = 0
    for i, fila in enumerate(tablero):
        if any(celda != '.' and (i, j) not in removidas for j, celda in enumerate(fila)):
            cubiertas += 1
    return cubiertas


def contar_filas_no_vacias_iniciales(tablero):
    return sum(1 for fila in tablero if any(celda != '.' for celda in fila))


def experimento_cota_con_optimo(lista_k=None, repeticiones=30):
    if lista_k is None:
        lista_k = [4, 6, 8, 10, 12, 14, 16, 18]

    filas_bt = []
    filas_gringo = []
    filas_greedy = []
    ratios_gringo = []
    ratios_greedy = []

    print(f"--- Experimento 1: Verificación de r(A) contra Backtracking ({repeticiones} ejecuciones) ---")
    for k in lista_k:
        z_k, ag_k, agr_k = [], [], []
        r_gringo_k, r_greedy_k = [], []

        for r in range(repeticiones):
            tab = pm.generar_tablero_aleatorio(k, k, seed=1000 * k + r)

            _, z_opt = bt_juego_piedras(tab)
            sol_gringo = gringo_juego_piedras(tab, seed=5000 * k + r)
            sol_greedy = greedy_juego_piedras(tab)

            a_gringo = contar_filas_cubiertas(tab, sol_gringo)
            a_greedy = contar_filas_cubiertas(tab, sol_greedy)

            z_k.append(z_opt)
            ag_k.append(a_gringo)
            agr_k.append(a_greedy)

            if a_gringo > 0 and a_greedy > 0:
                r_gringo_k.append(z_opt / a_gringo)
                r_greedy_k.append(z_opt / a_greedy)

        filas_bt.append(sum(z_k) / len(z_k))
        filas_gringo.append(sum(ag_k) / len(ag_k))
        filas_greedy.append(sum(agr_k) / len(agr_k))

        prom_gringo = sum(r_gringo_k) / len(r_gringo_k)
        prom_greedy = sum(r_greedy_k) / len(r_greedy_k)
        ratios_gringo.append(prom_gringo)
        ratios_greedy.append(prom_greedy)

        print(
            f"{k:2d}x{k:<2d} | BT: {filas_bt[-1]:.2f} | Greedy: {filas_greedy[-1]:.2f} | Gringo: {filas_gringo[-1]:.2f} "
            f"|| z/Gringo: {prom_gringo:.4f} | z/Greedy: {prom_greedy:.4f}"
        )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5.5))

    ax1.plot(lista_k, filas_bt, '^-', color='#1f77b4', linewidth=2.2, label='Backtracking (Óptimo $z(I)$)')
    ax1.plot(lista_k, filas_greedy, 's-', color='#2ca02c', label='Greedy ($A_{\\mathrm{Greedy}}(I)$)')
    ax1.plot(lista_k, filas_gringo, 'o-', color='#ff7f0e', label='Gringo Hinz ($A_{\\mathrm{Gringo}}(I)$)')
    ax1.set_title('Filas cubiertas promedio: Óptimo vs. Aproximaciones')
    ax1.set_xlabel('Dimensión del tablero ($k \\times k$)')
    ax1.set_ylabel('Cantidad de filas cubiertas')
    ax1.set_xticks(lista_k)
    ax1.set_xticklabels([f"{k}x{k}" for k in lista_k])
    ax1.legend()

    ax2.plot(lista_k, ratios_gringo, 'o-', color='#ff7f0e', label='Gringo Hinz ($z(I) / A_{\\mathrm{Gringo}}(I)$)')
    ax2.plot(lista_k, ratios_greedy, 's-', color='#2ca02c', label='Greedy ($z(I) / A_{\\mathrm{Greedy}}(I)$)')
    ax2.axhline(2.0, color='#d62728', linestyle='--', linewidth=1.8, label='Cota teórica $r(A) = 2$')
    ax2.axhline(1.0, color='#1f77b4', linestyle=':', linewidth=1.8, label='Backtracking (Óptimo $r = 1$)')
    ax2.set_title('Relación de aproximación empírica $z(I) / A(I)$')
    ax2.set_xlabel('Dimensión del tablero ($k \\times k$)')
    ax2.set_ylabel('Cociente $z(I) / A(I)$')
    ax2.set_xticks(lista_k)
    ax2.set_xticklabels([f"{k}x{k}" for k in lista_k])
    ax2.set_ylim(0.8, 2.2)
    ax2.legend()

    plt.tight_layout()
    plt.savefig('aprox_cota_optimo.png', dpi=300)
    plt.show()


def experimento_volumenes_grandes(m_fijo=12, lista_n=None, repeticiones=20):
    if lista_n is None:
        lista_n = [500, 1000, 2500, 5000, 7500, 10000]

    ratios_cota_gringo = []
    ratios_cota_greedy = []
    tiempos_gringo = []
    tiempos_greedy = []

    print(f"\n--- Experimento 2: Volúmenes grandes (m={m_fijo} fijo, n hasta {max(lista_n)}) ---")
    for n in lista_n:
        rc_gringo_k, rc_greedy_k = [], []
        t_gringo_k, t_greedy_k = [], []

        for r in range(repeticiones):
            tab = pm.generar_tablero_aleatorio(n, m_fijo, seed=9000 * n + r)
            n_prima = contar_filas_no_vacias_iniciales(tab)

            t0 = time.perf_counter()
            sol_gringo = gringo_juego_piedras(tab, seed=7000 * n + r)
            t_gringo_k.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            sol_greedy = greedy_juego_piedras(tab)
            t_greedy_k.append(time.perf_counter() - t0)

            a_gringo = contar_filas_cubiertas(tab, sol_gringo)
            a_greedy = contar_filas_cubiertas(tab, sol_greedy)

            if a_gringo > 0 and a_greedy > 0:
                rc_gringo_k.append(n_prima / a_gringo)
                rc_greedy_k.append(n_prima / a_greedy)

        prom_rc_gringo = sum(rc_gringo_k) / len(rc_gringo_k)
        prom_rc_greedy = sum(rc_greedy_k) / len(rc_greedy_k)
        prom_t_gringo = sum(t_gringo_k) / len(t_gringo_k)
        prom_t_greedy = sum(t_greedy_k) / len(t_greedy_k)

        ratios_cota_gringo.append(prom_rc_gringo)
        ratios_cota_greedy.append(prom_rc_greedy)
        tiempos_gringo.append(prom_t_gringo)
        tiempos_greedy.append(prom_t_greedy)

        print(
            f"n={n:5d} | n'/Gringo: {prom_rc_gringo:.4f} | n'/Greedy: {prom_rc_greedy:.4f} "
            f"| t_Gringo: {prom_t_gringo:.5f}s | t_Greedy: {prom_t_greedy:.5f}s"
        )

    plt.figure(figsize=(9, 5.5))
    plt.plot(lista_n, ratios_cota_gringo, 'o-', color='#ff7f0e', label="Gringo Hinz ($n' / A_{\\mathrm{Gringo}}(I)$)")
    plt.plot(lista_n, ratios_cota_greedy, 's-', color='#2ca02c', label="Greedy ($n' / A_{\\mathrm{Greedy}}(I)$)")
    plt.axhline(2.0, color='#d62728', linestyle='--', linewidth=1.8, label='Cota teórica $r(A) = 2$')
    plt.axhline(1.0, color='gray', linestyle=':', linewidth=1.2, label="Cota ideal ($n' / A(I) = 1$)")

    plt.title(f"Corroboración de $r(A)$ en volúmenes grandes ($m={m_fijo}$ fijo, usando $z(I) \\leq n'$)")
    plt.xlabel('Cantidad de filas ($n$)')
    plt.ylabel("Relación acotada $n' / A(I)$")
    plt.ylim(0.8, 2.2)
    plt.legend()
    plt.tight_layout()
    plt.savefig('aprox_volumenes_grandes.png', dpi=300)
    plt.show()

    n_arr = np.array(lista_n, dtype=float)
    m_gringo, b_gringo = np.polyfit(n_arr, tiempos_gringo, 1)
    m_greedy, b_greedy = np.polyfit(n_arr, tiempos_greedy, 1)
    n_suave = np.linspace(min(n_arr), max(n_arr), 200)

    plt.figure(figsize=(9, 5.5))
    plt.plot(lista_n, tiempos_gringo, 'o-', color='#ff7f0e', label='Gringo Hinz')
    plt.plot(n_suave, m_gringo * n_suave + b_gringo, '--', color='#ff7f0e', alpha=0.85,
             label=f'Gringo: ajuste lineal ($y={m_gringo:.2e}n + {b_gringo:.2e}$)')
    plt.plot(lista_n, tiempos_greedy, 's-', color='#2ca02c', label='Greedy')
    plt.plot(n_suave, m_greedy * n_suave + b_greedy, '--', color='#2ca02c', alpha=0.85,
             label=f'Greedy: ajuste lineal ($y={m_greedy:.2e}n + {b_greedy:.2e}$)')

    plt.title(f'Tiempos de ejecución en volúmenes grandes ($m={m_fijo}$ fijo)')
    plt.xlabel('Cantidad de filas ($n$)')
    plt.ylabel('Tiempo promedio (segundos)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('aprox_tiempos.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    experimento_cota_con_optimo(lista_k=[4, 6, 8, 10, 12, 14, 16, 18], repeticiones=30)
    experimento_volumenes_grandes(m_fijo=12, lista_n=[500, 1000, 2500, 5000, 7500, 10000], repeticiones=20)