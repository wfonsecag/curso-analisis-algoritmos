# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Wilmar Fonseca García · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-13 23:59 · **Versión revisada:** commit `23e5ee8`

Muy buen trabajo, completo y ordenado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 19 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **80 / 100** |
| **Nota (0–5)** | **4.00** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue entre que el algoritmo sea correcto y que sea viable, y nombra la restricción incumplida: la ventana de cuatro horas.
- Explica que duplicar la velocidad del servidor no cambia cómo crece el trabajo del algoritmo.
- En la Parte 2 identifica varios perjuicios (paciente, operador, Secretaría, equipo) e indica quién asume cada costo.
- Discute que el orden de la lista decide a quién se llama primero y propone controles de validación.

**Lo que puede mejorar:**
- En el segundo ejemplo (inventario de 100.000 equipos) usa 1,05 s para 6.400 registros. Su propia gráfica muestra cerca de 2,5 s con datos aleatorios, así que el tiempo estimado (4,3 min) no coincide con sus mediciones.
- La relación entre tiempo, energía y años de operación está explicada, pero queda general; faltó un dato propio más concreto.

## 2. Calidad de la explicación teórica (19 / 25)
**Lo que hizo bien:**
- Define peor, mejor y caso promedio indicando sobre qué entradas se toma cada uno, y justifica usar el peor caso por la ventana estricta.
- Deja escrita la predicción antes de medir.
- Plantea bien la recurrencia de merge sort, explica cada término y la resuelve con el método maestro llegando a `Θ(n log n)`.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- Al verificar el método maestro compara con `n^(log₂ b)`; lo correcto es `n^(log_b a)`. Aquí da igual porque a = b = 2, pero la condición debe escribirse bien.
- El análisis de insertion sort línea a línea no corresponde a su código: usa nombres (`a_copy`) y una condición del ciclo que no son los de su implementación, y no suma el costo de cada línea para llegar al total.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida y cuentan comparaciones entre elementos. No usa `sorted()` ni `sort()`.
- Merge sort tiene su propia mezcla recursiva.
- Los generadores dan listas del tamaño pedido, sin repetidos, y con semilla.

**Lo que puede mejorar:**
- Algunas líneas pasan de 100 caracteres (en `parte3_casos.py` y sobre todo en `parte4_complejidad.py`).
- Las descripciones de módulo en `datos.py` y `parte3_casos.py` quedaron después de las importaciones, así que Python no las toma como descripción del archivo.
- Varias funciones de medición no tienen las secciones `Args` y `Returns` del estilo Google.
- Está usando `List` de `typing`; se pide la forma `list[int]`.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda, y las curvas comparten ejes.
- Identifica con cifras que el escenario inverso es el peor, el casi ordenado el mejor y el aleatorio el intermedio, y lo contrasta con su predicción.
- Concluye que merge sort es mejor y lo apoya en sus tiempos (2,52 s frente a 0,029 s en n = 6400).
- Extrapola a 1.200.000 registros declarando que es una estimación, y responde a la propuesta del servidor con un dato medido.

**Lo que puede mejorar:**
- Menciona que con tamaños pequeños la diferencia puede ser reducida, pero no lo explica con lo que muestra su gráfica.
- Dice que el tiempo estimado "puede superar" las cuatro horas; con su cálculo (unas 24,6 horas) puede afirmarlo directamente.
- Se habla de la memoria extra de merge sort, pero no se mide ni se estima.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida y tiene todos los archivos pedidos.
- El informe está dividido por partes, con las gráficas visibles y enlaces al código en cada parte.
- Tiene instrucciones de reproducción y varios commits descriptivos.

**Lo que puede mejorar:**
- Los enlaces de texto a `parte4_tiempo.png` en 4.2 y 4.3 usan una ruta que no funciona desde el informe; deben ser relativos a su carpeta (`graficas/parte4_tiempo.png`).
- Las instrucciones de activación del entorno no indican cómo instalar `matplotlib` (por ejemplo desde `requirements.txt`).

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien listas pequeñas, aleatorias y de los tres escenarios, y el experimento corre y genera las gráficas.

## Para el próximo laboratorio
- Revise que las cifras de un ejemplo vengan de sus mediciones publicadas.
- Haga el análisis línea a línea sobre su propio código, sumando el costo de cada línea.
- Cuide el estilo PEP 8: líneas cortas, descripciones de módulo al inicio y `Args`/`Returns` en cada función.
- Compruebe que los enlaces del informe abren el archivo desde su carpeta.
- Explique con sus gráficas lo que pasa con tamaños pequeños.
