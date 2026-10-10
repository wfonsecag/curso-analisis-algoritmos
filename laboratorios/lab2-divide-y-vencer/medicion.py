"""Medición del laboratorio 02: subarreglo máximo.

Uso:
    python medicion.py            # experimento completo y gráficas
    python medicion.py --millon   # además mide divide y vencerás con 10**6
"""

from __future__ import annotations

import math
import random
import sys
import time
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS: list[int] = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES: int = 3
SEMILLA_BASE: int = 20261009
RUTA_GRAFICAS = Path(__file__).parent / "graficas"

FuncionAlgoritmo = Callable[[list[float]], tuple[int, int, float]]


def generar_datos(n: int, semilla: int) -> list[float]:
    """Genera una lista reproducible de enteros entre -100 y 100.

    Args:
        n: Cantidad de días (tamaño de la lista).
        semilla: Semilla del generador, para poder repetir la medición.

    Returns:
        Lista de n variaciones diarias con valores enteros en [-100, 100].
    """
    generador = random.Random(semilla)
    return [generador.randint(-100, 100) for _ in range(n)]


def divide_y_venceras(datos: list[float]) -> tuple[int, int, float]:
    """Adapta subarreglo_maximo a la firma de un solo argumento.

    Args:
        datos: Variación diaria de caja.

    Returns:
        La tupla (inicio, fin, suma) de subarreglo_maximo sobre toda la lista.
    """
    return subarreglo_maximo(datos, 0, len(datos) - 1)


def medir_algoritmo(algoritmo: FuncionAlgoritmo, datos: list[float]) -> float:
    """Mide una ejecución del algoritmo, sin incluir la generación de datos.

    Args:
        algoritmo: Función que recibe la lista y devuelve (inicio, fin, suma).
        datos: Lista sobre la que se ejecuta el algoritmo.

    Returns:
        Tiempo de la llamada, en segundos.
    """
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()
    return fin - inicio


def medir_promedio(algoritmo: FuncionAlgoritmo, datos: list[float]) -> float:
    """Promedia varias ejecuciones del algoritmo sobre la misma lista.

    Args:
        algoritmo: Función que recibe la lista y devuelve (inicio, fin, suma).
        datos: Lista sobre la que se ejecuta el algoritmo.

    Returns:
        Promedio de REPETICIONES mediciones, en segundos.
    """
    tiempos = [medir_algoritmo(algoritmo, datos) for _ in range(REPETICIONES)]
    return sum(tiempos) / len(tiempos)


def ejecutar_experimento() -> tuple[list[int], list[float], list[float]]:
    """Ejecuta el experimento y valida que ambas funciones dan la misma suma.

    Returns:
        Tupla (tamaños, tiempos de fuerza bruta, tiempos de divide y
        vencerás), con los tiempos en segundos.
    """
    tiempos_fuerza_bruta: list[float] = []
    tiempos_divide_y_venceras: list[float] = []

    for indice, n in enumerate(TAMANOS):
        datos = generar_datos(n, semilla=SEMILLA_BASE + indice)

        resultado_fb = subarreglo_fuerza_bruta(datos)
        resultado_dv = divide_y_venceras(datos)
        assert resultado_fb[2] == resultado_dv[2], (
            n, resultado_fb, resultado_dv,
        )

        tiempo_fb = medir_promedio(subarreglo_fuerza_bruta, datos)
        tiempo_dv = medir_promedio(divide_y_venceras, datos)

        tiempos_fuerza_bruta.append(tiempo_fb)
        tiempos_divide_y_venceras.append(tiempo_dv)

        print(
            f"n={n} | fuerza_bruta={tiempo_fb:.6f} s | "
            f"divide_y_venceras={tiempo_dv:.6f} s | suma={resultado_fb[2]}"
        )

    return TAMANOS, tiempos_fuerza_bruta, tiempos_divide_y_venceras


def imprimir_tabla(
    tamanos: list[int],
    tiempos_fb: list[float],
    tiempos_dv: list[float],
) -> None:
    """Imprime los tiempos medidos como tabla Markdown para el README.

    Args:
        tamanos: Tamaños de entrada medidos.
        tiempos_fb: Tiempos de la fuerza bruta, en segundos.
        tiempos_dv: Tiempos de divide y vencerás, en segundos.
    """
    print("\n| n | Fuerza bruta (s) | Divide y vencerás (s) |")
    print("|---:|---:|---:|")
    for n, t_fb, t_dv in zip(tamanos, tiempos_fb, tiempos_dv):
        print(f"| {n} | {t_fb:.6f} | {t_dv:.6f} |")


def imprimir_factores_al_duplicar(
    tamanos: list[int],
    tiempos_fb: list[float],
    tiempos_dv: list[float],
) -> None:
    """Imprime cuánto se multiplica el tiempo cuando n se duplica.

    Solo considera pares de tamaños consecutivos en los que n2 = 2 * n1 y
    compara el factor medido con el que predice cada complejidad teórica:
    4 para Θ(n²) y 2 * log2(n2) / log2(n1) para Θ(n log n).

    Args:
        tamanos: Tamaños de entrada medidos.
        tiempos_fb: Tiempos de la fuerza bruta, en segundos.
        tiempos_dv: Tiempos de divide y vencerás, en segundos.
    """
    print("\nFactor de crecimiento del tiempo cuando n se duplica:")
    print("| n1 -> n2 | FB medido | FB esperado Θ(n²) "
          "| DV medido | DV esperado Θ(n log n) |")
    print("|---|---:|---:|---:|---:|")
    for i in range(len(tamanos) - 1):
        n1, n2 = tamanos[i], tamanos[i + 1]
        if n2 != 2 * n1:
            continue
        medido_fb = tiempos_fb[i + 1] / tiempos_fb[i]
        medido_dv = tiempos_dv[i + 1] / tiempos_dv[i]
        esperado_dv = 2 * math.log2(n2) / math.log2(n1)
        print(
            f"| {n1} -> {n2} | {medido_fb:.2f} | 4.00 "
            f"| {medido_dv:.2f} | {esperado_dv:.2f} |"
        )


def graficar_tiempos(
    tamanos: list[int],
    tiempos_fb: list[float],
    tiempos_dv: list[float],
) -> None:
    """Genera la gráfica tiempo vs. tamaño de entrada en escala lineal.

    Args:
        tamanos: Tamaños de entrada medidos.
        tiempos_fb: Tiempos de la fuerza bruta, en segundos.
        tiempos_dv: Tiempos de divide y vencerás, en segundos.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_fb, marker="o", label="Fuerza bruta")
    plt.plot(tamanos, tiempos_dv, marker="o", label="Divide y vencerás")
    plt.title("Subarreglo máximo: tiempo de ejecución vs tamaño de entrada")
    plt.xlabel("Tamaño de entrada n (número de días)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(RUTA_GRAFICAS / "tiempo_vs_n.png", dpi=150)
    plt.close()


def graficar_tiempos_log(
    tamanos: list[int],
    tiempos_fb: list[float],
    tiempos_dv: list[float],
) -> None:
    """Genera la misma gráfica con ambos ejes en escala logarítmica.

    La escala log-log permite ver los tamaños pequeños, que en la escala
    lineal quedan pegados al eje horizontal.

    Args:
        tamanos: Tamaños de entrada medidos.
        tiempos_fb: Tiempos de la fuerza bruta, en segundos.
        tiempos_dv: Tiempos de divide y vencerás, en segundos.
    """
    plt.figure(figsize=(10, 6))
    plt.loglog(tamanos, tiempos_fb, marker="o", label="Fuerza bruta")
    plt.loglog(tamanos, tiempos_dv, marker="o", label="Divide y vencerás")
    plt.title("Subarreglo máximo: tiempo vs tamaño (escala log-log)")
    plt.xlabel("Tamaño de entrada n (número de días, escala log)")
    plt.ylabel("Tiempo de ejecución (s, escala log)")
    plt.legend()
    plt.grid(True, which="both", alpha=0.4)
    plt.tight_layout()

    RUTA_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(RUTA_GRAFICAS / "tiempo_vs_n_loglog.png", dpi=150)
    plt.close()


def medir_millon() -> None:
    """Mide divide y vencerás con 10**6 registros (la fuerza bruta no).

    Sirve para contrastar la estimación del informe con una medición real.
    La fuerza bruta se omite a propósito: con 10**6 datos tardaría horas.
    """
    n = 1_000_000
    datos = generar_datos(n, semilla=SEMILLA_BASE + len(TAMANOS))
    tiempo = medir_promedio(divide_y_venceras, datos)
    print(f"\nn={n} | divide_y_venceras={tiempo:.6f} s (medición directa)")


def main() -> None:
    """Punto de entrada del experimento."""
    tamanos, tiempos_fb, tiempos_dv = ejecutar_experimento()
    imprimir_tabla(tamanos, tiempos_fb, tiempos_dv)
    imprimir_factores_al_duplicar(tamanos, tiempos_fb, tiempos_dv)
    graficar_tiempos(tamanos, tiempos_fb, tiempos_dv)
    graficar_tiempos_log(tamanos, tiempos_fb, tiempos_dv)
    if "--millon" in sys.argv:
        medir_millon()


if __name__ == "__main__":
    main()
