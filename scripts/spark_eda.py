from pyspark.sql import SparkSession

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("EDA Stunting") \
    .getOrCreate()

# Leer dataset
df = spark.read.csv(
    "datos/procesados/stunting_bigdata.csv",
    header=True,
    inferSchema=True
)

print("\nESQUEMA")
df.printSchema()

print("\nTOTAL DE REGISTROS")
print(df.count())

print("\nPRIMERAS FILAS")
df.show(5)

print("\nESTADISTICAS GENERALES")
df.describe().show()

print("\nSTUNTING POR ZONA")
df.groupBy("zona") \
  .avg("stunting") \
  .show()

print("\nSTUNTING POR INGRESO")
df.groupBy("quintil_ingreso") \
  .avg("stunting") \
  .show()

print("\nSTUNTING POR EDUCACION DE LA MADRE")
df.groupBy("educacion_madre") \
  .avg("stunting") \
  .show()

print("\nDISTRIBUCIÓN DE LA VARIABLE OBJETIVO")
df.groupBy("stunting").count().show()

print("\nSTUNTING POR SEXO")
df.groupBy("sexo").avg("stunting").show()

print("\nSTUNTING POR ACCESO AL AGUA")
df.groupBy("acceso_agua").avg("stunting").show()

print("\nSTUNTING POR VACUNACIÓN")
df.groupBy("vacunacion").avg("stunting").show()

spark.stop()