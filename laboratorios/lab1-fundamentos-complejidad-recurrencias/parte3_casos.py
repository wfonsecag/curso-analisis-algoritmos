import time
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


"""Script de medición para la Parte 3.

Contiene funciones con docstrings y anotaciones de tipo. Las mediciones se
realizan actualmente una vez por tamaño; la repetición y promediado se
implementará en el siguiente paso.
"""

TAMANOS: List[int] = [100, 200, 400, 800, 1600, 3200, 6400]
RUTA_GRAFICAS = Path(__file__).parent / "graficas"


def medir_insertion(datos: List[int]) -> Tuple[float, int]:
    """Mide el tiempo de ejecución de `insertion_sort` sobre `datos`.

    Args:
        datos: Lista de enteros de entrada para la medición.

    Returns:
        Tupla `(tiempo_segundos, comparaciones)` donde `comparaciones` es el
        número de comparaciones entre elementos reportado por el algoritmo.
    """
    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    return fin - inicio, comparaciones


def ejecutar_experimento() -> Dict[str, Dict[str, List[float]]]:
    """Ejecuta el experimento para los tres escenarios y devuelve resultados.

    Resultado con la estructura:
    {
        "aleatorio": {"tiempos": [...], "comparaciones": [...]},
        "casi_ordenado": {...},
        "inverso": {...},
    }
    """
    resultados: Dict[str, Dict[str, List[float]]] = {
        "aleatorio": {"tiempos": [], "comparaciones": []},
        "casi_ordenado": {"tiempos": [], "comparaciones": []},
        "inverso": {"tiempos": [], "comparaciones": []},
    }

    for n in TAMANOS:
        escenarios = {
            "aleatorio": generar_aleatorio(n, semilla=42),
            "casi_ordenado": generar_casi_ordenado(n, semilla=42),
            "inverso": generar_inverso(n),
        }

        for nombre, datos in escenarios.items():
            tiempo, comparaciones = medir_insertion(datos)

            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)

            print(
                f"n={n} | {nombre} | "
                f"tiempo={tiempo:.6f} s | "
                f"comparaciones={comparaciones}"
            )

    return resultados


def graficar_comparaciones(resultados: Dict[str, Dict[str, List[float]]]) -> None:
    """Genera y guarda la gráfica de comparaciones por tamaño para los 3 escenarios."""
    plt.figure(figsize=(10, 6))

    plt.plot(TAMANOS, resultados["aleatorio"]["comparaciones"], marker="o", label="Aleatorio")
    plt.plot(TAMANOS, resultados["casi_ordenado"]["comparaciones"], marker="o", label="Casi ordenado")
    plt.plot(TAMANOS, resultados["inverso"]["comparaciones"], marker="o", label="Inverso")

    plt.title("Insertion Sort: comparaciones por tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(RUTA_GRAFICAS / "parte3_comparaciones.png", dpi=150)
    plt.close()


def graficar_tiempos(resultados: Dict[str, Dict[str, List[float]]]) -> None:
    """Genera y guarda la gráfica de tiempos por tamaño para los 3 escenarios."""
    plt.figure(figsize=(10, 6))

    plt.plot(TAMANOS, resultados["aleatorio"]["tiempos"], marker="o", label="Aleatorio")
    plt.plot(TAMANOS, resultados["casi_ordenado"]["tiempos"], marker="o", label="Casi ordenado")
    plt.plot(TAMANOS, resultados["inverso"]["tiempos"], marker="o", label="Inverso")

    plt.title("Insertion Sort: tiempo de ejecución por tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(RUTA_GRAFICAS / "parte3_tiempo.png", dpi=150)
    plt.close()


def main() -> None:
    """Punto de entrada: ejecuta el experimento y genera las gráficas."""
    resultados = ejecutar_experimento()
    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()