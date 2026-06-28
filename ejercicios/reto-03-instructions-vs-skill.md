# Reto 3 — Instructions vs Skill, y construye tú la tercera

**Objetivo:** entender la diferencia práctica entre "siempre activo" (Instructions) y "se descubre si aplica" (Skill), y luego crear una skill nueva desde cero tú misma.

## Parte A — Instructions vs Skill

Tienes `.github/copilot-instructions.md` con una regla: *"antes de ejecutar un script de una skill, di qué skill estás usando y por qué"*.

1. Pide cualquier tarea que dispare una skill (ej. del reto 1 o 2) y confirma que efectivamente Copilot dice explícitamente qué skill usa antes de ejecutar nada. Eso viene de las Instructions, no de la skill — la skill no dice nada sobre "explica tu razonamiento".
2. Ahora pide algo que **no** dispare ninguna skill, por ejemplo:
   > Explícame qué es un bucle for en Python

   ¿Sigue aplicándose la instrucción de "explica tu razonamiento antes de actuar"? Debería, porque las Instructions están siempre activas, no dependen de que una skill matchee. Esa es la diferencia clave con tu mapa: Instructions = siempre cargado en el prompt de sistema; Skill = solo `name`+`description` de entrada, cuerpo solo si aplica.

## Parte B — rompe la skill a propósito

Edita temporalmente `.github/skills/calculadora-finanzas/SKILL.md` y cambia la `description` a algo deliberadamente malo:

```yaml
description: Hace cosas.
```

Guarda, y en un **chat nuevo** de Copilot pregunta de nuevo:

> Si invierto 5000 euros al 4% anual durante 8 años, ¿cuánto tendré al final?

¿Sigue detectando la skill? Probablemente no, o lo haga con menos seguridad. Esto demuestra en la práctica la frase de tu mapa: *"calidad del prompt = calidad del resultado"* — pero aplicado a la `description` de la skill, que es el "prompt" que el agente usa para decidir si la carga.

Cuando termines, **revierte el cambio** (vuelve a poner la descripción original) y haz commit solo de esa vuelta atrás, para que quede constancia en el historial de qué probaste.

## Parte C — crea tu propia skill desde cero

Ahora te toca a ti. Crea una skill nueva, `.github/skills/conversor-unidades/`, que convierta entre unidades (por ejemplo km↔millas, kg↔libras, celsius↔fahrenheit — elige tú el alcance).

Requisitos mínimos:
- `SKILL.md` con `name` y `description` claros y que NO se solapen con las otras dos skills (para que Copilot no dude entre cuál usar).
- Un script Python en `scripts/` que reciba argumentos por línea de comandos y devuelva JSON, igual que las otras dos.
- Al menos un caso que el script rechace explícitamente con un mensaje de error claro (unidad no soportada, valor negativo donde no tiene sentido, etc.) — no dejes que falle en silencio.

Pista de proceso: puedes pedirle directamente a Copilot Agent mode que te ayude a generar el `SKILL.md` y el script, usando este mismo repo como ejemplo de formato. Es buena práctica ver si Copilot, cuando construye una skill, sigue el mismo patrón de las que ya existen en el repo (las lee como contexto del proyecto).

No hay solución de referencia para la Parte C porque el alcance lo decides tú — pero en `soluciones/reto-03-solucion.md` tienes una versión mía de ejemplo (conversor de temperatura) para comparar enfoques, no para copiar antes de intentarlo.
