# TestSkills

Repo de práctica para entender, a bajo nivel y con GitHub Copilot Agent Mode (VS Code), cómo un agente decide usar **Skills**, **Tools (vía MCP)**, **Instructions** y **Hooks** durante el bucle agente → acción → resultado.

No usamos subagentes todavía — eso queda para más adelante. Esto cubre el resto del mapa: prompt → agente → ¿qué carga y por qué? → resultado → ¿qué garantiza código determinista que el LLM no puede saltarse?

## 0. Requisitos antes de empezar

1. VS Code actualizado (última estable — algunas piezas como Hooks están en Preview y llegaron en febrero 2026, así que cuanto más reciente mejor).
2. Extensión GitHub Copilot + Copilot Chat instaladas y con sesión iniciada.
3. Python 3.10+ en el PATH (`python3 --version`).
4. Clona este contenido dentro de tu repo `carmenhermoso9/TestSkills`.

```bash
git clone https://github.com/carmenhermoso9/TestSkills.git
cd TestSkills
# copia aquí el contenido que te entrego
git add .
git commit -m "Estructura base: skills, instructions, hooks, mcp, ejercicios"
git push
```

5. Para el servidor MCP (Reto 4 en adelante), sigue el setup de `mcp-server/README.md` antes de continuar — necesita un paso manual de instalación que no se sube a git.
6. Abre la carpeta en VS Code, abre Copilot Chat, y pon el modo en **Agent** (no Ask, no Edit).

## 1. Qué hay en este repo

```
.github/
  copilot-instructions.md          ← Instructions globales del proyecto (siempre activas)
  hooks/
    hooks.json                     ← Configuración del hook PreToolUse
    scripts/pre_tool_use_guard.py  ← Lógica determinista: bloquea rm -rf, audita ejecuciones de skills
  skills/
    calculadora-finanzas/          ← Skill sencilla (interés compuesto, capital único)
    calculadora-prestamos/         ← Skill que se solapa a propósito con la anterior (amortización con cuotas)
    analizador-csv/                ← Skill con descubrimiento progresivo real (3 niveles de carga)
mcp-server/
  server.py                        ← Servidor MCP local con 3 tools reales (function-calling con schema)
  README.md                        ← Setup del entorno virtual y activación en VS Code
.vscode/
  mcp.json                         ← Config para que VS Code arranque el servidor MCP local
docs/
  conceptos.md                     ← Chuleta: qué pieza de tu mapa corresponde a qué fichero aquí
ejercicios/
  reto-01-tool-simple.md           ← Bucle básico agente → terminal → resultado
  reto-02-skill-progresiva.md      ← Descubrimiento progresivo de una skill
  reto-03-instructions-vs-skill.md ← Instructions siempre activas vs skill condicional, + crea tu skill
  reto-04-tool-vs-skill.md         ← Comparación directa: script por terminal vs tool MCP con schema
  reto-05-hooks.md                 ← Hooks: la única pieza 100% determinista
  reto-06-desambiguacion-skills.md ← Qué pasa cuando dos skills podrían aplicar a la misma petición
  reto-07-ventana-contexto.md      ← Crecimiento y saturación de la ventana de contexto en una sesión larga
  soluciones/                      ← No los abras hasta intentarlo tú primero
```

## 2. Cómo "ver" el bucle del agente en acción

Esto es lo importante. Para cada ejercicio, antes de pedirle nada a Copilot:

1. **Predice** qué va a hacer (¿usará la skill? ¿la tool MCP? ¿la ignorará? ¿por qué?).
2. Pide la tarea en Copilot Chat (modo Agent).
3. Observa en el panel de chat (o en `Developer: Open Agent Debug Panel` si tu versión lo tiene):
   - Si aparece un indicador de que cargó una skill.
   - Si aparece una llamada a una tool MCP con sus argumentos estructurados.
   - Qué herramienta del editor ejecuta (terminal, lectura de fichero, edición...).
   - Si te pide confirmación antes de ejecutar algo.
4. **Compara** con tu predicción. La parte interesante siempre es cuando falla: ¿la `description` era ambigua? ¿el prompt no daba pistas suficientes? ¿el hook bloqueó algo que no esperabas?

## 3. Orden recomendado

1. Lee `docs/conceptos.md` (2 min, mapea tu diagrama a este repo).
2. Retos 1, 2 y 3 — Skills e Instructions (no necesitan MCP ni hooks).
3. Setup de `mcp-server/README.md`, luego Reto 4 — Tools reales vía MCP.
4. Reto 5 — Hooks.
5. Reto 6 — Desambiguación entre skills que se solapan.
6. Reto 7 — Ventana de contexto en una sesión larga.
7. Cuando quieras más, dime y vemos subagentes — lo dejamos pendiente a propósito.

