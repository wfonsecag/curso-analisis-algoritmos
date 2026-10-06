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

# Número de repeticiones por tamaño/escenario para promediar mediciones
REPETICIONES: int = 5


def medir_insertion(datos: List[int]) -> Tuple[float, int]:
    """Mide una única ejecución de `insertion_sort` sobre `datos`.

    Esta función ejecuta el algoritmo una vez y devuelve el tiempo y el
    número de comparaciones reportado.
    """
    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    return fin - inicio, comparaciones


def medir_promediado(datos: List[int], repeticiones: int = REPETICIONES) -> Tuple[float, float]:
    """Ejecuta `medir_insertion` repetidas veces y devuelve el promedio.

    Args:
        datos: Lista de entrada para la medición (la función no la modifica).
        repeticiones: Número de ejecuciones a promediar.

    Returns:
        `(tiempo_promedio, comparaciones_promedio)` — ambos como `float`.
    """
    tiempos: List[float] = []
    comparaciones_list: List[int] = []

    for _ in range(repeticiones):
        # Pasamos una copia a la medición para garantizar que cada ejecución
        # parte del mismo estado de entrada.
        tiempo, comparaciones = medir_insertion(datos.copy())
        tiempos.append(tiempo)
        comparaciones_list.append(comparaciones)

    tiempo_promedio = sum(tiempos) / len(tiempos)
    comparaciones_promedio = sum(comparaciones_list) / len(comparaciones_list)

    return tiempo_promedio, comparaciones_promedio


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
            # Medimos varias repeticiones y promediamos para obtener valores
            # más estables frente a ruido de ejecución.
            tiempo, comparaciones = medir_promediado(datos, repeticiones=REPETICIONES)

            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)

            print(
                f"n={n} | {nombre} | "
                f"tiempo_promedio={tiempo:.6f} s | "
                f"comparaciones_promedio={comparaciones:.1f}"
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