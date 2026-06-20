# Detección de Retraso en el Crecimiento Infantil mediante Big Data Y Spark ML
Este proyecto desarrolla un pipeline de Big Data para el análisis y predicción del retraso en el crecimiento infantil utilizando Apache Spark MLlib. El objetivo del proyecto es diseñar e implementar un pipeline de Big Data para el análisis y modelado predictivo del retraso en el crecimiento infantil stunting, integrando procesos de adquisición, limpieza y transformación de datos provenientes de UNICEF, generación de un conjunto de datos sintético de gran volumen, análisis exploratorio distribuido mediante Apache Spark, construcción y evaluación de modelos de aprendizaje automático utilizando Spark MLlib, y desarrollo de un dashboard en Power BI para la visualizcación e interpretación de los resultados obtenidos. 

## Estructura 
La estructura del repositorio esta constituida por las siguientes carpetas:

-datos
procesados: stunting_limpio.csv y stunting_bigdata.csv 
raw: dataset_unicef.xlsx

-scripts
explorar_columnas.py
limpieza.py
exploracion.py
generar_dataset.py
spark_eda.py
spark_model.py

-dashboard
Visualización de resultados.pdf
Visualización del conjunto creado.pdf
Visualización del conjunto original.pdf

-resporte 

ProyectoBigData.pdf

## Dependencias principales

El proyecto requiere las siguientes bibliotecas de Python:

- pandas
- numpy
- openpyxl
- pyspark
- matplotlib
- seaborn
- scikit-learn

Instalar dependendencias en caso de no tenerlas:

```bash
pip install -r requirements.txt


1. Clonar el repositorio
   
- git clone git clone https://github.com/NavaAvelar/BigData_Crecimiento_Infantil.git
- cd BigData_Crecimiento_Infantil

3. Crear entorno virtual desde Ubuntu (estas pueden ser opcionales)

- python3 -m venv venv
Arctivar entorno 
- source venv/bin/activate

5. Explorar el dataset original

- python scripts/explorar_columnas.py

7. Limpiar los datos

- python scripts/limpieza.py 
- genera:stunting_limpio.csv

9. Exploración del conjunto stunting_limpio

- python scripts/exploracion.py

11. Generar dataset sintético

- python scripts/generar_dataset.py
- genera:stunting_bigdata.csv

12. Análisis exploratorio con Spark

- spark-submit scripts/spark_eda.py

13. Entrenar modelos predictivos

- spark-submit scripts/spark_model.py

### Nota para el punto 12 y 13 puede requerir cambiar la ruta 

En algunos entornos de Apache Spark puede ser necesario especificar la ruta absoluta del archivo utilizando el prefijo `file:///`.

Ejemplo:

- file:///home/USUARIO/BigData_Crecimiento_Infantil/datos/procesados/stunting_bigdata.csv

Sustituya `USUARIO` por el nombre de usuario correspondiente a su sistema.

Para cambiar la ruta necesita entrar a los archivos, puede hacerlo con  nano scripts/spark_eda.py o nano scripts/spark_model.py

## Modelos implementados

- Regresión Logística
- Árbol de Decisión
- Random Forest

## Métricas evaluadas

- Accuracy
- Precision
- Recall
- F1-score


##Equipo 
Jazmín Nava Polvo y
Dana María Nava Avelar 
