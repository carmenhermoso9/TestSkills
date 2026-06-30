# Reto 6 — Cuando dos skills podrían aplicar a la vez

**Objetivo:** ver cómo decide Copilot cuál usar cuando dos skills se solapan, y qué tan bien (o mal) gestiona la frontera entre ellas.

Ahora tienes 3 skills financieras en el repo:
- `calculadora-finanzas` (interés compuesto, capital único que crece)
- `calculadora-prestamos` (amortización, cuotas periódicas que reducen deuda)
- (la de CSV no aplica aquí, es de otro dominio)

Las dos primeras están deliberadamente cerca temáticamente — ambas hablan de "intereses" y "dinero a lo largo del tiempo" — pero resuelven problemas matemáticamente opuestos (crecimiento vs amortización).

## Ejercicio A — el caso que antes quedó sin resolver

¿Recuerdas el Reto 1, Ejercicio C? Pedías:

> Calcula el interés compuesto de mi hipoteca de 200000€ con cuotas mensuales al 3% en 20 años

En aquel momento, no existía `calculadora-prestamos`, así que la única skill candidata (`calculadora-finanzas`) no cubría ese caso. Ahora sí existe la skill correcta. Repite la misma pregunta y observa:

- ¿Copilot identifica que `calculadora-prestamos` es la skill correcta, a pesar de que tu pregunta dice literalmente "interés compuesto" (el término de la otra skill)?
- ¿O se deja llevar por las palabras literales de tu pregunta y elige mal?

Esto es interesante porque tu propia frase mezclaba terminología de las dos skills — es un test real de si el agente entiende la *intención* (amortización con cuotas) o solo hace pattern-matching de palabras clave contra las `description`.

## Ejercicio B — pregunta ambigua a propósito

Pregunta, sin más contexto:

> Tengo 10000€ y un interés del 5%, ¿qué pasa en 10 años?

Esta pregunta es deliberadamente incompleta: no dice si los 10000€ son un capital que inviertes (→ `calculadora-finanzas`) o un préstamo que debes (→ `calculadora-prestamos`, y le faltaría además el dato de la cuota). Observa:

- ¿Copilot te pregunta para desambiguar antes de actuar?
- ¿Asume una de las dos interpretaciones sin preguntar? ¿Cuál, y por qué crees que eligió esa?

## Ejercicio C — pide explícitamente que dude

Pregunta:

> No estoy segura de si esto es un préstamo o una inversión, pero tengo 10000€ al 5% durante 10 años, ¿me ayudas?

Aquí le estás diciendo explícitamente que hay ambigüedad. El comportamiento ideal sería que te pregunte cuál de las dos situaciones es antes de ejecutar cualquier script — ejecutar la skill equivocada y darte un número con seguridad sería peor que preguntar.

## Reflexión

Compara los 3 ejercicios. ¿En qué punto exacto pasa Copilot de "tengo suficiente información, actúo" a "necesito preguntar"? Esa frontera no es fija — depende de cómo de explícita sea tu ambigüedad y de cómo de bien describan las skills sus límites mutuos (fíjate que el SKILL.md de `calculadora-prestamos` menciona explícitamente a `calculadora-finanzas` como "la otra cara" — eso es información que ayuda al agente a distinguir, igual que ayudaría a un compañero humano nuevo en el equipo).

Solución/comentario de referencia: `soluciones/reto-06-solucion.md`
