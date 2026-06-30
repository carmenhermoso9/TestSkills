---
name: calculadora-prestamos
description: Calcula la cuota mensual de un préstamo con amortización (sistema francés) y el total de intereses pagados. Usa esta skill cuando el usuario pregunte por préstamos, hipotecas, cuotas mensuales, o amortización de deuda con pagos periódicos.
license: MIT
---

# Calculadora de préstamos con amortización

Esta skill resuelve preguntas de préstamos con cuotas periódicas (sistema de amortización francés, cuota constante) usando `scripts/amortizacion.py`.

## Cuándo usarla

- "¿Cuál es la cuota mensual de un préstamo de X€ a Y% en Z años?"
- "¿Cuánto pagaré de intereses totales en una hipoteca de...?"
- Cualquier pregunta sobre préstamos con pagos periódicos que reducen el capital.

No uses esta skill para capital único que crece con interés compuesto sin pagos periódicos — para eso existe la skill `calculadora-finanzas` de este mismo repo, que es la otra cara de un cálculo parecido pero con mecánica distinta (crece en vez de amortizarse).

## Cómo usarla

```bash
python3 .github/skills/calculadora-prestamos/scripts/amortizacion.py --principal 200000 --tasa-anual 0.03 --anios 20
```

Argumentos:
- `--principal`: importe del préstamo (float, obligatorio)
- `--tasa-anual`: tasa de interés anual en decimal (float, obligatorio)
- `--anios`: duración del préstamo en años (int, obligatorio)

El script devuelve JSON con la cuota mensual, el total pagado, y el total de intereses.

## Nota deliberada para este repo de aprendizaje

Esta skill existe a propósito junto a `calculadora-finanzas` para que compruebes cómo reacciona Copilot cuando dos skills *podrían* aplicar parcialmente a la misma pregunta (ambas hablan de "préstamos" o "intereses" en su descripción, en cierto modo). Si tienes dudas sobre cuál usar para una pregunta concreta, es una señal real de que las dos descripciones se solapan — exactamente el tipo de ambigüedad que se intenta evitar al escribir un buen SKILL.md.
