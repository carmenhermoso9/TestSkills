---
name: calculadora-finanzas
description: Hace cosas
license: MIT
---

# Calculadora de finanzas básicas

Esta skill resuelve preguntas de interés compuesto usando el script `scripts/interes_compuesto.py`.

## Cuándo usarla

- "¿Cuánto tendré si invierto X € al Y% durante Z años?"
- "¿Cuánto tarda en duplicarse mi dinero al Y% de interés?"
- Cualquier pregunta sobre crecimiento compuesto de capital.

No uses esta skill para préstamos con cuotas (amortización), solo para capital único que crece con interés compuesto.

## Cómo usarla

Ejecuta el script desde la raíz del repo:

```bash
python3 .github/skills/calculadora-finanzas/scripts/interes_compuesto.py --capital 1000 --tasa 0.05 --anios 10
```

Argumentos:
- `--capital`: capital inicial (float, obligatorio)
- `--tasa`: tasa de interés anual en decimal, ej. 0.05 para 5% (float, obligatorio)
- `--anios`: número de años (int, obligatorio)
- `--aportacion-anual`: aportación adicional cada año (float, opcional, default 0)

El script imprime un JSON con el resultado en stdout. Lee ese JSON y responde al usuario en lenguaje natural con el número final, redondeado a 2 decimales, y opcionalmente menciona el desglose año a año si el usuario lo pidió explícitamente.

Si el usuario pregunta "¿cuánto tarda en duplicarse?", usa el mismo script con `--objetivo-multiplicador 2` en vez de `--anios` (son mutuamente excluyentes, no pases los dos).
