# Reto 7 — Qué pasa cuando la ventana de contexto crece

**Objetivo:** observar en la práctica los dos conceptos de tu mapa sobre ventana de contexto: que crece con cada turno, y que un contexto saturado empeora el rendimiento.

Este reto no necesita código nuevo — usa todo lo que ya tienes en el repo, pero en una sola sesión larga de chat, sin abrir chats nuevos a mitad. Esa es la condición clave del experimento: la ventana de contexto se acumula por chat, no por skill.

## Preparación

VS Code tiene desde hace poco un panel de depuración de agente que te deja ver esto de forma mucho más directa que solo "intuirlo": `Developer: Open Agent Debug Panel` desde la paleta de comandos (Ctrl+Shift+P / Cmd+Shift+P). Si tu versión lo tiene, ábrelo antes de empezar — te va a mostrar el system prompt, las skills cargadas, y las tool calls de cada turno en tiempo real.

## Ejercicio A — observa el crecimiento turno a turno

En un único chat nuevo, en este orden:

1. Pide el cálculo del Reto 1 Ejercicio A (interés compuesto, 5000€ al 4%, 8 años).
2. Pide el análisis del Reto 2 Ejercicio A (`ventas_ok.csv`).
3. Pide el cálculo de amortización del Reto 6 Ejercicio A (hipoteca 200000€).
4. Pide que valide un DNI usando la tool MCP (si la tienes montada del Reto 4).
5. Por último, pide: "resume todo lo que hemos calculado en esta conversación".

El paso 5 es la prueba real de que el contexto se acumula: si Copilot puede resumir correctamente los 4 resultados anteriores sin volver a ejecutar nada, es porque todo seguía disponible en la ventana de contexto de ese chat — ninguno de esos resultados se "olvidó" entre turnos.

## Ejercicio B — fuerza la compactación

VS Code compacta automáticamente la conversación cuando la ventana de contexto se llena, y desde hace poco puedes forzarlo tú con `/compact` en el chat. Tras el Ejercicio A, escribe:

> /compact

y después pregunta de nuevo:

> ¿Cuál fue el resultado del préstamo de 200000€ que calculamos antes?

Observa si la respuesta sigue siendo correcta. Si VS Code resumió la conversación al compactar, es posible que algunos detalles numéricos exactos se pierdan o se aproximen — es el riesgo que tu mapa describe sobre saturación de contexto, materializado: en algún momento, mantener todo "tal cual" deja de ser viable y algo se resume o se descarta.

## Ejercicio C — sesión larga real, sin compactar a mano

Repite una secuencia similar a la del Ejercicio A pero más larga (6-8 peticiones distintas, mezclando skills, la tool MCP, y preguntas normales de programación sin relación). No fuerces `/compact` esta vez — déjalo pasar de forma natural. En algún momento debería aparecer un aviso o un cambio de comportamiento que indique que VS Code compactó automáticamente.

Pregunta para reflexionar con tus propias observaciones (no hay una respuesta de referencia única para esto, depende de tu sesión real): ¿en qué momento notaste que las respuestas empezaron a tardar más, o a perder precisión sobre detalles de turnos muy anteriores? ¿Coincide con cuando se disparó la compactación?

## Cierre de todo el recorrido

Has visto, con código real y observación directa, casi todas las piezas de tu mapa original:
- LLM + Prompt + Agente + Bucle del agente (todos los retos)
- Tool, vía terminal (skills) y vía MCP con schema (Reto 4)
- Skills con descubrimiento progresivo (Reto 2)
- Instructions siempre activas vs Skills condicionales (Reto 3)
- Hooks deterministas (Reto 5)
- Desambiguación entre piezas que se solapan (Reto 6)
- Ventana de contexto y su saturación (este reto)
- Memoria de sesión vs algo más persistente (Reto 4 Ejercicio C, con el estado del servidor MCP)

Lo único de tu mapa original que queda fuera a propósito es **Subagentes** — dijiste que todavía no, así que se queda pendiente para cuando quieras dar ese siguiente paso.
