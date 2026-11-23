# Trabajo Práctico 3 — TDA

* **Alumno:** Sosa Darío Leandro
* **Padrón:** 113737
* **Curso:** Buchwald - Genender

## Preparación del entorno

1. Crear y activar un entorno virtual en la raíz del proyecto:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar las dependencias necesarias
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución del programa

El programa principal puede ejecutarse mediante `./tp3` o `python3 tp3.py`. Por defecto utiliza el algoritmo de **Backtracking** (`bt`), aunque se puede especificar otro enfoque mediante un segundo argumento opcional:

```bash
./tp3 <ruta/al/tablero.txt> [bt|pl|greedy|gringo]
```

O bien:

```bash
python3 tp3.py <ruta/al/tablero.txt> [bt|pl|greedy|gringo]
```

### Ejemplos de uso

```bash
# Ejecución por defecto (Backtracking)
./tp3 tests/3_3.txt

# Ejecución especificando otro algoritmo
python3 tp3.py tests/3_3.txt pl
python3 tp3.py tests/3_3.txt greedy
python3 tp3.py tests/3_3.txt gringo
```

*(ACLARACIÓN: En caso de que el ejecutable `./tp3` no tenga permisos, habilitarlo con `chmod +x tp3`).*

## Informe

El informe donde se abordan todos los puntos del TP se encuentra en [informe.pdf](./informe.pdf).