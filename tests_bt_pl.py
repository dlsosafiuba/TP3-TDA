import random
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import src.ParserMatriz as pm
from scipy.optimize import curve_fit
from src.Backtracking import bt_juego_piedras
from src.Lineal import pl_juego_piedras

sns.set_theme(style="whitegrid")

def medir_tiempo_promedio(funcion, tableros):
    tiempos = []
    for tab in tableros:
        inicio = time.perf_counter()
        funcion(tab)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)


def modelo_exponencial(x, a, b):
    return a * (b ** x)


def ajustar_exponencial(x_datos, y_datos):
    x_arr = np.array(x_datos, dtype=float)
    y_arr = np.array(y_datos, dtype=float)
    popt, _ = curve_fit(modelo_exponencial, x_arr, y_arr, p0=[1e-6, 1.5], maxfev=10000)
    a, b = popt
    x_suave = np.linspace(min(x_arr), max(x_arr), 200)
    y_suave = modelo_exponencial(x_suave, a, b)
    etiqueta = f"Ajuste exp. ($y = {a:.2e} \\cdot {b:.2f}^m$)"
    return x_suave, y_suave, etiqueta


def ajustar_lineal(x_datos, y_datos):
    x_arr = np.array(x_datos, dtype=float)
    y_arr = np.array(y_datos, dtype=float)
    pendiente, ordenada = np.polyfit(x_arr, y_arr, 1)
    x_suave = np.linspace(min(x_arr), max(x_arr), 200)
    y_suave = pendiente * x_suave + ordenada
    etiqueta = f"Ajuste lineal ($y = {pendiente:.2e}n + {ordenada:.2e}$)"
    return x_suave, y_suave, etiqueta


def experimento_columnas(n_fijo=25, lista_m=None, repeticiones=30):
    if lista_m is None:
        lista_m = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    tiempos_bt = []
    tiempos_pl = []

    print(f"--- Experimento A: Variando columnas m (Filas = n={n_fijo}, {repeticiones} ejecuciones) ---")
    for m in lista_m:
        tableros = [
            pm.generar_tablero_aleatorio(n_fijo, m, seed=1000 * m + r)
            for r in range(repeticiones)
        ]

        t_bt = medir_tiempo_promedio(bt_juego_piedras, tableros)
        t_pl = medir_tiempo_promedio(pl_juego_piedras, tableros)

        tiempos_bt.append(t_bt)
        tiempos_pl.append(t_pl)
        print(f"m={m:2d} | BT: {t_bt:.5f}s | PL: {t_pl:.5f}s")

    xm_bt, yn_bt, lbl_m_bt = ajustar_exponencial(lista_m, tiempos_bt)
    xm_pl, yn_pl, lbl_m_pl = ajustar_exponencial(lista_m, tiempos_pl)

    plt.figure(figsize=(9, 5.5))
    plt.plot(lista_m, tiempos_bt, 'o-', color='#1f77b4', label='Backtracking')
    plt.plot(xm_bt, yn_bt, '--', color='#1f77b4', alpha=0.85, label=f'BT: {lbl_m_bt}')
    plt.plot(lista_m, tiempos_pl, 's-', color='#d62728', label='Prog. Lineal')
    plt.plot(xm_pl, yn_pl, '--', color='#d62728', alpha=0.85, label=f'PL: {lbl_m_pl}')
    plt.title(f'Tiempo de ejecución vs. Cantidad de columnas ($n={n_fijo}$ fijo)')
    plt.xlabel('Cantidad de columnas ($m$)')
    plt.ylabel('Tiempo promedio (segundos)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('tiempos_columnas.png', dpi=300)
    plt.show()


def experimento_filas(m_fijo=14, lista_n=None, repeticiones=30):
    if lista_n is None:
        lista_n = [10, 25, 50, 100, 150, 200, 300]

    tiempos_bt = []
    tiempos_pl = []

    print(f"\n--- Experimento B: Variando filas n (Columnas = m={m_fijo}, {repeticiones} ejecuciones) ---")
    for n in lista_n:
        tableros = [
            pm.generar_tablero_aleatorio(n, m_fijo, seed=2000 * n + r)
            for r in range(repeticiones)
        ]

        t_bt = medir_tiempo_promedio(bt_juego_piedras, tableros)
        t_pl = medir_tiempo_promedio(pl_juego_piedras, tableros)

        tiempos_bt.append(t_bt)
        tiempos_pl.append(t_pl)
        print(f"n={n:3d} | BT: {t_bt:.5f}s | PL: {t_pl:.5f}s")

    xn_bt, yn_bt, lbl_n_bt = ajustar_lineal(lista_n, tiempos_bt)
    xn_pl, yn_pl, lbl_n_pl = ajustar_lineal(lista_n, tiempos_pl)

    plt.figure(figsize=(9, 5.5))
    plt.plot(lista_n, tiempos_bt, 'o-', color='#1f77b4', label='Backtracking')
    plt.plot(xn_bt, yn_bt, '--', color='#1f77b4', alpha=0.85, label=f'BT: {lbl_n_bt}')
    plt.plot(lista_n, tiempos_pl, 's-', color='#d62728', label='Prog. Lineal')
    plt.plot(xn_pl, yn_pl, '--', color='#d62728', alpha=0.85, label=f'PL: {lbl_n_pl}')
    plt.title(f'Tiempo de ejecución vs. Cantidad de filas ($m={m_fijo}$ fijo)')
    plt.xlabel('Cantidad de filas ($n$)')
    plt.ylabel('Tiempo promedio (segundos)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('tiempos_filas.png', dpi=300)
    plt.show()

def experimento_cuadrados(lista_k=None, repeticiones=30):
    if lista_k is None:
        lista_k = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    tiempos_bt, tiempos_pl = [], []

    print(f"\n--- Experimento C: Tableros cuadrados k x k ({repeticiones} ejecuciones) ---")
    for k in lista_k:
        tableros = [
            pm.generar_tablero_aleatorio(k, k, seed=3000 * k + r)
            for r in range(repeticiones)
        ]

        t_bt = medir_tiempo_promedio(bt_juego_piedras, tableros)
        t_pl = medir_tiempo_promedio(pl_juego_piedras, tableros)

        tiempos_bt.append(t_bt)
        tiempos_pl.append(t_pl)
        print(f"{k:2d}x{k:<2d} | BT: {t_bt:.5f}s | PL: {t_pl:.5f}s")

    xk_bt, yk_bt, lbl_k_bt = ajustar_exponencial(lista_k, tiempos_bt)
    xk_pl, yk_pl, lbl_k_pl = ajustar_exponencial(lista_k, tiempos_pl)

    plt.figure(figsize=(9, 5.5))
    plt.plot(lista_k, tiempos_bt, 'o-', color='#1f77b4', label='Backtracking (empírico)')
    plt.plot(xk_bt, yk_bt, '--', color='#1f77b4', alpha=0.85, label=f'BT: {lbl_k_bt}')
    plt.plot(lista_k, tiempos_pl, 's-', color='#d62728', label='Prog. Lineal (empírico)')
    plt.plot(xk_pl, yk_pl, '--', color='#d62728', alpha=0.85, label=f'PL: {lbl_k_pl}')
    plt.title('Tiempo de ejecución vs. Dimensión de tablero cuadrado ($k \\times k$)')
    plt.xlabel('Dimensión $k$ (tablero $k \\times k$)')
    plt.ylabel('Tiempo promedio (segundos)')
    plt.xticks(lista_k, [f"{k}x{k}" for k in lista_k])
    plt.legend()
    plt.tight_layout()
    plt.savefig('tiempos_cuadrados.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    experimento_columnas(n_fijo=25, lista_m=[4, 6, 8, 10, 12, 14, 16, 18, 20], repeticiones=30)
    experimento_filas(m_fijo=14, lista_n=[10, 25, 50, 100, 150, 200, 300], repeticiones=30)
    experimento_cuadrados(lista_k=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], repeticiones=30)