import logging

from pyspark.sql import SparkSession


def create_spark_context():
    spark = None

    try:
        spark = (
            SparkSession.builder.appName("PysparkKafka")
            .config(
                "spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0",
            )
            .getOrCreate()
        )
        logging.info("Spark context created successfully")

    except Exception as e:
        logging.error(f"Error creating spark context: {e}")

    return spark


if __name__ == "__main__":
    spark = create_spark_context()
