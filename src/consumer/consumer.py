from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)

from src.common.spark_session import create_spark_context

spark = create_spark_context()

schema = StructType(
    [
        StructField("id", StringType(), True),
        StructField("title", StringType(), True),
        StructField("upvotes", IntegerType(), True),
        StructField("downvotes", IntegerType(), True),
        StructField("created_at", DoubleType(), True),
    ]
)
