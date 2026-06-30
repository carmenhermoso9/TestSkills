"""Servidor MCP local mínimo, para entender function-calling real (tools con schema).

Corre por stdio (entrada/salida estándar) — no abre ningún puerto de red,
no sale de tu máquina. VS Code lo arranca como subproceso cuando lo
necesita y le habla por stdin/stdout.

3 tools de ejemplo, cada una pensada para enseñar algo distinto:

1. sumar            -> la más simple posible. Sirve para ver el mecanismo limpio:
                       Copilot manda argumentos tipados, la función los usa tal cual,
                       sin parsear texto ni argparse. Comparar con cómo lo hacíamos
                       en las skills (construir un comando de terminal con --flags).

2. validar_dni      -> tiene lógica de validación real y puede DEVOLVER UN ERROR
                       estructurado. Sirve para ver cómo reacciona el agente cuando
                       una tool falla: ¿reintenta con otro valor? ¿pregunta al usuario?
                       ¿se rinde y lo dice?

3. lista_compra     -> tiene ESTADO en memoria del proceso del servidor (una lista
                       que persiste mientras el servidor esté vivo, no por turno de
                       chat). Sirve para ver cómo el agente encadena varias llamadas
                       a tools distintas (anadir, listar, vaciar) para completar una
                       tarea de varios pasos sin que tú reescribas el estado cada vez.
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("test-tools")

# Estado en memoria para la tool 3. Vive mientras el proceso del servidor
# esté vivo. Si VS Code reinicia el servidor, se pierde -- es justo el
# mismo concepto de "memoria de sesion vs persistente" de tu mapa, pero
# aplicado al lado del servidor en vez de al lado del chat.
_lista_compra: list[str] = []


@mcp.tool()
def sumar(a: float, b: float) -> float:
    """Suma dos números y devuelve el resultado.

    Útil para verificar que el mecanismo de tool-calling funciona de punta
    a punta antes de probar tools más complejas.
    """
    return a + b


@mcp.tool()
def validar_dni(dni: str) -> dict:
    """Valida un DNI español (8 dígitos + letra de control).

    Devuelve un dict con 'valido': bool y, si no es válido, un 'motivo'
    explicando por qué. No lanza excepciones -- el error es parte del
    resultado, no un fallo de la tool.
    """
    letras_control = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni_limpio = dni.strip().upper().replace("-", "").replace(" ", "")

    if len(dni_limpio) != 9:
        return {
            "valido": False,
            "motivo": f"Debe tener 9 caracteres (8 dígitos + letra), tiene {len(dni_limpio)}.",
        }

    numero, letra = dni_limpio[:8], dni_limpio[8]

    if not numero.isdigit():
        return {"valido": False, "motivo": "Los primeros 8 caracteres deben ser dígitos."}

    if not letra.isalpha():
        return {"valido": False, "motivo": "El último carácter debe ser una letra."}

    letra_esperada = letras_control[int(numero) % 23]
    if letra != letra_esperada:
        return {
            "valido": False,
            "motivo": f"Letra de control incorrecta. Para el número {numero} debería ser '{letra_esperada}', no '{letra}'.",
        }

    return {"valido": True, "dni_normalizado": f"{numero}{letra}"}


@mcp.tool()
def lista_compra_anadir(producto: str, cantidad: int = 1) -> dict:
    """Añade un producto a la lista de la compra (estado en memoria del servidor)."""
    entrada = f"{producto} x{cantidad}" if cantidad != 1 else producto
    _lista_compra.append(entrada)
    return {"añadido": entrada, "total_items": len(_lista_compra)}


@mcp.tool()
def lista_compra_ver() -> dict:
    """Devuelve el contenido actual de la lista de la compra."""
    return {"items": list(_lista_compra), "total_items": len(_lista_compra)}


@mcp.tool()
def lista_compra_vaciar() -> dict:
    """Vacía la lista de la compra y devuelve cuántos items se eliminaron."""
    eliminados = len(_lista_compra)
    _lista_compra.clear()
    return {"items_eliminados": eliminados}


if __name__ == "__main__":
    mcp.run(transport="stdio")
