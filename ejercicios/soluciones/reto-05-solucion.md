# Solución y comentario — Reto 5

## Ejercicio A

Comportamiento esperado: Copilot, al recibir tu petición, probablemente construya un comando como `rm -rf ejemplos_datos`. Antes de que aparezca el diálogo normal de "¿aprobar este comando?", el hook `PreToolUse` debería interceptarlo y VS Code debería mostrar el `reason` del bloqueo en vez de la confirmación habitual.

Este es el matiz importante que distingue un hook de todo lo demás que has visto: con una skill o una tool MCP, la "seguridad" depende de que la documentación (SKILL.md, docstring) sea lo bastante clara para que el LLM decida bien, y de que tú apruebes o no cada comando manualmente. Con el hook, el código se ejecuta siempre, sin pedirle opinión al LLM sobre si debería o no — es la diferencia entre "una buena práctica documentada" y "una regla forzada".

Si desactivas el hook (renombrando `hooks.json`) y repites la prueba, lo normal es que Copilot sí construya el comando igualmente y dependa solo del diálogo de confirmación de VS Code para frenarlo — que tú podrías aprobar por error si no lees con atención.

## Ejercicio B

Tras pedir el cálculo de interés compuesto, `hooks_log.jsonl` debería tener una línea como:

```json
{"timestamp": "2026-...", "comando": "python3 .github/skills/calculadora-finanzas/scripts/interes_compuesto.py --capital 3000 --tasa 0.04 --anios 5", "tool_name": "..."}
```

Sobre la reflexión: este tipo de log resuelve la parte de "no saber por dónde tocar algo si hace falta" de tu mapa — tienes un rastro determinista de qué se ejecutó y cuándo, útil para depurar o para auditoría de seguridad. Lo que NO resuelve: si el script se ejecutó con argumentos incorrectos pero el comando en sí no era peligroso (por ejemplo `--tasa` con un valor mal interpretado del prompt del usuario), el hook lo deja pasar igual — un hook de este tipo valida la forma del comando, no la corrección semántica del resultado. Para eso necesitarías otro tipo de control (tests, revisión humana del resultado, etc.) — la responsabilidad de calidad sigue siendo tuya, como dice tu propio mapa sobre el "nuevo rol".

## Ejercicio C

No hay una única solución correcta de código aquí porque depende del formato exacto del evento JSON en tu versión de VS Code (el formato puede variar entre eventos de terminal y eventos de edición de fichero). El paso recomendado del propio reto — loguear el evento crudo sin filtrar la primera vez — es la forma correcta de descubrirlo empíricamente en vez de adivinar la estructura.

Una vez tengas el formato real, una implementación de referencia razonable sería comprobar si el evento es de tipo edición de fichero (en vez de comando de terminal) y si la ruta del fichero cae dentro de `ejercicios/soluciones/`, bloqueando en ese caso con un `reason` claro — siguiendo exactamente el mismo patrón que la regla de `rm -rf` que ya tienes, solo que mirando una ruta de fichero en vez de un substring de comando.
