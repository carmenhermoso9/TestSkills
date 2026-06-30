# De tu mapa conceptual a este repo

| Concepto de tu mapa             | Dónde está aquí                                                                 | Qué vas a observar |
|----------------------------------|----------------------------------------------------------------------------------|---------------------|
| **LLM — el cerebro**            | El modelo detrás de Copilot (eliges el modelo en el selector del chat)          | No lo ves directamente, pero todo lo demás depende de qué modelo elijas |
| **Prompt**                      | Lo que escribes en Copilot Chat                                                  | Calidad del prompt → calidad de qué skill/tool detecta y qué argumentos pasa |
| **Agente**                      | Copilot Agent mode                                                              | Es el que decide: ¿uso una skill? ¿una tool MCP? ¿ejecuto un comando? |
| **Bucle del agente**            | La secuencia: lee tu prompt → decide acción → ejecuta → lee resultado → te responde (o repite si hace falta) | Visible en el panel de chat, o en el Agent Debug Panel paso a paso |
| **Tool**                        | Dos caminos en este repo: (a) el terminal de VS Code ejecutando scripts de skill, (b) las tools reales del servidor MCP en `mcp-server/` con schema JSON | Reto 1 para (a), Reto 4 para (b) y su comparación directa |
| **Skill**                       | Cada carpeta en `.github/skills/`                                                | El `name` + `description` del SKILL.md es lo único que Copilot ve de entrada |
| **Descubrimiento progresivo**   | `analizador-csv`: el cuerpo del SKILL.md solo se carga si la descripción matchea; los ficheros en `referencia/` solo se leen si el propio SKILL.md le dice a Copilot que los lea en ese caso concreto | Reto 2 |
| **Skills que podrían solaparse**| `calculadora-finanzas` vs `calculadora-prestamos`, diseñadas a propósito para tocarse | Reto 6 |
| **Instructions**                | `.github/copilot-instructions.md`                                               | Siempre está activo, no se "descubre" — Reto 3 |
| **Hooks**                       | `.github/hooks/hooks.json` + script de guarda                                   | La única pieza 100% determinista del repo — Reto 5 |
| **Memoria de sesión**           | El propio hilo de chat con Copilot                                              | Se pierde si abres un chat nuevo — comparar con el estado del servidor MCP, que vive aparte (Reto 4 Ejercicio C) |
| **Ventana de contexto**         | Todo lo que Copilot ha cargado hasta ahora en este chat                         | Reto 7, incluida la compactación automática/manual |

## Lo que NO está en este repo (a propósito)

- **Subagentes**: en Copilot esto se parece más a "Custom Agents" (`.agent.md`), que es un concepto algo distinto a los subagentes que viste en el curso de Anthropic. Pendiente para cuando quieras dar ese paso.

## Lo que SÍ está, y vale la pena remarcar el matiz

- **MCP**: lo metimos en `mcp-server/`. Es la única vía nativa en VS Code para tener tools con function-calling real (schema JSON, argumentos tipados) — sin MCP, lo más parecido que existe son las skills ejecutando scripts por terminal, que es un mecanismo distinto aunque relacionado.
- **Hooks**: están en Preview en VS Code desde febrero 2026. Usan el mismo formato que Claude Code y Copilot CLI, así que lo que aprendas aquí es transferible.
