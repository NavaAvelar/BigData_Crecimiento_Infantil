from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "datos" / "procesados" / "stunting_limpio.csv"
)

print("\nDimensiones:")
print(df.shape)

print("\nValores nulos:")
print(df.isnull().sum())

print("\nResumen estadístico:")
print(df.describe())

print("\nTop 10 países con mayor stunting:")

top10 = (
    df.sort_values("anio")
      .groupby("pais")
      .last()
      .sort_values("stunting", ascending=False)
      .head(10)
)

print(top10[["stunting"]])