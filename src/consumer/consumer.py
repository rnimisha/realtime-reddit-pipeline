from pyspark.sql.functions import col, concat, from_json, from_unixtime, udf
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
from src.consumer.preprocessing.clean_text import CleanText

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

agg_df = json_expanded_df.withColumn(
    "created_at", from_unixtime(json_expanded_df["created_at"])
).withColumn("content", concat(col("title"), col("body")))

clean_text = CleanText()
clean_text_udf = udf(clean_text.clean_text, StringType())

cleaned_df = agg_df.withColumn("cleaned_content", clean_text_udf(col("content")))
