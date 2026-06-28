# Reto 1 — Ver el bucle agente → tool → resultado

**Objetivo:** ver cómo Copilot detecta una skill sencilla, ejecuta el script como herramienta del terminal, y te devuelve el resultado interpretado.

## Antes de empezar — predicción

Sin mirar el código de `calculadora-finanzas`, responde mentalmente (o por escrito, mejor):

1. ¿Crees que Copilot va a "ejecutar algo" o va a calcular el interés compuesto él mismo, mentalmente, con el LLM?
2. ¿Qué pasa si tu pregunta es ambigua sobre si quieres "evolución año a año" o "tiempo hasta duplicar"?

## Ejercicio A

Abre Copilot Chat en modo **Agent** y pregunta, tal cual:

> Si invierto 5000 euros al 4% anual durante 8 años, ¿cuánto tendré al final?

Observa:
- ¿Aparece un paso de "usando skill calculadora-finanzas" o similar?
- ¿Te pide aprobar la ejecución de un comando de terminal? Acepta y mira el comando exacto que construyó — ¿qué argumentos eligió y de dónde los sacó de tu frase?
- ¿La respuesta final coincide con lo que el JSON del script devolvió, o el LLM "redondeó"/interpretó algo por su cuenta?

## Ejercicio B

Ahora pregunta:

> ¿Cuántos años tardan 2000€ en duplicarse al 3% de interés?

Observa si Copilot elige correctamente `--objetivo-multiplicador` en vez de `--anios`. Esto depende de si la `description` y el cuerpo del SKILL.md son lo bastante claros — es la parte que más se parece a "diseñar bien el prompt/skill = calidad del resultado" de tu mapa.

## Ejercicio C (rompe algo a propósito)

Pregunta:

> Calcula el interés compuesto de mi hipoteca de 200000€ con cuotas mensuales al 3% en 20 años

Esto es justo el caso que el SKILL.md dice explícitamente que NO cubre (amortización con cuotas, no capital único). Observa qué hace Copilot:
- ¿Reconoce que la skill no aplica y te lo dice?
- ¿Intenta forzar el script igualmente y el resultado sale mal sin avisar?
- ¿Calcula la amortización él mismo sin usar ningún script?

Esto es importante: una skill bien escrita también debe decir claramente qué NO cubre, igual que documentarías una función para un compañero.

## Preguntas para ti (sin solución única, son para reflexionar)

- ¿En qué parte exacta del proceso pasamos de "el LLM decide" a "se ejecuta código de verdad de forma determinista"?
- Si cambiaras la `description` del SKILL.md a algo muy vago como "Hace cálculos", ¿crees que seguiría detectándose igual de bien? Pruébalo y compara.

Solución/comentario de referencia: `soluciones/reto-01-solucion.md`
