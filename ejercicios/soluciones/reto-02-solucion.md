# Solución y comentario — Reto 2

## Ejercicio A — caso limpio

Salida esperada del script (resumen): `total_importe: 437.79`, categoría líder `Electrónica` con `240.49`.

Comportamiento esperado de Copilot: ejecuta el script, lee el JSON, te responde — **sin** abrir `referencia/columnas_esperadas.md` ni `referencia/formulas.md`, porque `columnas_faltantes` viene vacío y no has pedido ningún cálculo extra. Si ves que Copilot abre esos ficheros igualmente "por si acaso", es una señal de que no está aprovechando bien las instrucciones de carga condicional del SKILL.md — anótalo, es información útil sobre el modelo/configuración que estés usando.

## Ejercicio B — columnas raras

Primera ejecución (sin mapeo) devuelve `columnas_faltantes: ["fecha", "categoria", "importe"]`. Según el propio SKILL.md, esto debería disparar la lectura de `referencia/columnas_esperadas.md`.

Comando esperado tras leer la referencia:
```bash
python3 .github/skills/analizador-csv/scripts/analizar.py --csv ejemplos_datos/ventas_raras.csv --mapeo "Fecha de venta=fecha" --mapeo "Tipo de producto=categoria" --mapeo "Cantidad EUR=importe"
```
Resultado: `total_importe: 195.5`.

Si Copilot en cambio intenta adivinar el mapeo sin leer la referencia y falla (por ejemplo mapea mal `Tipo de producto` a `importe`), es un caso real de skill mal aprovechada — el fichero de referencia existía precisamente para evitar esa improvisación.

## Ejercicio C — nivel 3 (fórmulas)

Fórmula esperada (de `formulas.md`):
```
margen_% = (importe_categoria / importe_total_global) * 100
```
Con los datos del CSV limpio: `240.49 / 437.79 * 100 ≈ 54.9%`.

Punto clave: si ya analizaste el CSV en el mismo chat, Copilot no debería re-ejecutar el script — ya tiene `total_por_categoria` y `total_importe` en el contexto de la conversación (la "memoria de sesión" de tu mapa). Si abres un chat nuevo, sí necesita volver a ejecutar el script porque ese contexto no persiste entre conversaciones (a menos que tengas memoria persistente configurada, que es un concepto distinto — el "memory" de tu mapa, no la sesión).

## Ejercicio D — columna ambigua sin variante conocida

No hay una única respuesta correcta aquí — es justo el punto. Lo que deberías observar es uno de estos tres patrones:

1. **Pregunta al usuario** qué columna corresponde a qué campo (comportamiento más seguro).
2. **Improvisa un mapeo** basándose en el nombre de columna y el contexto semántico (ej. infiere que "Coste" es probablemente `importe` aunque no esté en la lista) — puede acertar o no.
3. **Se bloquea** y dice que no puede analizar el CSV sin más información.

Los tres son "correctos" en distinto grado según cuánta autonomía quieras darle al agente. Esto es exactamente la tensión de "Riesgo: perder el control del código" de tu mapa, aplicada a un caso pequeño: cuanto más improvisa el agente sin pedir confirmación, más rápido vas, pero menos controlas qué está asumiendo.
