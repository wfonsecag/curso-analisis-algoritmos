import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
RUTA_GRAFICAS = Path(__file__).parent / "graficas"


def medir_algoritmo(
    algoritmo,
    datos: list[int],
) -> float:
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio


def ejecutar_experimento() -> dict:
    resultados = {
        "insertion": [],
        "merge": [],
    }

    for n in TAMANOS:
        datos = generar_aleatorio(n, semilla=42)

        tiempo_insertion = medir_algoritmo(
            insertion_sort,
            datos,
        )

        tiempo_merge = medir_algoritmo(
            merge_sort,
            datos,
        )

        resultados["insertion"].append(tiempo_insertion)
        resultados["merge"].append(tiempo_merge)

        print(
            f"n={n} | "
            f"Insertion Sort={tiempo_insertion:.6f} s | "
            f"Merge Sort={tiempo_merge:.6f} s"
        )

    return resultados


def graficar_tiempos(resultados: dict) -> None:
    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        resultados["insertion"],
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        TAMANOS,
        resultados["merge"],
        marker="o",
        label="Merge Sort",
    )

    plt.title("Comparación de tiempo: Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)

    plt.savefig(
        RUTA_GRAFICAS / "parte4_tiempo.png",
        dpi=150,
    )

    plt.close()


def main() -> None:
    resultados = ejecutar_experimento()

    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()