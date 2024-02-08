import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()


class SentimentAnalyzer:
    def __init__(self) -> None:
        self.analyzer = SentimentIntensityAnalyzer()

    def _get_sentiment_score(self, text: str) -> float:
        sentiment_score = self.analyzer.polarity_scores(text)
        return sentiment_score["compound"]

    def _get_sentiment_label(self, score: float) -> str:
        if score > 0.05:
            return "positive"
        elif score < -0.05:
            return "negative"
        else:
            return "neutral"

    def get_sentiment(self, text: str) -> str:
        score = self._get_sentiment_score(text)
        sentiment = self._get_sentiment_label(score)
        return sentiment


if __name__ == "__main__":
    sentiment_analyzer = SentimentAnalyzer()
    text = "I love using this product, it's amazing!"
    print(sentiment_analyzer.get_sentiment(text))
