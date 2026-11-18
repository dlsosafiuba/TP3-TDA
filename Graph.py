from matplotlib.pylab import seed
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import time
from contextlib import redirect_stdout
from io import StringIO

from src.AlgoritmoGreedy import eleccion_monedas
from src.ListCreator import lista_aleatoria
from tests import test_lista_aleatoria




def graficar_tiempo_ejecucion(n):
    plt.style.use('ggplot')
    
    tamanios = np.arange(500, n + 1, 10) 
    tiempos = []
    
    for tamanio in tamanios:
        with redirect_stdout(StringIO()):
            tiempo = test_lista_aleatoria(tamanio, tamanio, 10000)
        tiempos.append(tiempo)
        
    coeficientes = np.polyfit(tamanios, tiempos, 1)
    polinomio_lineal = np.poly1d(coeficientes)
    tiempos_predichos = polinomio_lineal(tamanios)
  

    fig, ax = plt.subplots(figsize=(18, 8))
    
    
    ax.plot(tamanios, tiempos, label='Tiempos empíricos', linewidth=2.5, alpha=0.7)
    
  
    etiqueta_recta = f"Ajuste lineal ($y = {coeficientes[0]:.2e}x + {coeficientes[1]:.2e}$)"
    ax.plot(tamanios, tiempos_predichos, label=etiqueta_recta, color='red', linestyle='--', linewidth=2)
    
    marcas_x = np.arange(500, n + 1, 100)
    ax.set_xticks(marcas_x)
    ax.tick_params(axis='x', labelrotation=45)
    
    ax.set(xlim=(500, n),
           xlabel='Cantidad de elementos del lista', 
           ylabel='Tiempo (segundos)',
           title='Tiempo de ejecución según el tamaño del lista vs Ajuste Lineal')
    

    ax.legend()
    
    plt.savefig("tiempo_ejecucion.png", dpi=300, bbox_inches='tight')

def graficar_varianza_tamanio_fijo(tamanio, iteraciones=500):
    plt.style.use('ggplot')
    
    tiempos = []
    lista_iteraciones = np.arange(1, iteraciones + 1)
    
    print(f"--- Ejecutando {iteraciones} veces para un lista de tamaño {tamanio} ---")
    
    for i in range(iteraciones):
        with redirect_stdout(StringIO()):
            tiempo = test_lista_aleatoria(tamanio, tamanio, 10000)
        tiempos.append(tiempo)
        
  
    fig, ax = plt.subplots(figsize=(14, 6))
    
   
    ax.plot(lista_iteraciones, tiempos, label='Tiempo de cada ejecución', color='blue', alpha=0.6, linewidth=1.5)
    
    
    tiempo_promedio = np.mean(tiempos)
    ax.axhline(y=tiempo_promedio, color='red', linestyle='--', linewidth=2, 
               label=f'Promedio ({tiempo_promedio:.6f} s)')
    
    ax.set(xlabel='Número de ejecución (Iteración)', 
           ylabel='Tiempo (segundos)',
           title=f'Variación de tiempo para un tamaño fijo (N = {tamanio})')
    
    ax.legend()
    
    plt.savefig("varianza_fija.png", dpi=300, bbox_inches='tight')
    print("¡Gráfico guardado como 'varianza_fija.png'!")
if __name__ == "__main__":
   graficar_varianza_tamanio_fijo(2000, 1000)

graficar_tiempo_ejecucion(1000)