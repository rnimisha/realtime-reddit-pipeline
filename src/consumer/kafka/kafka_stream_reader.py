from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType


class KakfaStreamReader:
    def __init__(self, spark: SparkSession, kafka_host: str, kafka_port: int) -> None:
        self.spark = spark
        self.kafka_host = kafka_host
        self.kafka_port = kafka_port

    def _read_streaming_message(self) -> DataFrame:
        streaming_df = (
            self.spark.readStream.format("kafka")
            .option(
                "kafka.bootstrap.servers",
                f"{self.kafka_host}:{self.kafka_port}",
            )
            .option("subscribe", "redditsubmission")
            .option("startingOffsets", "earliest")
            .load()
        )
        return streaming_df

    def _convert_binary_to_string(self, df: DataFrame) -> DataFrame:
        return df.selectExpr("cast(value as string) as value")

    def get_kafka_data(self, schema: StructType) -> DataFrame:
        streaming_df = self._read_streaming_message()
        json_df = self._convert_binary_to_string(streaming_df)
        expanded_df = json_df.withColumn(
            "value", from_json(json_df["value"], schema)
        ).select("value.*")

        return expanded_df
