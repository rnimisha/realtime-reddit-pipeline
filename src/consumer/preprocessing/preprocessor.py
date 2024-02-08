from pyspark.sql import DataFrame
from pyspark.sql.functions import col, concat, from_unixtime, udf
from pyspark.sql.types import StringType

from src.common.emotion_analysis import EmotionAnalyzer
from src.common.sentiment_analysis import SentimentAnalyzer
from src.consumer.preprocessing.clean_text import CleanText


class Preprocessor:
    def __init__(
        self,
        clean_text: CleanText,
        sentiment_analyzer: SentimentAnalyzer,
        emotion_analyzer: EmotionAnalyzer,
    ) -> None:
        self.clean_text = clean_text
        self.sentiment_analyzer = sentiment_analyzer
        self.emotion_analyzer = emotion_analyzer

    def _convert_date_format(self, df: DataFrame) -> DataFrame:
        return df.withColumn("created_at", from_unixtime(df["created_at"]))

    def _create_content(self, df: DataFrame) -> DataFrame:
        return df.withColumn("content", concat(col("title"), col("body")))

    def _clean_text(self, df: DataFrame) -> DataFrame:
        clean_text_udf = udf(self.clean_text.clean_text, StringType())
        cleaned_df = df.withColumn("cleaned_content", clean_text_udf(col("content")))
        return cleaned_df

    def _generate_sentiment(self, df: DataFrame) -> DataFrame:
        sentiment_analyzer_udf = udf(
            self.sentiment_analyzer.get_sentiment, StringType()
        )
        return df.withColumn(
            "sentiment", sentiment_analyzer_udf(col("cleaned_content"))
        )

    def _generate_emotion(self, df: DataFrame) -> DataFrame:
        emotion_analyzer_udf = udf(self.emotion_analyzer.get_emotion, StringType())
        return df.withColumn("emotion", emotion_analyzer_udf(col("cleaned_content")))

    def preprocess(self, df: DataFrame) -> DataFrame:
        df = self._convert_date_format(df)
        df = self._create_content(df)
        df = self._clean_text(df)
        df = self._generate_sentiment(df)
        df = self._generate_emotion(df)
        df = df.drop("content")
        return df
