# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

**Estudiante:** Wilmar Fonseca García

## Reproducción del laboratorio

El laboratorio fue desarrollado en Python utilizando un entorno virtual y la biblioteca `matplotlib`.

### Activar el entorno virtual

Desde la raíz del repositorio:

```bash
.venv\Scripts\activate
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

### Ejecutar Parte 3

```bash
python laboratorios/lab1-fundamentos-complejidad-recurrencias/parte3_casos.py
```

Este comando ejecuta las pruebas de Insertion Sort para los tres escenarios y genera:

* `graficas/parte3_comparaciones.png`
* `graficas/parte3_tiempo.png`

### Ejecutar Parte 4

```bash
python laboratorios/lab1-fundamentos-complejidad-recurrencias/parte4_complejidad.py
```

Este comando compara los tiempos de Insertion Sort y Merge Sort y genera:

* `graficas/parte4_tiempo.png`

Los algoritmos implementados se encuentran en [`algoritmos.py`](algoritmos.py) y los generadores de datos en [`datos.py`](datos.py).

---

# Parte 1 — Analizar el algoritmo antes de comprar hardware

En el caso de la plataforma Tamiza es importante analizar primero el algoritmo porque que un algoritmo sea correcto no significa que siga siendo viable cuando aumenta considerablemente la cantidad de datos.

El algoritmo actual de Insertion Sort puede producir una lista correctamente ordenada y durante varios años pudo cumplir con el proceso. Sin embargo, la situación cambió porque ahora debe procesar 1.200.000 registros dentro de una restricción concreta de tiempo: entre las 2:00 a. m. y las 6:00 a. m. La ventana disponible es de solamente cuatro horas y no se puede ampliar.

La eficiencia debe analizarse teniendo en cuenta el recurso que se consume y la restricción que debe cumplirse. En este caso el recurso principal es el tiempo de procesamiento. Aunque el algoritmo siga entregando una lista correcta, si tarda más de cuatro horas deja de ser viable para el proceso de producción.

Duplicar la velocidad del servidor puede disminuir el tiempo de ejecución, pero no cambia la forma en que crece el número de operaciones del algoritmo. Insertion Sort tiene un comportamiento cuadrático en sus casos desfavorables, por lo que cuando aumenta mucho la cantidad de registros el número de operaciones crece rápidamente. Por esta razón, aumentar solamente la velocidad del hardware no soluciona la causa principal del problema.

Un ejemplo más concreto sería un sistema de inventario tecnológico que debe ordenar aproximadamente 100.000 equipos para generar reportes y asignaciones antes del inicio del turno. Si la restricción operativa exige, por ejemplo, que el reporte se genere en menos de 2 minutos, la diferencia en la complejidad puede ser determinante: extrapolando desde la medición registrada en este laboratorio para 6.400 registros (≈1,05 s) y asumiendo crecimiento cuadrático, el tiempo estimado para 100.000 registros sería del orden de minutos (≈4,3 min), por lo que no cumpliría una ventana estricta de 2 minutos. El punto es que hay que comparar el crecimiento teórico del algoritmo con la restricción concreta del proceso (qué se procesa, cuántos datos y cuánto tiempo disponible) antes de comprar hardware.

Por esto, antes de invertir en hardware es necesario analizar el comportamiento del algoritmo y determinar si su crecimiento permite cumplir la restricción de cuatro horas con el volumen actual y futuro de datos.

---

# Parte 2 — Responsabilidad ambiental y ética de la implementación

El tiempo de ejecución de un algoritmo también tiene una relación directa con el consumo de recursos. Una ejecución que necesita más tiempo mantiene el servidor trabajando durante más tiempo y, por lo tanto, puede aumentar el consumo de energía. En Tamiza el proceso se ejecuta durante la noche y debe repetirse de manera frecuente. Si el algoritmo mantiene un comportamiento costoso durante años, el impacto no corresponde solamente a una ejecución, sino a la acumulación de muchas ejecuciones. Por ejemplo, una ejecución nocturna que ocupe 4 horas por noche equivale a `4 h × 365 = 1.460 horas` de servidor al año; ese volumen ya es significativo para el consumo energético y el coste operativo.

La decisión también tiene una responsabilidad ética porque los registros representan personas que esperan ser contactadas de acuerdo con su nivel de riesgo.

Un primer impacto puede presentarse sobre un paciente con un nivel de riesgo alto. Si el proceso no termina antes de las 6:00 a. m. o genera una lista incompleta, ese paciente podría no aparecer oportunamente en la lista de llamadas. El costo lo asume principalmente el paciente, porque puede existir un retraso en la atención o en el contacto que se esperaba realizar.

Un segundo impacto puede presentarse sobre el operador del call center. Si la lista no queda ordenada correctamente por nivel de riesgo, el operador puede comenzar a llamar a personas con menor prioridad mientras otras con mayor riesgo todavía están pendientes. En este caso el costo recae sobre el operador porque debe trabajar con información incompleta o incorrecta y posiblemente realizar reprocesos.

También existe un costo para la Secretaría de Salud. Si el proceso falla de manera repetida, puede ser necesario reprocesar información, revisar resultados y dedicar recursos técnicos adicionales para solucionar el problema.

Finalmente, el equipo de desarrollo también asume un costo cuando una solución que ya no escala obliga a realizar correcciones urgentes o mantener una implementación que no responde al crecimiento de los datos.

Existe además una responsabilidad sobre el orden de la lista. No se trata solamente de obtener una lista ordenada, porque el orden determina quién será llamado primero y, por tanto, la prioridad de atención. En producción no basta con que el proceso termine a tiempo: también hay que garantizar que el orden refleje correctamente la prioridad. Esto exige controles adicionales, por ejemplo:

- Pruebas unitarias y de integración que verifiquen que la prioridad está preservada en distintos tamaños y disposiciones de entrada.
- Validación por muestreo y auditoría periódica para detectar desviaciones en el orden.
- Registros de trazabilidad que permitan reproducir y verificar resultados ante incidencias.

Por esta razón, la selección del algoritmo debe considerar el tiempo, el consumo de recursos, la confiabilidad del proceso y las obligaciones de validación y auditoría que impone la correcta priorización.

---

# Parte 3 — Peor caso, mejor caso y caso promedio, demostrados en Python

Código utilizado en esta parte: [`parte3_casos.py`](parte3_casos.py)

Los algoritmos y generadores utilizados en esta parte se encuentran en [`algoritmos.py`](algoritmos.py) y [`datos.py`](datos.py).

## 3.1 — Peor caso, mejor caso y caso promedio

Para un tamaño fijo `n`, el **peor caso** corresponde al conjunto de entradas que produce el mayor costo de ejecución del algoritmo.

El **mejor caso** corresponde al conjunto de entradas del mismo tamaño `n` que produce el menor costo de ejecución.

El **caso promedio** representa el comportamiento esperado calculado sobre el conjunto de todas las permutaciones de `n` elementos, asumiendo una distribución uniforme entre esas permutaciones. En la práctica experimental usamos el escenario aleatorio como aproximación de este comportamiento promedio.

Para Tamiza no se debe seleccionar el algoritmo pensando únicamente en el mejor caso. Como la ventana de procesamiento es estricta y el proceso debe terminar antes de las 6:00 a. m., se debe considerar un comportamiento que permita responder correctamente incluso cuando la entrada sea desfavorable.

Por esta razón, el criterio de producción debe considerar principalmente el peor caso y la capacidad del algoritmo para mantener un crecimiento controlado cuando aumenta el número de registros.

### Predicción antes de realizar las mediciones

Para Insertion Sort se esperaba el siguiente comportamiento:

* **Escenario A — Aleatorio:** comportamiento cercano al caso promedio.
* **Escenario B — Casi ordenado:** comportamiento cercano al mejor caso.
* **Escenario C — Inverso:** comportamiento correspondiente al peor caso.

La predicción se realizó antes de ejecutar las mediciones.

En el escenario B, el conjunto contiene el 98 % de los datos ordenados y el 2 % de nuevos registros agregados al final. Por esta razón se aproxima al mejor caso, aunque el mejor caso exacto sería una entrada completamente ordenada en el sentido requerido por el algoritmo.

## Resultados experimentales

Se utilizaron los tamaños:

`100, 200, 400, 800, 1600, 3200 y 6400`

El tiempo se midió utilizando `time.perf_counter()` y solamente se midió la ejecución del algoritmo. La generación de los datos se realizó antes de iniciar el cronómetro.

### Comparaciones

![Comparaciones de Insertion Sort](graficas/parte3_comparaciones.png)

### Tiempo de ejecución

![Tiempo de ejecución de Insertion Sort](graficas/parte3_tiempo.png)

## 3.2 — Análisis de los resultados

Los resultados de las comparaciones muestran diferencias claras entre los tres escenarios.

En el escenario B, correspondiente a la entrada casi ordenada, el número de comparaciones crece mucho menos que en los escenarios A y C. Para `n = 6400`, se obtuvieron:

* Aleatorio: `10.276.753` comparaciones.
* Casi ordenado: `813.455` comparaciones.
* Inverso: `20.476.800` comparaciones.

El escenario C presenta el mayor número de comparaciones y también el mayor tiempo de ejecución, por lo que corresponde al comportamiento esperado para el peor caso de Insertion Sort.

El escenario A presenta un comportamiento intermedio y representa el comportamiento esperado para entradas aleatorias.

El escenario B presenta el menor costo de los tres escenarios medidos y se aproxima al mejor caso debido a que la mayor parte de los datos ya se encuentra ordenada.

Los resultados experimentales coinciden con la predicción realizada antes de las mediciones.

---

# Parte 4 — Complejidad de Merge Sort e Insertion Sort: cálculo y validación

Código utilizado en esta parte: [`parte4_complejidad.py`](parte4_complejidad.py)

Los algoritmos utilizados se encuentran en [`algoritmos.py`](algoritmos.py) y los datos de prueba en [`datos.py`](datos.py).

## 4.1 — Complejidad teórica

### Merge Sort

La recurrencia de Merge Sort es:

`T(n) = 2T(n/2) + Θ(n)`

Cada término representa:

* `2T(n/2)`: se realizan dos llamadas recursivas y cada una procesa aproximadamente la mitad de los datos.
* `Θ(n)`: corresponde al costo de combinar las dos partes ordenadas.
* `T(n)`: representa el tiempo total necesario para procesar una entrada de tamaño `n`.

### Resolución mediante el Teorema Maestro

La forma general es:

`T(n) = aT(n/b) + f(n)`

En este caso:

`a = 2`

`b = 2`

`f(n) = Θ(n)`

Calculamos:

`n^(log₂ 2) = n`

Por lo tanto:

`n^(log₂ b) = n^(log₂ 2) = n`

y, como:

`f(n) = Θ(n)`

se obtiene directamente que:

`f(n) = Θ(n^(log₂ b))`

Es decir, `f(n)` y `n^(log₂ b)` tienen el mismo orden de crecimiento.

Se cumple entonces la condición del caso 2 del Teorema Maestro.

Por lo tanto:

`T(n) = Θ(n log n)`

Así, Merge Sort tiene un crecimiento `Θ(n log n)` en sus casos de entrada.

### Análisis detallado de Insertion Sort (ligado al código)

La implementación utilizada realiza una copia de la lista y trabaja sobre esa copia. Si llamamos `a` a la lista de entrada y `a_copy` a la copia que manipula el algoritmo, el flujo principal es:

1. `for i in range(1, n)`: el ciclo externo se ejecuta `n - 1` veces.
2. `clave = a_copy[i]`: asignación de la clave — `n - 1` veces.
3. `j = i - 1`: inicialización de `j` — `n - 1` veces.
4. `while j >= 0 and a_copy[j] > clave`: cada iteración del `while` genera una comparación entre elementos; en el peor caso el número total de comparaciones del `while` sobre todos los `i` es `1 + 2 + ... + (n - 1) = n(n - 1)/2`.
5. Dentro del `while`, el desplazamiento se realiza con `a_copy[j + 1] = a_copy[j]`: en el peor caso también puede ocurrir hasta `n(n - 1)/2` movimientos.
6. Al salir del `while`, se hace `a_copy[j + 1] = clave`: una asignación final por iteración del `for` (`n - 1` veces).

Resumiendo los costos (peor caso): el ciclo `for` y las asignaciones lineales aportan términos Θ(n), mientras que las comparaciones y desplazamientos del `while` aportan Θ(n²). Conservando el término dominante:

`T(n) = Θ(n²)`

En el mejor caso (lista ya ordenada) el `while` realiza aproximadamente una comparación por elemento y no hay desplazamientos, por lo que `T(n) = Θ(n)`. El caso promedio, tomando la media sobre permutaciones aleatorias, mantiene `T(n) = Θ(n²)`.

### Comparación de complejidades (resumen)

| Algoritmo      | Mejor        | Promedio     | Peor         |
| -------------- | ------------:| ------------:| ------------:|
| Insertion Sort | `Θ(n)`       | `Θ(n²)`      | `Θ(n²)`      |
| Merge Sort     | `Θ(n log n)` | `Θ(n log n)` | `Θ(n log n)` |

---

## 4.2 — Validación experimental

Se compararon Insertion Sort y Merge Sort utilizando el escenario A, con los mismos tamaños empleados en la Parte 3.

Los tiempos se midieron utilizando `time.perf_counter()` y cada medición corresponde al promedio de 5 repeticiones para reducir el ruido experimental.

![Comparación de tiempo entre Insertion Sort y Merge Sort](graficas/parte4_tiempo.png)

A medida que aumenta `n`, la diferencia entre los dos algoritmos se hace cada vez mayor.

Para `n = 6400`, los resultados promediados fueron:

- Insertion Sort (promedio 5 repeticiones): `2.515812 segundos`
- Merge Sort (promedio 5 repeticiones): `0.028995 segundos`

En esta medición, Merge Sort fue aproximadamente **86.8 veces más rápido** que Insertion Sort.

La curva de Insertion Sort crece mucho más rápidamente a medida que aumenta el tamaño de entrada, mientras que Merge Sort mantiene un crecimiento considerablemente menor.

La conclusión experimental coincide con el análisis teórico. Insertion Sort presenta un crecimiento cuadrático en el escenario aleatorio, mientras que Merge Sort presenta un crecimiento `Θ(n log n)`.

En los tamaños utilizados en esta prueba, Merge Sort presentó un mejor tiempo de ejecución que Insertion Sort, aunque en tamaños muy pequeños la diferencia puede ser reducida debido al costo adicional de la recursividad y la combinación de datos.

La diferencia entre ambos algoritmos puede verse en la gráfica [graficas/parte4_tiempo.png](laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte4_tiempo.png), donde para tamaños pequeños las curvas están más cerca y la separación se vuelve más visible a medida que `n` crece.

---

# 4.3 — Concepto técnico a la Secretaría de Salud

**Para:** Equipo de ingeniería de la Secretaría de Salud
**Asunto:** Recomendación de algoritmo para el procesamiento de registros de la plataforma Tamiza

Se recomienda reemplazar Insertion Sort por Merge Sort para el proceso nocturno de ordenamiento de los registros de Tamiza.

El criterio principal de selección debe ser el comportamiento del algoritmo cuando cambia el tipo de entrada. La plataforma recibe información de diferentes fuentes y el orden de los datos puede cambiar sin previo aviso. Por esta razón, no resulta conveniente mantener tres implementaciones diferentes dependiendo de si los datos llegan aleatorios, casi ordenados o en orden inverso. Se recomienda utilizar un algoritmo cuyo comportamiento tenga un crecimiento más controlado frente a estos cambios.

Las mediciones realizadas muestran una diferencia importante. Con 6.400 registros del escenario A (promedio de 5 repeticiones), Insertion Sort tardó `2.515812 segundos`, mientras que Merge Sort tardó `0.028995 segundos`. En esta medición, Merge Sort fue aproximadamente 86.8 veces más rápido. Estos valores provienen de la misma corrida que generó la gráfica [graficas/parte4_tiempo.png](laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte4_tiempo.png).

Para estimar el comportamiento con los 1.200.000 registros de producción se utiliza como referencia la medición de 6.400 registros y el crecimiento teórico de cada algoritmo. Extrapolando:

- Para Insertion Sort (crecimiento Θ(n²)):

	ratio = (1.200.000 / 6.400)² ≈ 35_156.25

	tiempo ≈ 2.515812 × 35_156.25 ≈ 88_446 segundos ≈ **24.57 horas** (aproximación; no es una medición directa).

- Para Merge Sort (crecimiento Θ(n log n)):

	ratio = (1.200.000 × log₂(1.200.000)) / (6.400 × log₂(6.400)) ≈ 299.5

	tiempo ≈ 0.028995 × 299.5 ≈ **8.68 segundos** (aproximación; no es una medición directa).

Estas estimaciones muestran que duplicar la velocidad del servidor no soluciona la causa principal: Insertion Sort mantiene un crecimiento cuadrático que, al extrapolarse al volumen de producción, puede superar ampliamente la ventana de cuatro horas.

Además del tiempo, se debe considerar el mantenimiento de la solución. Merge Sort requiere memoria adicional para realizar las divisiones y combinaciones de los datos. Sin embargo, este costo debe compararse con el riesgo operativo de depender de que el escenario B continúe siendo casi ordenado. Si en algún momento cambia la forma de entrada y los datos llegan en un orden desfavorable, Insertion Sort puede aumentar considerablemente su tiempo de procesamiento.

Por lo anterior, se recomienda implementar Merge Sort como la solución única para el ordenamiento de los registros antes de generar la lista de llamadas. Esta alternativa ofrece un crecimiento `Θ(n log n)` y reduce considerablemente el riesgo de que el cambio en el tipo de entrada provoque que el proceso supere la ventana de cuatro horas.
