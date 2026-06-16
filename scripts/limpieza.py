from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

archivo = BASE_DIR / "datos" / "raw" / "stunting_unicef.xlsx"

df = pd.read_excel(
    archivo,
    sheet_name="Trend",
    header=8
)

columnas = [
    'CountryName',
    'UNICEF_Reporting_Sub_Region',
    'UNRegion',
    'WHORegion',
    'WB_Latest',
    'CMRS_year',
    'National_r',
    'male_r',
    'female_r',
    'urban_r',
    'rural_r',
    'Q1_r',
    'Q5_r',
    'meduc_none_r',
    'meduc_high_r'
]

df = df[columnas]

df.columns = [
    'pais',
    'subregion',
    'region_un',
    'region_who',
    'nivel_ingreso',
    'anio',
    'stunting',
    'stunting_hombres',
    'stunting_mujeres',
    'stunting_urbano',
    'stunting_rural',
    'quintil_pobre',
    'quintil_rico',
    'sin_educacion_madre',
    'educacion_superior_madre'
]

df = df.dropna(subset=['stunting'])

print(df.shape)

df.to_csv(
    BASE_DIR / "datos" / "procesados" / "stunting_limpio.csv",
    index=False
)

print("Archivo generado correctamente")