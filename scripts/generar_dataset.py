from pathlib import Path
import pandas as pd
import numpy as np

N = 500000

np.random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent

# Variables

df = pd.DataFrame()

df["id"] = range(1, N + 1)

df["edad_meses"] = np.random.randint(6, 60, N)

df["sexo"] = np.random.choice(
    ["M", "F"],
    N
)

df["zona"] = np.random.choice(
    ["Urbana", "Rural"],
    N,
    p=[0.65, 0.35]
)

df["quintil_ingreso"] = np.random.choice(
    ["Muy_Bajo", "Bajo", "Medio", "Alto", "Muy_Alto"],
    N,
    p=[0.20, 0.25, 0.25, 0.20, 0.10]
)

df["educacion_madre"] = np.random.choice(
    ["Ninguna", "Primaria", "Secundaria", "Superior"],
    N,
    p=[0.10, 0.30, 0.40, 0.20]
)

df["acceso_agua"] = np.random.choice(
    ["Si", "No"],
    N,
    p=[0.85, 0.15]
)

df["vacunacion"] = np.random.choice(
    ["Completa", "Incompleta"],
    N,
    p=[0.80, 0.20]
)

# Peso y estatura

df["peso_kg"] = np.round(
    np.random.normal(12, 3, N),
    1
)

df["estatura_cm"] = np.round(
    np.random.normal(88, 10, N),
    1
)

# Evitar valores absurdos

df["peso_kg"] = df["peso_kg"].clip(5, 30)

df["estatura_cm"] = df["estatura_cm"].clip(55, 130)

# Riesgo de stunting

riesgo = np.zeros(N)

riesgo += np.where(df["zona"] == "Rural", 2, 0)

riesgo += np.where(df["quintil_ingreso"] == "Muy_Bajo", 3, 0)
riesgo += np.where(df["quintil_ingreso"] == "Bajo", 2, 0)

riesgo += np.where(df["educacion_madre"] == "Ninguna", 3, 0)
riesgo += np.where(df["educacion_madre"] == "Primaria", 1, 0)

riesgo += np.where(df["acceso_agua"] == "No", 2, 0)

riesgo += np.where(df["vacunacion"] == "Incompleta", 2, 0)

riesgo += np.where(df["estatura_cm"] < 80, 4, 0)

# Conversión a etiqueta

probabilidad = riesgo / riesgo.max()

df["stunting"] = (
    np.random.rand(N) < probabilidad
).astype(int)

# Guardar

salida = BASE_DIR / "datos" / "procesados" / "stunting_bigdata.csv"

df.to_csv(
    salida,
    index=False
)

print("\nDataset generado correctamente")
print(df.shape)
print("\nArchivo:")
print(salida)