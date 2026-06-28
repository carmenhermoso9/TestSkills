# De tu mapa conceptual a este repo

| Concepto de tu mapa             | Dónde está aquí                                                                 | Qué vas a observar |
|----------------------------------|----------------------------------------------------------------------------------|---------------------|
| **LLM — el cerebro**            | El modelo detrás de Copilot (eliges el modelo en el selector del chat)          | No lo ves directamente, pero todo lo demás depende de qué modelo elijas |
| **Prompt**                      | Lo que escribes en Copilot Chat                                                  | Calidad del prompt → calidad de qué skill detecta y qué argumentos pasa al script |
| **Agente**                      | Copilot Agent mode                                                              | Es el que decide: ¿uso una skill? ¿ejecuto un comando? ¿edito un fichero? |
| **Bucle del agente**            | La secuencia: lee tu prompt → decide acción → ejecuta script → lee resultado → te responde (o repite si hace falta) | Visible en el panel de chat, paso a paso |
| **Tool**                        | El terminal de VS Code que Copilot usa para correr `python3 ...`               | Copilot te pedirá aprobar el comando la primera vez — esa confirmación ES la frontera entre "el LLM decide" y "algo se ejecuta de verdad" |
| **Skill**                       | Cada carpeta en `.github/skills/`                                                | El `name` + `description` del SKILL.md es lo único que Copilot ve de entrada |
| **Descubrimiento progresivo**   | `analizador-csv`: el cuerpo del SKILL.md solo se carga si la descripción matchea; los ficheros en `referencia/` solo se leen si el propio SKILL.md le dice a Copilot que los lea en ese caso concreto | Compara cuántos ficheros lee Copilot con un CSV "limpio" vs uno "raro" |
| **Skills anidadas (general → específica)** | No la hemos montado todavía — es el reto 3 si quieres ampliarlo | — |
| **Instructions**                | `.github/copilot-instructions.md`                                               | Siempre está activo, no se "descubre" — compáralo con cómo se comporta una skill |
| **Memoria de sesión**           | El propio hilo de chat con Copilot                                              | Se pierde si abres un chat nuevo |
| **Ventana de contexto**         | Todo lo que Copilot ha cargado hasta ahora en este chat: tu prompt + instructions + skill cargada + resultado de scripts | Si encadenas muchas peticiones en el mismo chat, esto crece — es justo lo que tu mapa marca como riesgo de saturación |
| **Hooks**                       | No están en este repo (Copilot CLI/cloud agent los soporta, VS Code Agent mode no de forma nativa todavía) | — |

## Lo que NO está en este repo (a propósito)

- **MCP**: pediste no meterte ahí todavía.
- **Subagentes**: en Copilot esto se parece más a "Custom Agents" (`.agent.md`), que es un concepto algo distinto a los subagentes que viste en el curso de Anthropic. Cuando quieras, lo vemos aparte para no mezclar conceptos.
- **Hooks**: disponibles en Copilot CLI/cloud agent, no en VS Code Agent mode de forma nativa por ahora.
