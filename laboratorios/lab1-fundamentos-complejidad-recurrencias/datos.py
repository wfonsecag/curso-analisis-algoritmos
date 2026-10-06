import random
from typing import List


"""Generadores de datos para los experimentos del laboratorio.

Funciones:
- `generar_aleatorio`: devuelve una permutación aleatoria de 1..n con semilla.
- `generar_casi_ordenado`: devuelve una lista con el 98% ordenada y el 2% final mezclado.
- `generar_inverso`: devuelve la lista en orden inverso.

Las funciones devuelven nuevas listas de enteros y no modifican argumentos externos.
"""


def generar_aleatorio(n: int, semilla: int = 42) -> List[int]:
    """Genera una permutación aleatoria de los enteros de 1 a n.

    Args:
        n: Tamaño de la lista a generar.
        semilla: Semilla para el generador aleatorio (por reproducibilidad).

    Returns:
        Lista de enteros de longitud `n` con los valores 1..n en orden aleatorio.
    """
    datos = list(range(1, n + 1))

    generador = random.Random(semilla)
    generador.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> List[int]:
    """Genera una lista casi ordenada.

    Construye una lista donde el 98% de los primeros elementos están en orden
    ascendente y el 2% final contiene nuevos registros mezclados (con semilla).

    Args:
        n: Tamaño de la lista a generar.
        semilla: Semilla para mezclar los elementos nuevos.

    Returns:
        Lista de enteros de longitud `n` aproximadamente ordenada.
    """
    cantidad_ordenada = int(n * 0.98)
    cantidad_nueva = n - cantidad_ordenada

    datos_ordenados = list(range(1, cantidad_ordenada + 1))

    # Generar nuevos valores distintos y mezclarlos
    datos_nuevos = list(range(cantidad_ordenada + 1, cantidad_ordenada + cantidad_nueva + 1))

    generador = random.Random(semilla)
    generador.shuffle(datos_nuevos)

    return datos_ordenados + datos_nuevos


def generar_inverso(n: int) -> List[int]:
    """Genera la lista 1..n en orden inverso (mayor a menor).

    Args:
        n: Tamaño de la lista a generar.

    Returns:
        Lista de enteros en orden inverso.
    """
    return list(range(n, 0, -1))