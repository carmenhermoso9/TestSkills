# Reto 4 — La misma tarea, dos mecanismos: Skill vs Tool MCP

**Objetivo:** ver con tus propios ojos la diferencia entre "Copilot construye un comando de terminal a partir de una skill" y "Copilot llama una función con argumentos estructurados via MCP".

Requisito: haber completado el setup de `mcp-server/README.md` y tener el servidor `testTools` arrancado y con sus tools activadas en VS Code.

## Ejercicio A — observar las dos rutas en paralelo

En un chat nuevo, pide:

> Valida el DNI 12345678Z usando la tool de MCP

Y en otro chat nuevo (o después, da igual):

> Calcula el interés compuesto de 1000€ al 5% en 10 años

Para cada una, fíjate en el panel de Copilot:

| | Skill (interés compuesto) | Tool MCP (validar DNI) |
|---|---|---|
| ¿Qué ves antes de la ejecución? | Un comando de terminal completo, con `--flags` | Un nombre de función + un objeto JSON de argumentos |
| ¿Cómo confirmas? | Aprobando un comando de shell | Aprobando una llamada a tool (suele verse distinto en la UI) |
| ¿Qué formato tiene la respuesta cruda? | Lo que tu script imprime por `print()` en stdout — texto que Copilot tiene que interpretar | Un objeto ya estructurado que devuelve la función Python directamente |

Esta tabla es la respuesta corta a "qué cambia realmente" — confírmala tú misma observando, no la copies sin probar.

## Ejercicio B — fuerza un error en cada mecanismo

Compara cómo se comporta cada mecanismo cuando algo va mal:

1. Pide validar un DNI claramente inválido: `12345678A`. La tool devuelve `{"valido": false, "motivo": "..."}` — no es un fallo de ejecución, es un resultado negativo válido.
2. Pide a la skill de finanzas algo fuera de su alcance documentado, como en el Reto 1 Ejercicio C (préstamo con cuotas).

Pregunta para reflexionar: ¿en cuál de los dos casos el agente tiene más información estructurada para decidir qué hacer a continuación (reintentar, preguntar, explicar)? El JSON tipado de una tool MCP suele dar pie a una reacción más predecible que el texto libre de un script por terminal — pero compruébalo tú, no lo asumas.

## Ejercicio C — encadenar varias tools (estado en memoria)

Pide, todo en una sola petición:

> Añade leche, pan y huevos a la lista de la compra. Después muéstrame la lista completa.

Observa:
- ¿Cuántas llamadas a tools hace Copilot? (Debería ser 3 `lista_compra_anadir` + 1 `lista_compra_ver`, o podría agrupar de otra forma — no hay una única manera correcta).
- Cierra el chat, abre uno nuevo, y pide solo "muéstrame la lista de la compra". ¿Sigue ahí? Debería, porque el estado vive en el proceso del servidor MCP, no en el chat — a diferencia de la "memoria de sesión" del propio chat de Copilot.
- Ahora reinicia el servidor MCP (botón Stop/Start en `.vscode/mcp.json`) y vuelve a pedir la lista. Debería estar vacía — el estado en memoria del proceso se perdió al reiniciar.

Esto reproduce de forma muy concreta la diferencia que tu mapa marca entre **memoria de sesión** (se pierde fácil) y algo más persistente — aquí con un matiz nuevo: la "sesión" relevante para el estado de esta tool es la vida del proceso del servidor, no la del chat.

## Reflexión final

Con lo que has visto en los retos 1-4, ¿en qué casos elegirías una skill con script por terminal, y en qué casos una tool MCP con schema? No hay una respuesta única correcta, pero una pista de la industria real: las skills suelen preferirse para flujos de trabajo con pasos y razonamiento (como hizo tu `analizador-csv`), y las tools MCP para operaciones puntuales bien definidas que se integran con sistemas externos reales (bases de datos, APIs, servicios).

Solución/comentario de referencia: `soluciones/reto-04-solucion.md`
