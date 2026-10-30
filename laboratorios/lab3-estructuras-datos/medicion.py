"""Medicion del laboratorio 03: lista enlazada frente a tabla hash.

Experimento A: tiempo de busqueda de guias inexistentes frente a n.
Experimento B: tiempo de busqueda frente al factor de carga alfa.
"""

from __future__ import annotations

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

TAMANOS: list[int] = [100, 500, 1000, 5000, 20000, 50000]
N_EXPERIMENTO_B: int = 20000
ALFAS: list[float] = [0.5, 1.0, 4.0, 10.0]
BUSQUEDAS_A: int = 200
BUSQUEDAS_B: int = 1000
REPETICIONES: int = 7
SEMILLA_GUIAS: int = 2026
ESTADOS: tuple[str, ...] = ("en bodega", "en reparto", "entregado")
RUTA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo.

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Devuelve el primo mas pequeno que es mayor o igual al objetivo.

    Args:
        objetivo: valor desde el cual se busca el primo.

    Returns:
        El menor primo mayor o igual a `objetivo`.
    """
    candidato = max(2, objetivo)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def generar_guias(n: int, semilla: int) -> list[int]:
    """Genera n guias distintas de diez digitos con semilla fija.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador.

    Returns:
        Lista de n enteros distintos entre 10**9 y 10**10 - 1.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def construir(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash, dict[int, str]]:
    """Construye la lista y la tabla con las mismas guias.

    Args:
        guias: guias a insertar en ambas estructuras.
        m: numero de casillas de la tabla.

    Returns:
        La lista, la tabla y el estado esperado de cada guia.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    estados: dict[int, str] = {}
    for posicion, guia in enumerate(guias):
        estado = ESTADOS[posicion % len(ESTADOS)]
        estados[guia] = estado
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla, estados


def verificar_coinciden(
    lista: ListaEnlazada,
    tabla: TablaHash,
    estados: dict[int, str],
    muestra: int = 200,
) -> None:
    """Verifica que lista y tabla devuelven el mismo estado.

    Args:
        lista: lista enlazada ya construida.
        tabla: tabla hash ya construida.
        estados: estado esperado de cada guia almacenada.
        muestra: cuantas guias existentes se comprueban.
    """
    azar = random.Random(11)
    guias = list(estados)
    for guia in azar.sample(guias, min(muestra, len(guias))):
        assert lista.buscar(guia) == estados[guia] == tabla.buscar(guia)


def tiempo_medio_busqueda(estructura: ListaEnlazada | TablaHash,
                          guias: list[int]) -> float:
    """Mide el tiempo medio por busqueda sobre una lista de guias.

    Cronometra solo las busquedas, y repite el bloque REPETICIONES veces
    para devolver la mediana, que resiste mejor el ruido del sistema.

    Args:
        estructura: lista o tabla donde se busca.
        guias: guias que se buscan en cada repeticion.

    Returns:
        Mediana, entre repeticiones, del tiempo medio por busqueda en
        microsegundos.
    """
    medias: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in guias:
            estructura.buscar(guia)
        fin = time.perf_counter()
        medias.append((fin - inicio) / len(guias))
    return statistics.median(medias) * 1e6


def experimento_a() -> tuple[list[int], list[int], list[float], list[float]]:
    """Mide lista y tabla para cada n, con busquedas inexistentes.

    Returns:
        Tupla (tamanos, m usado, tiempos de la lista, tiempos de la tabla),
        con los tiempos en microsegundos por busqueda.
    """
    ms: list[int] = []
    t_lista: list[float] = []
    t_tabla: list[float] = []
    for n in TAMANOS:
        m = primo_cercano(n // 2)
        guias = generar_guias(n, SEMILLA_GUIAS)
        lista, tabla, estados = construir(guias, m)
        verificar_coinciden(lista, tabla, estados)
        inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS_A)
        assert all(lista.buscar(g) is None for g in inexistentes[:5])

        t_l = tiempo_medio_busqueda(lista, inexistentes)
        t_t = tiempo_medio_busqueda(tabla, inexistentes)
        ms.append(m)
        t_lista.append(t_l)
        t_tabla.append(t_t)
        print(f"n={n} | m={m} | alfa={tabla.factor_carga():.2f} | "
              f"lista={t_l:.3f} us | tabla={t_t:.3f} us")
    return TAMANOS, ms, t_lista, t_tabla


def experimento_b() -> tuple[list[float], list[float]]:
    """Mide la tabla con n fijo y distintos factores de carga.

    Returns:
        Tupla (alfa real de cada tabla, tiempos en microsegundos por
        busqueda).
    """
    guias = generar_guias(N_EXPERIMENTO_B, SEMILLA_GUIAS)
    inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS_B)
    alfas_reales: list[float] = []
    tiempos: list[float] = []
    for alfa in ALFAS:
        m = primo_cercano(round(N_EXPERIMENTO_B / alfa))
        lista, tabla, estados = construir(guias, m)
        verificar_coinciden(lista, tabla, estados, muestra=100)
        t = tiempo_medio_busqueda(tabla, inexistentes)
        alfas_reales.append(tabla.factor_carga())
        tiempos.append(t)
        print(f"alfa={tabla.factor_carga():.2f} | m={m} | "
              f"tabla={t:.3f} us")
    return alfas_reales, tiempos


def imprimir_tabla_a(
    tamanos: list[int],
    ms: list[int],
    t_lista: list[float],
    t_tabla: list[float],
) -> None:
    """Imprime los resultados del experimento A como tabla Markdown.

    Args:
        tamanos: valores de n medidos.
        ms: numero de casillas usado en cada n.
        t_lista: tiempos de la lista, en microsegundos.
        t_tabla: tiempos de la tabla, en microsegundos.
    """
    print("\n| n | m | alfa | Lista (us) | Tabla (us) |")
    print("|---:|---:|---:|---:|---:|")
    for n, m, tl, tt in zip(tamanos, ms, t_lista, t_tabla):
        print(f"| {n} | {m} | {n / m:.2f} | {tl:.3f} | {tt:.3f} |")


def imprimir_factores(
    tamanos: list[int], t_lista: list[float], t_tabla: list[float]
) -> None:
    """Imprime cuanto se multiplica el tiempo entre valores consecutivos de n.

    Args:
        tamanos: valores de n medidos.
        t_lista: tiempos de la lista, en microsegundos.
        t_tabla: tiempos de la tabla, en microsegundos.
    """
    print("\nFactor por el que se multiplica el tiempo entre n consecutivos")
    print("(esperado: lista = n2 / n1, tabla = 1):")
    print("| n1 -> n2 | n2 / n1 | Lista medido | Tabla medido |")
    print("|---|---:|---:|---:|")
    for i in range(len(tamanos) - 1):
        n1, n2 = tamanos[i], tamanos[i + 1]
        print(f"| {n1} -> {n2} | {n2 / n1:.2f} "
              f"| {t_lista[i + 1] / t_lista[i]:.2f} "
              f"| {t_tabla[i + 1] / t_tabla[i]:.2f} |")


def imprimir_tabla_b(alfas: list[float], tiempos: list[float]) -> None:
    """Imprime los resultados del experimento B como tabla Markdown.

    Args:
        alfas: factor de carga real de cada tabla.
        tiempos: tiempos en microsegundos por busqueda.
    """
    print("\n| alfa | Tabla (us) |")
    print("|---:|---:|")
    for alfa, tiempo in zip(alfas, tiempos):
        print(f"| {alfa:.2f} | {tiempo:.3f} |")


def graficar_a(
    tamanos: list[int], t_lista: list[float], t_tabla: list[float]
) -> None:
    """Genera lista_vs_tabla.png.

    Args:
        tamanos: valores de n medidos.
        t_lista: tiempos de la lista, en microsegundos.
        t_tabla: tiempos de la tabla, en microsegundos.
    """
    RUTA_GRAFICAS.mkdir(exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, t_lista, marker="o", label="Lista enlazada")
    plt.plot(tamanos, t_tabla, marker="o", label="Tabla hash (alfa ~ 2)")
    plt.title("Busqueda de una guia inexistente: lista vs tabla hash")
    plt.xlabel("Numero de guias n (envios almacenados)")
    plt.ylabel("Tiempo medio por busqueda (us)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def graficar_b(alfas: list[float], tiempos: list[float]) -> None:
    """Genera tiempo_vs_alfa.png.

    Args:
        alfas: factor de carga real de cada tabla.
        tiempos: tiempos en microsegundos por busqueda.
    """
    RUTA_GRAFICAS.mkdir(exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.plot(alfas, tiempos, marker="o", label="Tabla hash, n = 20.000")
    plt.title("Tabla hash: tiempo de busqueda vs factor de carga")
    plt.xlabel("Factor de carga alfa = n / m (guias por casilla)")
    plt.ylabel("Tiempo medio por busqueda (us)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos, imprime tablas y genera las graficas."""
    print("== Experimento A: lista vs tabla ==")
    tamanos, ms, t_lista, t_tabla = experimento_a()
    imprimir_tabla_a(tamanos, ms, t_lista, t_tabla)
    imprimir_factores(tamanos, t_lista, t_tabla)
    graficar_a(tamanos, t_lista, t_tabla)

    print("\n== Experimento B: factor de carga ==")
    alfas, tiempos = experimento_b()
    imprimir_tabla_b(alfas, tiempos)
    graficar_b(alfas, tiempos)


if __name__ == "__main__":
    main()
