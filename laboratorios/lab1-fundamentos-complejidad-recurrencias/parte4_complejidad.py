import time
from pathlib import Path
from typing import Callable, Dict, List, Tuple

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS: List[int] = [100, 200, 400, 800, 1600, 3200, 6400]
RUTA_GRAFICAS = Path(__file__).parent / "graficas"

# Repeticiones para promediar las mediciones (consistente con Parte 3)
REPETICIONES: int = 5


def medir_algoritmo(algoritmo: Callable[[List[int]], Tuple[List[int], int]], datos: List[int]) -> float:
    """Mide una única ejecución del algoritmo sobre `datos` y devuelve el tiempo en segundos."""
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio


def medir_promediado(algoritmo: Callable[[List[int]], Tuple[List[int], int]], datos: List[int], repeticiones: int = REPETICIONES) -> float:
    """Ejecuta `algoritmo` varias veces sobre copias de `datos` y devuelve el tiempo promedio."""
    tiempos: List[float] = []
    for _ in range(repeticiones):
        tiempos.append(medir_algoritmo(algoritmo, datos.copy()))
    return sum(tiempos) / len(tiempos)


def ejecutar_experimento() -> Dict[str, List[float]]:
    """Ejecuta las mediciones para Insertion y Merge usando datos aleatorios.

    Devuelve un diccionario con listas de tiempos promediados por tamaño.
    """
    resultados: Dict[str, List[float]] = {"insertion": [], "merge": []}

    for n in TAMANOS:
        datos = generar_aleatorio(n, semilla=42)

        tiempo_insertion = medir_promediado(insertion_sort, datos, repeticiones=REPETICIONES)
        tiempo_merge = medir_promediado(merge_sort, datos, repeticiones=REPETICIONES)

        resultados["insertion"].append(tiempo_insertion)
        resultados["merge"].append(tiempo_merge)

        print(f"n={n} | Insertion avg={tiempo_insertion:.6f} s | Merge avg={tiempo_merge:.6f} s")

    return resultados


def graficar_tiempos(resultados: Dict[str, List[float]]) -> None:
    """Genera y guarda la gráfica comparativa de tiempos para ambos algoritmos."""
    plt.figure(figsize=(10, 6))

    plt.plot(TAMANOS, resultados["insertion"], marker="o", label="Insertion Sort")
    plt.plot(TAMANOS, resultados["merge"], marker="o", label="Merge Sort")

    plt.title("Comparación de tiempo: Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(RUTA_GRAFICAS / "parte4_tiempo.png", dpi=150)
    plt.close()


def main() -> None:
    resultados = ejecutar_experimento()
    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()