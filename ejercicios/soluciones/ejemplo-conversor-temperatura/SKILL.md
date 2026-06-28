---
name: conversor-temperatura
description: Convierte temperaturas entre Celsius, Fahrenheit y Kelvin. Usa esta skill cuando el usuario pida convertir grados, o pregunte equivalencias de temperatura entre escalas.
license: MIT
---

# Conversor de temperatura

Convierte un valor entre Celsius, Fahrenheit y Kelvin usando `scripts/convertir.py`.

## Cuándo usarla

- "¿Cuántos grados Fahrenheit son 20°C?"
- "Convierte 98.6°F a Celsius"
- Cualquier conversión entre C, F, K.

No uses esta skill para interés compuesto ni para análisis de CSV — esas son otras skills de este repo.

## Cómo usarla

```bash
python3 .github/skills/conversor-temperatura/scripts/convertir.py --valor 20 --desde C --hasta F
```

Unidades válidas: `C`, `F`, `K` (mayúsculas). Si el usuario da una temperatura por debajo del cero absoluto (-273.15°C / -459.67°F / 0K), el script devuelve un error explícito — no devuelvas tú un número igualmente, respeta ese error y explícaselo al usuario.
