import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    datos = list(range(1, n + 1))

    generador = random.Random(semilla)
    generador.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    cantidad_ordenada = int(n * 0.98)
    cantidad_nueva = n - cantidad_ordenada

    datos_ordenados = list(
        range(n, cantidad_nueva, -1)
    )

    datos_nuevos = list(
        range(n + 1, n + cantidad_nueva + 1)
    )

    generador = random.Random(semilla)
    generador.shuffle(datos_nuevos)

    return datos_ordenados + datos_nuevos


def generar_inverso(n: int) -> list[int]:
    return list(range(1, n + 1))