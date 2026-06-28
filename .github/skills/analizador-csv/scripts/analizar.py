"""Analizador de CSV de ventas/gastos.

Uso:
    python3 analizar.py --csv datos.csv
    python3 analizar.py --csv datos.csv --mapeo "Fecha de venta=fecha" --mapeo "Cantidad EUR=importe"
"""
import argparse
import csv
import json
import os
import unicodedata
from collections import defaultdict

COLUMNAS_CANONICAS = {
    "fecha": ["fecha", "date", "dia"],
    "categoria": ["categoria", "category", "tipo"],
    "importe": ["importe", "monto", "total", "amount", "precio"],
}


def _normalizar(texto: str) -> str:
    """Quita tildes y pasa a minúsculas para comparar nombres de columnas."""
    sin_tildes = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return sin_tildes.strip().lower()


def detectar_mapeo(columnas_csv: list[str], mapeo_manual: dict[str, str]) -> tuple[dict[str, str], list[str]]:
    """Intenta mapear columnas del CSV a nombres canónicos. Devuelve (mapeo, faltantes)."""
    mapeo: dict[str, str] = {}

    # Primero aplicar mapeo manual indicado por el usuario
    for col_csv, canonico in mapeo_manual.items():
        if col_csv in columnas_csv:
            mapeo[canonico] = col_csv

    # Luego autodetección para lo que no se haya mapeado ya
    columnas_normalizadas = {_normalizar(c): c for c in columnas_csv}
    for canonico, variantes in COLUMNAS_CANONICAS.items():
        if canonico in mapeo:
            continue
        for variante in variantes:
            if variante in columnas_normalizadas:
                mapeo[canonico] = columnas_normalizadas[variante]
                break

    faltantes = [c for c in COLUMNAS_CANONICAS if c not in mapeo]
    return mapeo, faltantes


def analizar(ruta_csv: str, mapeo_manual: dict[str, str]) -> dict:
    if not os.path.isfile(ruta_csv):
        return {"error": f"No existe el fichero: {ruta_csv}"}

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        filas = list(lector)
        columnas_csv = lector.fieldnames or []

    if not filas:
        return {"error": "El CSV no tiene filas de datos", "columnas_detectadas": columnas_csv}

    mapeo, faltantes = detectar_mapeo(columnas_csv, mapeo_manual)

    resultado = {
        "num_filas": len(filas),
        "columnas_detectadas": columnas_csv,
        "mapeo_aplicado": mapeo,
        "columnas_faltantes": faltantes,
        "avisos": [],
        "muestra_filas": filas[:3],
    }

    if "importe" in mapeo:
        col_importe = mapeo["importe"]
        valores = []
        for fila in filas:
            crudo = fila.get(col_importe, "").replace(",", ".").replace("€", "").strip()
            try:
                valores.append(float(crudo))
            except ValueError:
                resultado["avisos"].append(f"Valor no numérico en importe: '{fila.get(col_importe)}'")

        if valores:
            resultado["total_importe"] = round(sum(valores), 2)
            resultado["media_importe"] = round(sum(valores) / len(valores), 2)
            resultado["max_importe"] = max(valores)
            resultado["min_importe"] = min(valores)

        if "categoria" in mapeo:
            col_cat = mapeo["categoria"]
            totales_por_categoria: dict[str, float] = defaultdict(float)
            for fila in filas:
                crudo = fila.get(col_importe, "").replace(",", ".").replace("€", "").strip()
                try:
                    valor = float(crudo)
                except ValueError:
                    continue
                cat = fila.get(col_cat, "(sin categoría)")
                totales_por_categoria[cat] += valor
            resultado["total_por_categoria"] = {
                k: round(v, 2) for k, v in sorted(totales_por_categoria.items(), key=lambda kv: -kv[1])
            }

    return resultado


def main() -> None:
    parser = argparse.ArgumentParser(description="Analizador de CSV de ventas/gastos")
    parser.add_argument("--csv", required=True, help="Ruta al fichero CSV")
    parser.add_argument(
        "--mapeo",
        action="append",
        default=[],
        help='Mapeo manual columna_csv=canonico, ej. "Cantidad EUR=importe". Se puede repetir.',
    )
    args = parser.parse_args()

    mapeo_manual = {}
    for item in args.mapeo:
        if "=" not in item:
            print(json.dumps({"error": f"Formato de --mapeo inválido: '{item}', usa columna_csv=canonico"}))
            return
        col_csv, canonico = item.split("=", 1)
        mapeo_manual[col_csv.strip()] = canonico.strip()

    resultado = analizar(args.csv, mapeo_manual)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
