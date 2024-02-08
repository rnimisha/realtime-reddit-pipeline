from pyspark.sql import DataFrame
from pyspark.sql.functions import col, concat, from_unixtime, udf
from pyspark.sql.types import StringType

from src.consumer.preprocessing.clean_text import CleanText


class Preprocessor:
    def __init__(self, clean_text: CleanText) -> None:
        self.clean_text = clean_text

    def _convert_date_format(self, df: DataFrame) -> DataFrame:
        return df.withColumn("created_at", from_unixtime(df["created_at"]))

    def _create_content(self, df: DataFrame) -> DataFrame:
        return df.withColumn("content", concat(col("title"), col("body")))

    def _clean_text(self, df: DataFrame) -> DataFrame:
        clean_text_udf = udf(self.clean_text.clean_text, StringType())
        cleaned_df = df.withColumn("cleaned_content", clean_text_udf(col("content")))
        return cleaned_df

    def preprocess(self, df: DataFrame) -> DataFrame:
        df = self._convert_date_format(df)
        df = self._create_content(df)
        df = self._clean_text(df)
        return df
