"""Conversor de temperatura entre Celsius, Fahrenheit y Kelvin.

Uso:
    python convertir.py --valor 20 --desde C --hasta F
"""
import argparse
import json

CERO_ABSOLUTO_C = -273.15


def a_celsius(valor: float, unidad: str) -> float:
    if unidad == "C":
        return valor
    if unidad == "F":
        return (valor - 32) * 5 / 9
    if unidad == "K":
        return valor - 273.15
    raise ValueError(f"Unidad no soportada: {unidad}")


def desde_celsius(valor_c: float, unidad: str) -> float:
    if unidad == "C":
        return valor_c
    if unidad == "F":
        return valor_c * 9 / 5 + 32
    if unidad == "K":
        return valor_c + 273.15
    raise ValueError(f"Unidad no soportada: {unidad}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Conversor de temperatura")
    parser.add_argument("--valor", type=float, required=True)
    parser.add_argument("--desde", required=True, choices=["C", "F", "K"])
    parser.add_argument("--hasta", required=True, choices=["C", "F", "K"])
    args = parser.parse_args()

    valor_c = a_celsius(args.valor, args.desde)
    if valor_c < CERO_ABSOLUTO_C:
        print(
            json.dumps(
                {
                    "error": (
                        f"{args.valor}{args.desde} está por debajo del cero absoluto "
                        f"({CERO_ABSOLUTO_C}°C). No es una temperatura física válida."
                    )
                },
                ensure_ascii=False,
            )
        )
        return

    resultado = desde_celsius(valor_c, args.hasta)
    print(
        json.dumps(
            {
                "valor_original": args.valor,
                "unidad_original": args.desde,
                "valor_convertido": round(resultado, 2),
                "unidad_destino": args.hasta,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
