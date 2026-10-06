# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Wilmar Fonseca García · **Laboratorio:** Fundamentos, complejidad y recurrencias (Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `28f4c69`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 19 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **75 / 100** |
| **Nota (0–5)** | **3.75** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que sea viable, y nombra la restricción que se incumple: la ventana de cuatro horas.
- Explica que duplicar la velocidad del servidor no cambia la forma en que crece el trabajo.
- En la Parte 2 identifica varios perjuicios (paciente, operador, Secretaría, equipo) y dice quién asume cada costo.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- El segundo ejemplo (inventario de 100.000 equipos) es genérico: falta decir qué restricción exacta se rompe y con qué tiempos.
- La relación entre tiempo de ejecución y energía quedó corta: faltó una idea cuantitativa, por ejemplo cuántas horas de servidor se acumulan en un año.
- La tensión del orden de la lista se menciona, pero no se desarrolla la obligación que impone (por ejemplo, validar que el orden sea correcto).

## 2. Calidad de la explicación teórica (19 / 25)
**Lo que hizo bien:**
- Define los tres casos, justifica que usaría el peor caso para decidir y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort, explica cada término y aplica el método maestro identificando `a`, `b` y `f(n)`.
- Presenta la tabla de complejidades de insertion sort.

**Lo que puede mejorar:**
- La definición del caso promedio no dice sobre qué entradas se promedia (por ejemplo, todas las ordenaciones posibles de `n` datos).
- El análisis de insertion sort no va línea a línea sobre su código: usa una tabla de operaciones aproximadas y copia de la lista, en vez de contar cada línea real.
- Falta la complejidad de merge sort en mejor, peor y promedio dentro de la tabla.
- La verificación del método maestro es muy breve; conviene escribir la comparación y la conclusión con más detalle.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`.
- Los tres generadores entregan listas del tamaño pedido, sin repetidos, con semilla.
- Mide el tiempo solo sobre el algoritmo.

**Lo que puede mejorar:**
- Los generadores y las funciones de `parte3_casos.py` y `parte4_complejidad.py` no tienen docstring, y algunas faltan de anotaciones de tipos.
- Los docstrings de los algoritmos no siguen el texto pedido (por ejemplo, no dicen que trabajan sobre una copia).
- Cada tiempo se mide una sola vez; repetir y promediar daría curvas más estables.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y se ven en el informe.
- Identifica con cifras que el inverso es el peor caso, el aleatorio el intermedio y el casi ordenado el mejor.
- Contrasta bien la conclusión con la complejidad teórica y hace la extrapolación a 1.200.000 registros declarándola como estimación.

**Lo que puede mejorar:**
- Los números del informe para la Parte 4 (1,05 s para insertion sort) no coinciden con la gráfica publicada, donde se ve cerca de 0,6 s. Debe usar los datos de la misma corrida que la gráfica.
- El informe dice que a tamaños pequeños la diferencia es menor, pero no lo comprueba en su gráfica.
- El concepto técnico no cita la gráfica ni el tamaño de entrada del que sale el dato, y la justificación de elegir una sola implementación es breve.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en la ubicación acordada y tiene todos los archivos pedidos.
- Las gráficas se incrustan bien, cada parte enlaza su código y hay instrucciones de reproducción.

**Lo que puede mejorar:**
- Todo el laboratorio se subió en un solo commit; se pedían al menos cinco commits descriptivos que muestren el avance.
- Las instrucciones de activación del entorno sirven solo para Windows.
- El informe pone "Wilmar Fonseca" y no el nombre completo.

## ¿El código funciona?
Sí. Los scripts corren sin errores, ordenan correctamente los tres escenarios y generan las tres gráficas.

## Para el próximo laboratorio
- Haga commits pequeños y frecuentes mientras avanza, con mensajes que digan qué cambió.
- Escriba docstring y tipos en todas las funciones, también en los generadores y los scripts de medición.
- Antes de entregar, revise que los números del informe salgan de la misma corrida que las gráficas.
- Analice insertion sort línea por línea sobre su propio código e incluya merge sort en la tabla de complejidades.
- Dé datos concretos en los ejemplos propios (qué se procesa, cuántos datos, qué límite de tiempo) y cite la gráfica que respalda cada afirmación.
