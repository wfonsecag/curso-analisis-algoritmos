"""Pruebas del laboratorio 02: subarreglo máximo."""

from __future__ import annotations

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)


def verificar_misma_suma(valores: list[float]) -> None:
    """Verifica que ambos algoritmos devuelven la misma suma máxima."""
    suma_fb = subarreglo_fuerza_bruta(valores)[2]
    suma_dv = subarreglo_maximo(valores, 0, len(valores) - 1)[2]
    assert suma_fb == suma_dv, (valores, suma_fb, suma_dv)


def verificar_tramo_consistente(valores: list[float]) -> None:
    """Verifica que los índices devueltos suman realmente el valor devuelto."""
    for inicio, fin, suma in (
        subarreglo_fuerza_bruta(valores),
        subarreglo_maximo(valores, 0, len(valores) - 1),
    ):
        assert 0 <= inicio <= fin < len(valores), (valores, inicio, fin)
        assert sum(valores[inicio:fin + 1]) == suma, (valores, inicio, fin)


def main() -> None:
    """Ejecuta pruebas representativas y aleatorias."""
    # Serie de ocho días del enunciado: la mejor racha es del día 2 al 7.
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

    # Un solo elemento.
    assert subarreglo_fuerza_bruta([7])[2] == 7
    assert subarreglo_maximo([7], 0, 0)[2] == 7

    # Todos negativos: la mejor racha es el elemento menos negativo.
    negativos = [-8, -3, -10, -2, -7]
    assert subarreglo_fuerza_bruta(negativos)[2] == -2
    assert subarreglo_maximo(negativos, 0, len(negativos) - 1)[2] == -2

    # Todos positivos: la mejor racha es la serie completa.
    positivos = [1, 2, 3, 4, 5]
    assert subarreglo_fuerza_bruta(positivos)[2] == 15
    assert subarreglo_maximo(positivos, 0, len(positivos) - 1)[2] == 15

    # Caso cruzado: el mejor tramo (índices 1 a 3) cruza el punto medio
    # (medio = 2), así que ni la mitad izquierda ni la derecha lo contienen.
    cruzado = [-2, 3, -1, 4, -5, 2]
    assert subarreglo_fuerza_bruta(cruzado)[2] == 6
    assert subarreglo_maximo(cruzado, 0, len(cruzado) - 1)[2] == 6
    assert suma_cruzada(cruzado, 0, 2, 5) == (1, 3, 6)

    # Ninguna función modifica la lista recibida.
    original = [-3, 5, -2, 8, -6, 3, 9, -4]
    copia = original.copy()
    subarreglo_fuerza_bruta(original)
    subarreglo_maximo(original, 0, len(original) - 1)
    suma_cruzada(original, 0, 3, 7)
    assert original == copia

    # Los índices devueltos son coherentes con la suma devuelta.
    for caso in (serie, [7], negativos, positivos, cruzado):
        verificar_tramo_consistente(caso)

    # Listas aleatorias (semilla fija): ambas funciones deben dar la misma
    # suma. Se incluyen tamaños pequeños y algunos mayores.
    generador = random.Random(42)
    for _ in range(50):
        tamano = generador.randint(1, 60)
        muestra = [generador.randint(-100, 100) for _ in range(tamano)]
        verificar_misma_suma(muestra)
        verificar_tramo_consistente(muestra)

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
