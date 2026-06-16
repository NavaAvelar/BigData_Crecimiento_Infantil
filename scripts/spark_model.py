from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("Modelos Stunting") \
    .getOrCreate()


df = spark.read.csv(
    "datos/procesados/stunting_bigdata.csv",
    header=True,
    inferSchema=True
)

print("\nTOTAL DE REGISTROS")
print(df.count())

print("\nDISTRIBUCION DE LA VARIABLE OBJETIVO")
df.groupBy("stunting").count().show()

# Variables categóricas
columnas_categoricas = [
    "sexo",
    "zona",
    "quintil_ingreso",
    "educacion_madre",
    "acceso_agua",
    "vacunacion"
]

for columna in columnas_categoricas:

    indexer = StringIndexer(
        inputCol=columna,
        outputCol=columna + "_idx",
        handleInvalid="keep"
    )

    df = indexer.fit(df).transform(df)

# Variables predictoras
features = [
    "edad_meses",
    "sexo_idx",
    "zona_idx",
    "quintil_ingreso_idx",
    "educacion_madre_idx",
    "acceso_agua_idx",
    "vacunacion_idx",
    "peso_kg",
    "estatura_cm"
]

assembler = VectorAssembler(
    inputCols=features,
    outputCol="features"
)

df = assembler.transform(df)

# División entrenamiento/prueba
train, test = df.randomSplit([0.8, 0.2], seed=42)

print("\nREGISTROS ENTRENAMIENTO")
print(train.count())

print("\nREGISTROS PRUEBA")
print(test.count())


accuracy_eval = MulticlassClassificationEvaluator(
    labelCol="stunting",
    predictionCol="prediction",
    metricName="accuracy"
)

precision_eval = MulticlassClassificationEvaluator(
    labelCol="stunting",
    predictionCol="prediction",
    metricName="weightedPrecision"
)

recall_eval = MulticlassClassificationEvaluator(
    labelCol="stunting",
    predictionCol="prediction",
    metricName="weightedRecall"
)

f1_eval = MulticlassClassificationEvaluator(
    labelCol="stunting",
    predictionCol="prediction",
    metricName="f1"
)


def evaluar_modelo(nombre, modelo, train, test):

    print(f"\n{'='*40}")
    print(nombre)
    print(f"{'='*40}")

    modelo_entrenado = modelo.fit(train)

    predicciones = modelo_entrenado.transform(test)

    accuracy = accuracy_eval.evaluate(predicciones)
    precision = precision_eval.evaluate(predicciones)
    recall = recall_eval.evaluate(predicciones)
    f1 = f1_eval.evaluate(predicciones)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nMATRIZ DE CONFUSION")

    predicciones.groupBy(
        "stunting",
        "prediction"
    ).count().orderBy(
        "stunting",
        "prediction"
    ).show()

    return {
        "modelo": nombre,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "predicciones": predicciones
    }

# REGRESIÓN LOGISTICA

lr = LogisticRegression(
    featuresCol="features",
    labelCol="stunting",
    maxIter=20
)

resultado_lr = evaluar_modelo(
    "REGRESIÓN LOGÍSTICA",
    lr,
    train,
    test
)

conf_lr = resultado_lr["predicciones"].groupBy(
    "stunting", "prediction"
).count()

conf_lr.write.mode("overwrite").csv("/tmp/confusion_lr")

# ÁRBOL DE DECISIÓN

dt = DecisionTreeClassifier(
    featuresCol="features",
    labelCol="stunting",
    maxDepth=8
)

resultado_dt = evaluar_modelo(
    "ÁRBOL DE DECISIÓN",
    dt,
    train,
    test
)

conf_dt = resultado_dt["predicciones"].groupBy(
    "stunting", "prediction"
).count()

conf_dt.write.mode("overwrite").csv("/tmp/confusion_dt")

# RANDOM FOREST

rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="stunting",
    numTrees=50,
    maxDepth=8
)

resultado_rf = evaluar_modelo(
    "RANDOM FOREST",
    rf,
    train,
    test
)

conf_rf = resultado_rf["predicciones"].groupBy(
    "stunting", "prediction"
).count()

conf_rf.write.mode("overwrite").csv("/tmp/confusion_rf")


print("\n")
print("=" * 90)
print("COMPARACION FINAL DE MODELOS")
print("=" * 90)

print(
    f"{'Modelo':25}"
    f"{'Accuracy':12}"
    f"{'Precision':12}"
    f"{'Recall':12}"
    f"{'F1':12}"
)

for r in [resultado_lr, resultado_dt, resultado_rf]:

    print(
        f"{r['modelo']:25}"
        f"{r['accuracy']:.4f}      "
        f"{r['precision']:.4f}      "
        f"{r['recall']:.4f}      "
        f"{r['f1']:.4f}"
    )

import os

output_file = "/tmp/resultados_modelos.txt"

with open(output_file, "w") as f:

    f.write("COMPARACION FINAL\n")

    for r in [resultado_lr, resultado_dt, resultado_rf]:

        f.write(
            f"{r['modelo']} | "
            f"Accuracy={r['accuracy']:.4f} | "
            f"Precision={r['precision']:.4f} | "
            f"Recall={r['recall']:.4f} | "
            f"F1={r['f1']:.4f}\n"
        )

print(f"\nResultados guardados en: {output_file}")

spark.stop()