def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista en orden descendente usando Insertion Sort.

    La función NO modifica la lista de entrada: trabaja sobre una copia y
    devuelve una nueva lista ordenada junto con el número de comparaciones
    realizadas entre elementos.

    Args:
        datos: Lista de enteros que se desea ordenar.

    Returns:
        Tuple donde el primer elemento es la lista ordenada (nueva lista) y
        el segundo elemento es el número de comparaciones realizadas.
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
    """Ordena una lista en orden descendente usando Merge Sort.

    La función trabaja conceptualmente sobre una copia de los subarreglos y
    devuelve una nueva lista ordenada y el número de comparaciones entre
    elementos realizadas durante el proceso.

    Args:
        datos: Lista de enteros que se desea ordenar.

    Returns:
        Tuple donde el primer elemento es la lista ordenada (nueva lista) y
        el segundo elemento es el número de comparaciones realizadas.
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


def merge(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ordenadas (descendente) y cuenta comparaciones.

    Args:
        izquierda: Primera lista ordenada (descendente).
        derecha: Segunda lista ordenada (descendente).

    Returns:
        Tuple con la lista combinada (descendente) y el número de comparaciones
        realizadas durante la fusión.
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