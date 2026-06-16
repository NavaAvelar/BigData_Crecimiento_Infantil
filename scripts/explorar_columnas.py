from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

archivo = BASE_DIR / "datos" / "raw" / "stunting_unicef.xlsx"

df = pd.read_excel(
    archivo,
    sheet_name="Trend",
    header=8
)

for col in df.columns:
    if "_r" in col.lower():
        print(col)

print(df[['CountryName','CMRS_year']].head())
print(df[['CountryName','CMRS_year','National_r']].head())