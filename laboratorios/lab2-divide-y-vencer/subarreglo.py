"""Subarreglo máximo: fuerza bruta y divide y vencerás."""

from __future__ import annotations


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de días.

    Args:
        valores: Variación diaria de caja, una por día. Debe contener al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los índices inclusivos del tramo de
        mayor suma y el valor de esa suma.
    """
    if not valores:
        raise ValueError("valores debe contener al menos un elemento")

    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = valores[0]

    for inicio in range(len(valores)):
        suma_actual = 0.0
        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]
            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = inicio
                mejor_fin = fin

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: Variación diaria de caja.
        inicio: Índice inicial del rango considerado (inclusive).
        medio: Índice del último elemento de la mitad izquierda.
        fin: Índice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al menos un
        elemento de cada mitad.
    """
    mejor_suma_izquierda = valores[medio]
    suma_actual = 0.0
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]
        if suma_actual > mejor_suma_izquierda:
            mejor_suma_izquierda = suma_actual
            mejor_inicio = i

    mejor_suma_derecha = valores[medio + 1]
    suma_actual = 0.0
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]
        if suma_actual > mejor_suma_derecha:
            mejor_suma_derecha = suma_actual
            mejor_fin = j

    return mejor_inicio, mejor_fin, mejor_suma_izquierda + mejor_suma_derecha


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int,
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y vencerás.

    Args:
        valores: Variación diaria de caja.
        inicio: Índice inicial del rango a considerar (inclusive).
        fin: Índice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio < 0 or fin >= len(valores):
        raise IndexError(
            "inicio y fin deben estar dentro de los límites de la lista"
        )
    if inicio > fin:
        raise ValueError("inicio no puede ser mayor que fin")

    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2
    izquierdo = subarreglo_maximo(valores, inicio, medio)
    derecho = subarreglo_maximo(valores, medio + 1, fin)
    cruzado = suma_cruzada(valores, inicio, medio, fin)

    mejor = izquierdo
    if derecho[2] > mejor[2]:
        mejor = derecho
    if cruzado[2] > mejor[2]:
        mejor = cruzado

    return mejor
