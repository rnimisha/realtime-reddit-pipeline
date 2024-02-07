from pyspark.sql.functions import from_json, from_unixtime
from pyspark.sql.types import (
    DoubleType,
    FloatType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)

from src.common.spark_session import create_spark_context
from src.config.settings import settings

spark = create_spark_context()

schema = StructType(
    [
        StructField("id", StringType(), True),
        StructField("title", StringType(), True),
        StructField("body", StringType(), True),
        StructField("upvotes", IntegerType(), True),
        StructField("upvote_ratio", FloatType(), True),
        StructField("created_at", DoubleType(), True),
    ]
)

streaming_df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", f"{settings.KAFKA_HOST}:{settings.KAFKA_PORT}")
    .option("subscribe", "redditsubmission")
    .option("startingOffsets", "earliest")
    .load()
)

# binary to string
json_df = streaming_df.selectExpr("cast(value as string) as value")

json_expanded_df = json_df.withColumn(
    "value", from_json(json_df["value"], schema)
).select("value.*")

json_expanded_df = json_expanded_df.withColumn(
    "created_at", from_unixtime(json_expanded_df["created_at"])
)
