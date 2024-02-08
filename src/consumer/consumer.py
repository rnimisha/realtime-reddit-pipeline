from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import (
    DoubleType,
    FloatType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)

from src.common.sentiment_analysis import SentimentAnalyzer
from src.common.spark_session import create_spark_context
from src.config.settings import settings
from src.consumer.kafka.kafka_stream_reader import KakfaStreamReader
from src.consumer.preprocessing.clean_text import CleanText
from src.consumer.preprocessing.preprocessor import Preprocessor


class RedditConsumer:

    def __init__(
        self,
        spark: SparkSession,
        kafka_stream_reader: KakfaStreamReader,
        preprocessor: Preprocessor,
    ) -> None:
        self.spark = spark
        self.kafka_stream_reader = kafka_stream_reader
        self.preprocessor = preprocessor
        self.schema = self._define_schema()

    def _define_schema(self) -> StructType:
        return StructType(
            [
                StructField("id", StringType(), True),
                StructField("title", StringType(), True),
                StructField("body", StringType(), True),
                StructField("upvotes", IntegerType(), True),
                StructField("upvote_ratio", FloatType(), True),
                StructField("created_at", DoubleType(), True),
            ]
        )

    def process_stream(self):
        df = self.kafka_stream_reader.get_kafka_data(self.schema)
        processed_df = self.preprocessor.preprocess(df)
        return processed_df


if __name__ == "__main__":
    spark = create_spark_context()
    kafka_stream_reader = KakfaStreamReader(
        spark, settings.KAFKA_HOST, settings.KAFKA_PORT
    )
    clean_text = CleanText()
    sentiment_analyzer = SentimentAnalyzer()
    preprocessor = Preprocessor(clean_text, sentiment_analyzer)
    consumer = RedditConsumer(spark, kafka_stream_reader, preprocessor)
    cleaned_df = consumer.process_stream()

    query = cleaned_df.writeStream.outputMode("append").format("console").start()
    query.awaitTermination()
