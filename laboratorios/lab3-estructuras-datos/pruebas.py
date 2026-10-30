"""Pruebas del laboratorio 03: lista enlazada y tabla hash."""

from __future__ import annotations

import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ("en bodega", "en reparto", "entregado")


def probar_lista_y_tabla_basicas() -> None:
    """Busquedas exitosas e infructuosas en la lista y en la tabla."""
    # Serie de ejemplo del enunciado.
    ejemplo = [
        (1000000010, "en bodega"),
        (1000000024, "en reparto"),
        (1000000017, "en bodega"),
        (1000000005, "entregado"),
    ]
    lista = ListaEnlazada()
    tabla = TablaHash(7)
    for guia, estado in ejemplo:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia, estado in ejemplo:
        assert lista.buscar(guia) == estado
        assert tabla.buscar(guia) == estado

    # Busquedas infructuosas: la guia no existe.
    assert lista.buscar(1000000099) is None
    assert tabla.buscar(1000000099) is None

    # Estructuras vacias.
    assert ListaEnlazada().buscar(5) is None
    assert TablaHash(7).buscar(5) is None
    assert TablaHash(7).factor_carga() == 0

    # La lista inserta al inicio: la ultima guia insertada queda en cabeza.
    assert lista.cabeza is not None and lista.cabeza.guia == 1000000005
    assert lista.tamano == 4 and tabla.tamano == 4


def probar_colision_forzada() -> None:
    """Con m = 7, las guias 10, 24 y 17 caen en la casilla 3."""
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, "en bodega")

    # Las tres siguen siendo encontrables pese a compartir casilla.
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    # Una guia de otra casilla o inexistente devuelve None.
    assert tabla.buscar(3) is None  # 3 % 7 = 3: misma casilla, no existe

    # La lista de la casilla 3 tiene longitud 3 y las demas estan vacias.
    assert tabla.casillas[3].tamano == 3
    assert sum(c.tamano for c in tabla.casillas) == 3

    # Factor de carga n / m.
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Lista y tabla devuelven lo mismo en 30 colecciones aleatorias."""
    azar = random.Random(2026)
    for _ in range(30):
        n = azar.randint(1, 300)
        m = azar.choice((1, 7, 31, 101, 997))
        guias = azar.sample(range(10**9, 10**10), n)
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        estados: dict[int, str] = {}
        for guia in guias:
            estado = azar.choice(ESTADOS)
            estados[guia] = estado
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        # Guias existentes: ambas devuelven el estado guardado.
        for guia in guias:
            assert lista.buscar(guia) == estados[guia]
            assert tabla.buscar(guia) == estados[guia]

        # Guias inexistentes: ambas devuelven None.
        conjunto = set(guias)
        for _ in range(50):
            guia = azar.randint(10**9, 10**10 - 1)
            if guia in conjunto:
                continue
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

        assert tabla.tamano == lista.tamano == n
        assert tabla.factor_carga() == n / m


def main() -> None:
    """Ejecuta todas las pruebas."""
    probar_lista_y_tabla_basicas()
    probar_colision_forzada()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
