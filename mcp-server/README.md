# mcp-server — Tools reales (function-calling) para Copilot Agent mode

Esto es lo que en tu mapa conceptual aparece como **Tool**: una función que se ejecuta fuera del LLM, con un input y output determinados por un schema — pero, a diferencia de las skills del repo principal (que envuelven un script invocado por terminal), aquí Copilot llama a la función pasándole **argumentos estructurados y tipados**, sin que él tenga que construir un comando de texto.

## Las 3 tools, y qué te van a enseñar cada una

| Tool | Qué hace | Qué deberías observar |
|------|----------|------------------------|
| `sumar` | Suma dos números | El mecanismo más limpio posible: Copilot manda `{"a": 10, "b": 5}` directamente, sin parsear ni construir ningún string de comando |
| `validar_dni` | Valida un DNI español y explica por qué falla si no es válido | Cómo reacciona Copilot cuando una tool devuelve un resultado de "fallo" sin que la llamada en sí falle — el error es parte de la respuesta, no una excepción |
| `lista_compra_anadir` / `_ver` / `_vaciar` | Mantienen una lista en memoria del propio proceso del servidor | Cómo Copilot encadena varias llamadas a tools distintas para completar una tarea de varios pasos, y qué pasa con ese estado si reinicias el servidor |

## Setup (una vez, en tu máquina)

El entorno virtual de Python **no se sube a git** (está en `.gitignore`), así que tienes que crearlo tú la primera vez:

```bash
cd mcp-server
python3 -m venv .venv
.venv/bin/pip install "mcp[cli]"
```

Verifica que arranca sin errores (Ctrl+C para salir, si se queda esperando es buena señal — significa que está escuchando por stdio):

```bash
.venv/bin/python3 server.py
```

## Activarlo en VS Code

Ya tienes `.vscode/mcp.json` configurado en la raíz del repo, apuntando al Python de este venv. Pasos:

1. Abre el repo en VS Code.
2. VS Code debería detectar `.vscode/mcp.json` y mostrar un botón **Start** encima de la definición del servidor `testTools` dentro de ese fichero — ábrelo y pulsa Start.
3. Abre Copilot Chat en modo **Agent**.
4. Pulsa el icono de herramientas (tools) en la caja de chat — deberías ver `testTools` con sus 5 tools listadas. Confírmalas si están desactivadas.

Si algo no aparece, comprueba primero que la ruta `mcp-server/.venv/bin/python3` existe (en Windows sería `mcp-server\.venv\Scripts\python.exe` — si usas Windows, edita `command` en `mcp.json` en consecuencia).

## Primeras pruebas sugeridas

> Usa la tool sumar para sumar 17 y 25

> Valida este DNI: 12345678Z

> Valida este DNI: 12345678A

> Añade leche y pan a la lista de la compra, luego muéstrame la lista

Después de probar esto, pasa a `../ejercicios/reto-04-tool-vs-skill.md` para la comparación directa con las skills que ya tienes.
