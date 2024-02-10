import logging

from pyspark.sql import SparkSession


def create_spark_context(
    MONGO_USER: str,
    MONGO_PASSWORD: str,
    MONGO_HOST: str,
    MONGO_PORT: str,
    MONGO_DB: str,
):
    spark = None

    try:
        spark = (
            SparkSession.builder.appName("PysparkKafka")
            .config(
                "spark.mongodb.input.uri",
                f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}",
            )
            .config(
                "spark.mongodb.output.uri",
                f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}",
            )
            .config(
                "spark.jars.packages",
                "org.mongodb.spark:mongo-spark-connector_2.12:3.0.2,"
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0",
            )
            .getOrCreate()
        )
        logging.info("Spark context created successfully")

    except Exception as e:
        logging.error(f"Error creating spark context: {e}")

    return spark
