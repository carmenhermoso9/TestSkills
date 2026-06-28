# Reto 2 — Descubrimiento progresivo real

**Objetivo:** comprobar que Copilot solo carga los ficheros de `referencia/` cuando realmente los necesita, no siempre.

Esta es la skill `analizador-csv`. Tiene 3 niveles de carga:
1. `SKILL.md` (front-matter siempre visible, cuerpo solo si aplica)
2. `referencia/columnas_esperadas.md` (solo si el CSV tiene columnas raras)
3. `referencia/formulas.md` (solo si pides un cálculo que el script no hace de fábrica)

## Preparación

Ya tienes dos CSV de ejemplo en `ejemplos_datos/`:
- `ventas_ok.csv` — columnas estándar, no debería requerir nivel 2 ni 3.
- `ventas_raras.csv` — columnas con nombres no estándar, debería disparar nivel 2.

Si no existen en tu copia del repo, créalos tú con este contenido (o pide a Copilot que los genere, es buena práctica añadida):

`ejemplos_datos/ventas_ok.csv`:
```csv
fecha,categoria,importe
2026-01-05,Electrónica,150.50
2026-01-10,Hogar,45.00
2026-01-15,Electrónica,89.99
2026-02-01,Ropa,32.30
2026-02-10,Hogar,120.00
```

`ejemplos_datos/ventas_raras.csv`:
```csv
Fecha de venta,Tipo de producto,Cantidad EUR
05/01/2026,Electrónica,"150,50"
10/01/2026,Hogar,"45,00"
```

## Ejercicio A — caso limpio

Pregunta a Copilot:

> Analiza ejemplos_datos/ventas_ok.csv y dime el total y qué categoría vende más

Predicción antes de ejecutar: ¿debería Copilot necesitar leer `columnas_esperadas.md`? Según el propio SKILL.md, no — confírmalo observando si lo abre o no (en el panel de Copilot suele verse qué ficheros lee/abre durante el turno).

## Ejercicio B — caso con columnas raras

Pregunta:

> Analiza ejemplos_datos/ventas_raras.csv y dime el total

Aquí el script va a devolver `columnas_faltantes` no vacío. Observa si Copilot, al ver eso en el JSON de salida, decide leer `referencia/columnas_esperadas.md` y luego reintenta el comando con `--mapeo`. Eso es el "Paso 2" del SKILL.md funcionando como debería.

## Ejercicio C — forzar el nivel 3

Pregunta, sobre el CSV limpio:

> Del CSV ventas_ok.csv, ¿qué porcentaje del total representa la categoría Electrónica?

Esto no lo calcula el script de fábrica (no hay flag de "margen %"). Debería forzar a Copilot a:
1. Leer `referencia/formulas.md` para coger la fórmula exacta de "margen sobre el total".
2. Usar los datos que ya tiene del análisis previo (no debería re-ejecutar el script si ya tiene `total_por_categoria` y `total_importe` en el contexto de la conversación).

Si abres un **chat nuevo** y haces directamente esta pregunta sin haber analizado antes el CSV, Copilot probablemente necesite ejecutar el script primero. Esa diferencia es justo el concepto de "memoria de sesión" de tu mapa: lo que ya está en el contexto de este chat no se vuelve a pedir.

## Ejercicio D — el caso interesante: ambigüedad de columnas

Crea tú misma un tercer CSV con una columna ambigua, por ejemplo una columna llamada `Coste` en vez de `importe`/`monto`/`total`/`amount`/`precio` (ninguna variante del listado de `columnas_esperadas.md` la cubre). Pide a Copilot que lo analice.

¿Qué hace cuando ni siquiera el fichero de referencia tiene la variante exacta? ¿Te pregunta a ti, o intenta adivinar el mapeo él mismo? Esto reproduce el límite real del descubrimiento progresivo: si la documentación no cubre el caso, el agente tiene que decidir entre preguntar o improvisar — y esa decisión es exactamente la clase de comportamiento no determinista de la que habla tu mapa sobre el LLM.

Solución/comentario de referencia: `soluciones/reto-02-solucion.md`
