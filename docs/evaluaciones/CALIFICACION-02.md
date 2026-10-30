# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Wilmar Fonseca García · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `cc67114`

Excelente trabajo: un laboratorio completo, ordenado y bien sustentado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **91 / 100** |
| **Nota (0–5)** | **4.55** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre n = 10 y n = 50 y explica por qué la fuerza bruta gana en listas muy pequeñas.
- En la comparación con el máximo de un arreglo, justifica con el costo de combinar (Θ(1)) y la recurrencia que dividir no mejora nada.
- Recomienda divide y vencerás y declara que las cifras para 1.000.000 de registros son estimaciones, sin usar una regla de tres lineal.

**Lo que puede mejorar:**
- La estimación parte de un solo tiempo (n = 8000) de divide y vencerás que tiene mucho ruido. Convenía decir que el resultado es aproximado por ese motivo o promediar varios tamaños.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea T(n) = 2T(n/2) + Θ(n) y explica de dónde sale cada término.
- Aplica el método maestro (caso 2) comparando f(n) con n^(log₂ 2) = n.
- Justifica el Θ(n²) de la fuerza bruta contando los n(n+1)/2 pares.

**Lo que puede mejorar:**
- La verificación de la condición del caso podía ser más explícita: escribir que f(n) = Θ(n^(log_b a)) y concluir de ahí el Θ(n log n).

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y ninguna función modifica la lista recibida.
- Tiene *type hints* y *docstrings* en todas las funciones, y el código cumple PEP 8.

**Lo que puede mejorar:**
- Las pruebas usan `sum()` de un tramo para comprobar índices; está bien, pero conviene dejar claro en comentarios qué se verifica.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, y cubre 8 tamaños. Agregó además una gráfica log-log y una tabla.
- Calcula los factores al duplicar n para ambos algoritmos y los compara con 4 y con 2·log₂(2n)/log₂(n).
- Mide con semilla fija, misma lista para ambos y repite 3 veces.

**Lo que puede mejorar:**
- El análisis se apoya en la tabla de números y casi no en lo que se lee en la gráfica (por ejemplo, el valor de cada curva en n = 8000).
- Los factores de divide y vencerás (3.19, 2.76, 3.37) se alejan bastante de lo esperado; lo atribuye al ruido, pero faltó usar más repeticiones o la mediana para reducirlo.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta en `laboratorios/lab2-divide-y-vencer/` con todos los archivos pedidos; el informe sigue el orden pedido, enlaza el código en cada parte e incrusta las gráficas con rutas que funcionan.
- Instrucciones de reproducción claras y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre sin errores y genera las gráficas. Al ejecutar la medición, los factores de crecimiento resultaron más cercanos a la teoría que los de su tabla.

## Para el próximo laboratorio
- Repita las mediciones más veces y use la mediana para que los tiempos pequeños sean más estables.
- Apóyese también en valores leídos de la gráfica al describir cada curva.
- Si estima con un solo tamaño, adviértalo y, mejor, promedie varios.
- Escriba explícitamente la condición del caso del método maestro.
