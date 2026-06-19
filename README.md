# Detección de Retraso en el Crecimiento Infantil mediante Big Data Y Spark ML
Este proyecto desarrolla un pipeline de Big Data para el análisis y predicción del retraso en el crecimiento infantil utilizando Apache Spark MLlib. El objetivo del proyecto es diseñar e implementar un pipeline de Big Data para el análisis y modelado predictivo del retraso en el crecimiento infantil stunting, integrando procesos de adquisición, limpieza y transformación de datos provenientes de UNICEF, generación de un conjunto de datos sintético de gran volumen, análisis exploratorio distribuido mediante Apache Spark, construcción y evaluación de modelos de aprendizaje automático utilizando Spark MLlib, y desarrollo de un dashboard en Power BI para la visualizcación e interpretación de los resultados obtenidos. 

#Estructura 
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

-resporte 
ProyectoBigData.pdf

1. Clonar el repositorio
git clone https://github.com/usuario/proyecto-bigdata-stunting.git
cd proyecto-bigdata-stunting
3. Crear entorno virtual desde Ubuntu
python3 -m venv venv source venv/bin/activate
4. Explorar el dataset original
python scripts/explorar_columnas.py
5. Limpiar los datos
python scripts/limpieza.py 
genera:stunting_limpio.csv
6. Exploración del conjunto stunting_limpio
python scripts/exploracion.py
7. Generar dataset sintético 

#Equipo 
Jazmín Nava Polvo y
Dana María Nava Avelar 
