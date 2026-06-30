# Reto 5 — Hooks: la pieza que SÍ es determinista

**Objetivo:** comprobar que un hook se ejecuta siempre, sin depender de que el LLM "decida" hacerlo, y entender qué tipo de control te da eso que ni una skill ni una tool MCP te dan.

Esto reproduce literalmente la frase de tu mapa: *"la IA no es determinista — un hook sí garantiza algo siempre"*. Ojo: los hooks de VS Code están en **Preview** (llegaron en febrero 2026) — si tu versión de VS Code no los soporta todavía, actualízala antes de este reto.

## Qué hace el hook que ya tienes montado

`.github/hooks/hooks.json` registra un hook de tipo `PreToolUse`, que se dispara justo **antes** de que Copilot ejecute cualquier herramienta (terminal, edición, etc.). El script `.github/hooks/scripts/pre_tool_use_guard.py` aplica 3 reglas fijas, sin ningún LLM de por medio:

1. Si el comando contiene `rm -rf` → lo bloquea siempre, sin excepción.
2. Si el comando ejecuta un script de una de nuestras skills → lo deja pasar, pero lo anota en `.github/hooks/hooks_log.jsonl`.
3. Cualquier otro comando → lo deja pasar sin más.

## Ejercicio A — comprobar el bloqueo

Pide a Copilot, en modo Agent:

> Borra la carpeta ejemplos_datos con rm -rf

Predicción antes de probarlo: ¿crees que el hook bloqueará esto, o que Copilot ni siquiera construirá ese comando porque ya sabe que es peligroso?

Ejecuta y observa qué pasa. Si el hook funciona, deberías ver que VS Code rechaza el comando antes de pedirte aprobación a ti — la decisión se tomó por código, no porque Copilot "decidiera no hacerlo".

**El punto importante:** compara esto con pedirle lo mismo sin el hook activo (puedes desactivarlo momentáneamente renombrando `hooks.json` a `hooks.json.bak` y reiniciando la sesión). Sin el hook, todo depende de que el LLM, ese turno, decida no ejecutarlo o de que tú lo rechaces manualmente en el diálogo de confirmación. Con el hook, no depende de nada de eso.

## Ejercicio B — comprobar la auditoría

Pide cualquier tarea que dispare una skill, por ejemplo del Reto 1:

> Si invierto 3000 euros al 4% durante 5 años, ¿cuánto tendré?

Después, abre `.github/hooks/hooks_log.jsonl` (puede que tengas que crear el fichero la primera vez, o puede que ya exista tras la primera ejecución). Deberías ver una línea JSON con el comando exacto que se ejecutó y un timestamp.

Pregunta para reflexionar: si este log existiera en un proyecto real con muchas skills y muchas tools, ¿qué tipo de problemas de tu mapa ("Riesgo: perder el control del código") ayudaría a mitigar tener esta auditoría? ¿Y qué no resuelve (el hook no evalúa si el *resultado* del script es correcto, solo registra que se ejecutó)?

## Ejercicio C — añade tu propia regla

Modifica `pre_tool_use_guard.py` para añadir una cuarta regla: bloquear cualquier comando que intente modificar ficheros dentro de `ejercicios/soluciones/` (recuerda que las Instructions ya piden no tocarlos, pero eso depende de que el LLM las respete — con un hook lo garantizas en código).

Pista: el evento que llega por stdin también puede tener información sobre edición de ficheros, no solo comandos de terminal — la estructura exacta puede variar según la tool, así que un buen primer paso es loguear el JSON completo del evento crudo (sin filtrar nada) la primera vez, para ver qué pinta tiene de verdad en tu versión de VS Code, en vez de asumir el formato.

Solución/comentario de referencia: `soluciones/reto-05-solucion.md`
