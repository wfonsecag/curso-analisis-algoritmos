# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Wilmar Fonseca García · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `7dddfdc`

Excelente trabajo: entregó un laboratorio completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **97 / 100** |
| **Nota (0–5)** | **4.85** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explicó bien la colisión con el ejemplo de las guías 10, 24 y 17 en la casilla 3, y comparó encadenamiento con direccionamiento abierto, con su ventaja y su costo.
- Justificó que la tabla no sirve para rangos y que el árbol sí, y estimó la altura y las comparaciones del árbol degenerado frente al equilibrado.
- Recomendó una combinación (tabla más árbol equilibrado) y declaró la estimación a 5.000.000 de envíos como estimación, explicando su razonamiento.

**Lo que puede mejorar (y cómo corregirlo):**
- Al explicar el direccionamiento abierto solo mencionó "una regla de sondeo" sin describir cómo funciona.
  → *Cómo corregirlo:* nombre al menos un tipo de sondeo y diga con sus palabras qué casilla se prueba después de encontrar la primera ocupada.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Justificó el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla, nombró el supuesto de hash uniforme y explicó que, si todo cae en una casilla, la tabla se comporta como una lista.

**Lo que puede mejorar (y cómo corregirlo):**
- Dijo que cada casilla tiene "en promedio n/m nodos" pero no explicó por qué el hash uniforme lleva a ese promedio.
  → *Cómo corregirlo:* conecte la probabilidad de cada casilla (1/m) con el reparto de los n elementos para llegar al tamaño promedio de la cadena.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las dos estructuras responden bien en búsquedas exitosas e infructuosas; la colisión forzada con `m = 7` funciona y `factor_carga` da 3/7.
- La tabla reutiliza la lista, no usa `dict`, `set` ni `hash()`, y la búsqueda de la lista es con ciclo `while`.
- Las pruebas cubren 30 colecciones aleatorias y todas pasan. Hay *docstrings* con `Args` y `Returns`, *type hints* y buen espaciado entre funciones.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda; la primera cubre seis valores de `n` con las dos curvas en los mismos ejes y la segunda cuatro valores de `α`.
- Calculó los factores de crecimiento (4,17 para la lista y 0,94 para la tabla entre 5.000 y 20.000) y los contrastó con `Θ(n)` y `Θ(1)`.

**Lo que puede mejorar (y cómo corregirlo):**
- En la segunda gráfica, el tiempo creció unas 3,6 veces mientras `α` se multiplicó por 20. Dijo que es coherente con `Θ(1 + α)`, pero no comparó con lo que esa fórmula predice.
  → *Cómo corregirlo:* calcule cuánto crece `1 + α` entre los mismos dos valores de `α` y compárelo con el crecimiento medido, comentando la diferencia.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, trae su nombre, instrucciones de reproducción y enlaces al código de cada parte; las gráficas están incrustadas con rutas que funcionan.
- Hay cinco commits descriptivos sobre el laboratorio.
- La carpeta del laboratorio está en `laboratorios/lab3-estructuras-datos/`, ubicación válida.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y la medición corre completa y regenera las dos gráficas. Las estructuras devuelven lo mismo en todos los casos probados.
