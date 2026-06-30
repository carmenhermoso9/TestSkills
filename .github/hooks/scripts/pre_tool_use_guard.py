#!/usr/bin/env python3
"""Hook PreToolUse: se ejecuta justo ANTES de que Copilot corra cualquier
herramienta (terminal, edición de fichero, etc.), y decide si la deja pasar.

Esto es lo que tu mapa llama: "la IA no es determinista, un hook sí
garantiza algo siempre". El LLM puede decidir distinto cada vez si ejecutar
algo con cuidado o no -- este script no decide nada con un LLM, es código
Python normal que aplica la misma regla siempre, sin excepción.

VS Code le pasa por stdin un JSON con información sobre la tool que está
a punto de ejecutarse. El hook debe imprimir un JSON por stdout. Si el JSON
de salida incluye {"decision": "block", "reason": "..."}, VS Code impide
la ejecución y muestra el motivo a Copilot (que normalmente lo explica al
usuario y prueba otra cosa).

Reglas de este hook (deliberadamente simples, para que se entiendan a simple vista):

1. Si el comando de terminal contiene "rm -rf" -> bloquear siempre.
2. Si el comando ejecuta uno de los scripts de nuestras skills -> dejar pasar,
   pero registrar la llamada en hooks_log.jsonl (auditoría).
3. Cualquier otra cosa -> dejar pasar sin más.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path(__file__).parent.parent / "hooks_log.jsonl"


def main() -> None:
    raw_input = sys.stdin.read()
    try:
        evento = json.loads(raw_input) if raw_input.strip() else {}
    except json.JSONDecodeError:
        evento = {"_raw_input_no_parseable": raw_input}

    comando = ""
    tool_input = evento.get("tool_input", {})
    if isinstance(tool_input, dict):
        comando = tool_input.get("command", "") or ""

    # Regla 1: bloquear comandos destructivos, siempre, sin excepción.
    if "rm -rf" in comando:
        salida = {
            "decision": "block",
            "reason": (
                "Bloqueado por hook de seguridad: el comando contiene 'rm -rf'. "
                "Este repo de pruebas no permite borrados recursivos automáticos."
            ),
        }
        print(json.dumps(salida, ensure_ascii=False))
        return

    # Regla 2: si es uno de nuestros scripts de skill, lo registramos.
    es_script_de_skill = ".github/skills" in comando and comando.strip().startswith("python")
    if es_script_de_skill:
        entrada_log = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "comando": comando,
            "tool_name": evento.get("tool_name", "desconocido"),
        }
        try:
            with open(LOG_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(entrada_log, ensure_ascii=False) + "\n")
        except OSError:
            pass  # Si el log falla, no bloqueamos la tarea del usuario por eso.

    # Regla 3 (implícita): si no se bloqueó arriba, se deja pasar sin más.
    print(json.dumps({"decision": "allow"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
