"""Calculadora de interés compuesto.

Uso:
    python3 interes_compuesto.py --capital 1000 --tasa 0.05 --anios 10
    python3 interes_compuesto.py --capital 1000 --tasa 0.05 --objetivo-multiplicador 2
"""
import argparse
import json
import sys


def calcular_evolucion(
    capital: float,
    tasa: float,
    anios: int,
    aportacion_anual: float = 0.0,
) -> list[dict]:
    """Devuelve el desglose año a año del capital con interés compuesto."""
    evolucion = []
    saldo = capital
    for anio in range(1, anios + 1):
        saldo = saldo * (1 + tasa) + aportacion_anual
        evolucion.append({"anio": anio, "saldo": round(saldo, 2)})
    return evolucion


def anios_para_multiplicar(capital: float, tasa: float, multiplicador: float) -> int:
    """Calcula cuántos años enteros se necesitan para multiplicar el capital por `multiplicador`."""
    saldo = capital
    anios = 0
    objetivo = capital * multiplicador
    while saldo < objetivo:
        saldo *= (1 + tasa)
        anios += 1
        if anios > 1000:
            raise ValueError("La tasa es demasiado baja o cero; no converge en un tiempo razonable.")
    return anios


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora de interés compuesto")
    parser.add_argument("--capital", type=float, required=True)
    parser.add_argument("--tasa", type=float, required=True, help="Decimal, ej. 0.05 para 5%%")
    parser.add_argument("--anios", type=int, help="Número de años a simular")
    parser.add_argument("--aportacion-anual", type=float, default=0.0)
    parser.add_argument(
        "--objetivo-multiplicador",
        type=float,
        help="Si se indica, calcula años para multiplicar el capital por este factor (ignora --anios)",
    )
    args = parser.parse_args()

    if args.objetivo_multiplicador is not None:
        anios = anios_para_multiplicar(args.capital, args.tasa, args.objetivo_multiplicador)
        resultado = {
            "modo": "objetivo_multiplicador",
            "capital_inicial": args.capital,
            "tasa": args.tasa,
            "multiplicador_objetivo": args.objetivo_multiplicador,
            "anios_necesarios": anios,
        }
    elif args.anios is not None:
        evolucion = calcular_evolucion(args.capital, args.tasa, args.anios, args.aportacion_anual)
        resultado = {
            "modo": "evolucion",
            "capital_inicial": args.capital,
            "tasa": args.tasa,
            "anios": args.anios,
            "aportacion_anual": args.aportacion_anual,
            "saldo_final": evolucion[-1]["saldo"] if evolucion else args.capital,
            "evolucion": evolucion,
        }
    else:
        print(json.dumps({"error": "Debes indicar --anios o --objetivo-multiplicador"}))
        sys.exit(1)

    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
