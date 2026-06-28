---
name: analizador-csv
description: Analiza ficheros CSV de ventas o gastos y genera estadísticas (totales, medias, top categorías, detección de columnas faltantes o mal formateadas). Usa esta skill cuando el usuario mencione un fichero .csv y pida un análisis, resumen, estadísticas, o si el CSV da error al procesarlo.
license: MIT
---

# Analizador de CSV de ventas/gastos

Esta skill tiene varios recursos. **No los cargues todos de golpe** — esa es la idea de esta skill: lee solo lo que necesites para la tarea concreta.

## Paso 1 — siempre

Ejecuta el script base para obtener estadísticas generales:

```bash
python3 .github/skills/analizador-csv/scripts/analizar.py --csv RUTA_AL_FICHERO
```

Esto devuelve un JSON con: número de filas, columnas detectadas, columnas que faltan (si alguna columna esperada no está), totales por columna numérica, y la fila con el valor máximo/mínimo por columna numérica.

## Paso 2 — solo si el script reporta columnas faltantes o tipos inesperados

Si el JSON de salida incluye `"columnas_faltantes"` no vacío, o `"avisos"` no vacío, lee `referencia/columnas_esperadas.md` para saber qué columnas espera el script y cómo se llaman habitualmente sus variantes (ej. "importe" vs "monto" vs "total").

No leas este fichero si el script no reportó ningún problema — no aporta nada en ese caso.

## Paso 3 — solo si el usuario pide cálculos financieros específicos (margen, crecimiento %, médias ponderadas)

Si el usuario pide algo que el script base no calcula (por ejemplo "calcúlame el margen sobre el total" o "qué % creció cada mes"), lee `referencia/formulas.md` antes de escribir el código para ese cálculo ad-hoc, en vez de inventar la fórmula de memoria.

## Notas

- El script nunca modifica el CSV original, solo lee.
- Si el CSV no existe o la ruta está mal, el script devuelve un JSON con `"error"` — no es un fallo silencioso.
