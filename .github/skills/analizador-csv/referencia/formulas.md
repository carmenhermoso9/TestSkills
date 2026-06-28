# Fórmulas para cálculos ad-hoc sobre los datos del CSV

Usa estas fórmulas exactas cuando el usuario pida estos cálculos sobre los datos ya cargados por `analizar.py`. No las recalcules de memoria con una variante distinta.

## Crecimiento porcentual entre dos periodos

```
crecimiento_% = ((valor_periodo_2 - valor_periodo_1) / valor_periodo_1) * 100
```

Si `valor_periodo_1` es 0, el crecimiento no está definido — dilo explícitamente, no devuelvas infinito ni None silencioso.

## Media ponderada

```
media_ponderada = sum(valor_i * peso_i for cada fila) / sum(peso_i para cada fila)
```

Para datos de ventas, el "peso" suele ser la cantidad/unidades vendidas y el "valor" el precio unitario — confírmalo con el usuario si no está claro cuál columna es cuál.

## Margen sobre el total

```
margen_% = (importe_categoria / importe_total_global) * 100
```

Redondea siempre a 1 decimal al presentar porcentajes al usuario, salvo que pida más precisión.
