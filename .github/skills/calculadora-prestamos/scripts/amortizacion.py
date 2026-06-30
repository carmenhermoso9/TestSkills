"""Calculadora de amortización de préstamos (sistema francés, cuota constante).

Uso:
    python3 amortizacion.py --principal 200000 --tasa-anual 0.03 --anios 20
"""
import argparse
import json


def calcular_cuota_mensual(principal: float, tasa_anual: float, anios: int) -> dict:
    """Calcula la cuota mensual constante de un préstamo con amortización francesa."""
    if tasa_anual == 0:
        cuota = principal / (anios * 12)
    else:
        tasa_mensual = tasa_anual / 12
        num_pagos = anios * 12
        cuota = principal * (tasa_mensual * (1 + tasa_mensual) ** num_pagos) / (
            (1 + tasa_mensual) ** num_pagos - 1
        )

    total_pagado = cuota * anios * 12
    total_intereses = total_pagado - principal

    return {
        "principal": principal,
        "tasa_anual": tasa_anual,
        "anios": anios,
        "cuota_mensual": round(cuota, 2),
        "total_pagado": round(total_pagado, 2),
        "total_intereses": round(total_intereses, 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora de amortización de préstamos")
    parser.add_argument("--principal", type=float, required=True)
    parser.add_argument("--tasa-anual", type=float, required=True, dest="tasa_anual")
    parser.add_argument("--anios", type=int, required=True)
    args = parser.parse_args()

    resultado = calcular_cuota_mensual(args.principal, args.tasa_anual, args.anios)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
