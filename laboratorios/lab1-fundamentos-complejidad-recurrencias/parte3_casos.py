import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
RUTA_GRAFICAS = Path(__file__).parent / "graficas"


def medir_insertion(datos: list[int]) -> tuple[float, int]:
    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    return fin - inicio, comparaciones


def ejecutar_experimento() -> dict:
    resultados = {
        "aleatorio": {
            "tiempos": [],
            "comparaciones": [],
        },
        "casi_ordenado": {
            "tiempos": [],
            "comparaciones": [],
        },
        "inverso": {
            "tiempos": [],
            "comparaciones": [],
        },
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


def graficar_comparaciones(resultados: dict) -> None:
    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        resultados["aleatorio"]["comparaciones"],
        marker="o",
        label="Aleatorio",
    )

    plt.plot(
        TAMANOS,
        resultados["casi_ordenado"]["comparaciones"],
        marker="o",
        label="Casi ordenado",
    )

    plt.plot(
        TAMANOS,
        resultados["inverso"]["comparaciones"],
        marker="o",
        label="Inverso",
    )

    plt.title("Insertion Sort: comparaciones por tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)

    plt.savefig(
        RUTA_GRAFICAS / "parte3_comparaciones.png",
        dpi=150,
    )

    plt.close()


def graficar_tiempos(resultados: dict) -> None:
    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        resultados["aleatorio"]["tiempos"],
        marker="o",
        label="Aleatorio",
    )

    plt.plot(
        TAMANOS,
        resultados["casi_ordenado"]["tiempos"],
        marker="o",
        label="Casi ordenado",
    )

    plt.plot(
        TAMANOS,
        resultados["inverso"]["tiempos"],
        marker="o",
        label="Inverso",
    )

    plt.title("Insertion Sort: tiempo de ejecución por tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)

    plt.savefig(
        RUTA_GRAFICAS / "parte3_tiempo.png",
        dpi=150,
    )

    plt.close()


def main() -> None:
    resultados = ejecutar_experimento()

    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()