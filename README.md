# TestSkills

Repo de práctica para entender, a bajo nivel y con GitHub Copilot Agent Mode (VS Code), cómo un agente decide usar **Skills**, **Instructions** y herramientas del editor (tools) durante el bucle agente → acción → resultado.

No usamos MCP ni subagentes aquí — eso es para otro repo. Esto es solo: prompt → agente → ¿qué carga y por qué? → resultado.

## 0. Requisitos antes de empezar

1. VS Code actualizado (1.108+, idealmente la última estable — Agent Skills llegó a estable en enero 2026).
2. Extensión GitHub Copilot + Copilot Chat instaladas y con sesión iniciada.
3. Python 3.10+ en el PATH (`python3 --version`).
4. Clona este contenido dentro de tu repo vacío `carmenhermoso9/TestSkills`.

```bash
git clone https://github.com/carmenhermoso9/TestSkills.git
cd TestSkills
# copia aquí el contenido que te entrego
git add .
git commit -m "Estructura base: skills, instructions, ejercicios"
git push
```

5. Abre la carpeta en VS Code, abre Copilot Chat, y pon el modo en **Agent** (no Ask, no Edit).

## 1. Qué hay en este repo

```
.github/
  copilot-instructions.md          ← Instructions globales del proyecto (siempre activas)
  skills/
    calculadora-finanzas/
      SKILL.md                     ← Skill sencilla, un único script
      scripts/interes_compuesto.py
    analizador-csv/
      SKILL.md                     ← Skill con descubrimiento progresivo real (varios ficheros)
      scripts/analizar.py
      referencia/formulas.md
      referencia/columnas_esperadas.md
docs/
  conceptos.md                     ← Chuleta: qué pieza de tu mapa corresponde a qué fichero aquí
ejercicios/
  reto-01-tool-simple.md
  reto-02-skill-progresiva.md
  reto-03-instructions-vs-skill.md
  soluciones/                      ← No los abras hasta intentarlo tú primero
```

## 2. Cómo "ver" el bucle del agente en acción

Esto es lo importante. Para cada ejercicio, antes de pedirle nada a Copilot:

1. **Predice** qué va a hacer (¿usará la skill? ¿la ignorará? ¿por qué?).
2. Pide la tarea en Copilot Chat (modo Agent).
3. Observa en el panel de chat:
   - Si aparece un indicador de que cargó una skill (suele mostrarlo como paso expandible).
   - Qué herramienta del editor ejecuta (terminal, lectura de fichero, edición...).
   - Si te pide confirmación antes de ejecutar un script (por seguridad, Copilot pide aprobar comandos de terminal la primera vez).
4. **Compara** con tu predicción. Si falló, esa es la parte interesante: ¿la `description` de la skill era ambigua? ¿el prompt no daba pistas suficientes?

Esto reproduce exactamente lo que tu mapa llama "descubrimiento progresivo": Copilot solo tiene `name` + `description` de cada skill en su contexto inicial — el resto se carga solo si decide que aplica.

## 3. Orden recomendado

1. Lee `docs/conceptos.md` (2 min, mapea tu diagrama a este repo).
2. Haz `ejercicios/reto-01-tool-simple.md`.
3. Haz `ejercicios/reto-02-skill-progresiva.md`.
4. Haz `ejercicios/reto-03-instructions-vs-skill.md`.
5. Cuando quieras más, dime y montamos retos de subagentes o un servidor MCP mínimo (lo dejamos para cuando te sientas cómoda con esto).
