import os
import pandas as pd

RUTA_ENTRADA = 'data/raw/ventas_generadas.csv'
RUTA_SALIDA = 'data/processed/ventas_limpias.xlsx'
DIAS = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

df = pd.read_csv(RUTA_ENTRADA)

print(df.head())

# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())

df["fecha"] = pd.to_datetime(df["fecha"])

df["cliente"] = (
    df["cliente"]
    .str.replace(r"^\w+(\(a\))?\.\s+", "", regex=True)
    .str.strip()
)
print("Clientes con punto (prefijos sin limpiar):", df["cliente"].str.contains(r"\.").sum())

diferencia = (df["cantidad"] * df["precio_unitario"] - df["monto_total"]).abs()
print("Filas donde el monto no coincide:", (diferencia > 0.01).sum())
