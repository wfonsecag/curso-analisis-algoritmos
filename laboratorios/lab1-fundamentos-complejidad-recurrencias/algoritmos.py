def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """
    Ordena una lista de enteros de forma descendente mediante Insertion Sort.

    Args:
        datos: Lista de enteros que se desea ordenar.

    Returns:
        Una tupla con la lista ordenada y el número de comparaciones
        realizadas entre elementos.
    """
    datos_ordenados = datos.copy()
    comparaciones = 0

    for i in range(1, len(datos_ordenados)):
        clave = datos_ordenados[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if datos_ordenados[j] < clave:
                datos_ordenados[j + 1] = datos_ordenados[j]
                j -= 1
            else:
                break

        datos_ordenados[j + 1] = clave

    return datos_ordenados, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """
    Ordena una lista de enteros de forma descendente mediante Merge Sort.

    Args:
        datos: Lista de enteros que se desea ordenar.

    Returns:
        Una tupla con la lista ordenada y el número de comparaciones
        realizadas entre elementos.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    mitad = len(datos) // 2

    izquierda, comparaciones_izquierda = merge_sort(datos[:mitad])
    derecha, comparaciones_derecha = merge_sort(datos[mitad:])

    resultado, comparaciones_merge = merge(
        izquierda,
        derecha
    )

    comparaciones_totales = (
        comparaciones_izquierda
        + comparaciones_derecha
        + comparaciones_merge
    )

    return resultado, comparaciones_totales


def merge(
    izquierda: list[int],
    derecha: list[int]
) -> tuple[list[int], int]:
    """
    Combina dos listas ordenadas de forma descendente.

    Args:
        izquierda: Primera lista ordenada.
        derecha: Segunda lista ordenada.

    Returns:
        Una tupla con la lista combinada y el número de comparaciones
        realizadas entre elementos.
    """
    resultado = []
    i = 0
    j = 0
    comparaciones = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones