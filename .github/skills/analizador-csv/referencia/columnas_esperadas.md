# Columnas esperadas por el script `analizar.py`

El script busca estas columnas (no distingue mayúsculas/minúsculas, ni tildes):

| Columna canónica | Variantes aceptadas                      | Tipo    |
|-------------------|-------------------------------------------|---------|
| fecha             | fecha, date, dia                          | fecha   |
| categoria         | categoria, categoría, category, tipo      | texto   |
| importe           | importe, monto, total, amount, precio     | número  |

Si el CSV usa nombres distintos a estos y a sus variantes, el script no podrá mapearlos automáticamente y los listará en `columnas_faltantes`. En ese caso, la solución más simple es:

1. Decirle al script qué columna del CSV corresponde a cada campo canónico usando `--mapeo columna_csv=canonico`, por ejemplo:
   ```bash
   python3 .github/skills/analizador-csv/scripts/analizar.py --csv datos.csv --mapeo "Fecha de venta=fecha" --mapeo "Cantidad EUR=importe"
   ```
2. Si el usuario no sabe qué columna corresponde a qué, sugiere mirar las primeras filas del CSV (el script ya las incluye en `"muestra_filas"` del JSON de salida) antes de adivinar.
