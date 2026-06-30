# Solución y comentario — Reto 4

## Ejercicio A

Diferencias esperadas, confirmadas contra el comportamiento documentado de VS Code:

- Con la **skill**, Copilot construye literalmente una línea de comando (`python3 .github/skills/.../interes_compuesto.py --capital 1000 --tasa 0.05 --anios 10`) y la pasa por la tool de terminal del propio editor. Lo que recibe de vuelta es texto plano (el stdout de tu script), que él mismo tiene que volver a interpretar como si leyera la salida de cualquier comando de shell.
- Con la **tool MCP**, Copilot nunca construye un string de comando. Llama directamente a la función `validar_dni` pasando `{"dni": "12345678Z"}` como argumentos ya tipados según el schema que el SDK de MCP genera automáticamente a partir de los type hints de tu función Python. La respuesta es un objeto estructurado, no texto que haya que parsear.

Esta es la diferencia de fondo con tu mapa: la skill usa la Tool genérica "terminal" del agente como intermediaria; el servidor MCP expone tools *específicas de tu dominio* directamente al agente.

## Ejercicio B

- `validar_dni("12345678A")` no es un error de ejecución — la función Python se ejecuta perfectamente y simplemente devuelve `valido: false` con un motivo. Esto es exactamente cómo deberías diseñar tools MCP en general: errores de negocio = parte del resultado, no excepciones.
- La skill de finanzas con el caso de amortización (Reto 1C) es más ambiguo porque no hay una señal estructurada de "esto no aplica" — depende de que la documentación en prosa del SKILL.md sea suficientemente clara y de que Copilot la respete.

Conclusión esperable: con la tool MCP, el agente tiene una señal binaria y explícita (`valido: true/false`) sobre la que razonar con certeza. Con la skill, depende de la interpretación de texto libre — más flexible pero menos fiable como contrato.

## Ejercicio C

Comportamiento esperado: Copilot debería hacer 3 llamadas independientes a `lista_compra_anadir` (una por producto) seguidas de una llamada a `lista_compra_ver`, aunque algunos modelos podrían intentar meter los tres productos en una sola llamada si interpretan mal el schema (la función solo acepta un `producto` por llamada, así que si lo intenta con una lista, fallaría o lo trataría como un string raro — es interesante ver cuál de los dos pasa).

Sobre persistencia:
- **Chat nuevo, servidor sin reiniciar:** la lista sigue ahí. El estado vive en el proceso de `server.py`, completamente independiente del historial de chat.
- **Servidor reiniciado:** la lista se vacía, porque `_lista_compra` es una variable Python normal en memoria — al matar el proceso, se pierde. No hay nada de persistencia en disco en este ejemplo a propósito, para que la diferencia con "memoria persistente" (que sí escribe a un store en disco) quede clara por contraste.

Si quisieras simular memoria persistente de verdad, el siguiente paso natural sería que `lista_compra_anadir` escribiera a un fichero JSON en disco en cada llamada, y lo leyera al arrancar — eso ya empieza a parecerse al concepto de "memory" persistente de tu mapa, distinto de la sesión.

## Reflexión final

No hay solución única aquí, es deliberadamente abierta. Lo único que vale la pena remarcar: cuantas más tools MCP definas con responsabilidades muy concretas (una función = una acción clara), más fácil le resulta al agente decidir cuál usar — el mismo principio de "descripción clara" que viste con las skills, aplicado ahora a la docstring de cada función Python, que es lo que el SDK usa para generar la descripción que el agente ve.
