import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()


class SentimentAnalyzer:
    def __init__(self) -> None:
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment_score(self, text: str) -> float:
        sentiment_score = self.analyzer.polarity_scores(text)
        return sentiment_score["compound"]

    def get_sentiment_label(self, score: float) -> str:
        if score > 0.05:
            return "positive"
        elif score < -0.05:
            return "negative"
        else:
            return "neutral"


if __name__ == "__main__":
    sentiment_analyzer = SentimentAnalyzer()
    text = "I love using this product, it's amazing!"
    print(sentiment_analyzer.get_sentiment(text))
