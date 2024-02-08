import nltk
from nrclex import NRCLex

nltk.download("punkt")


class EmotionAnalyzer:

    def _get_max_emotion(self, emotion_frequencies) -> str:
        return max(emotion_frequencies, key=emotion_frequencies.get)

    def _filter_emotions(self, emotion_frequencies):
        excluded_emotions = ["positive", "negative"]
        filtered_emotions = {
            emotion: freq
            for emotion, freq in emotion_frequencies.items()
            if emotion not in excluded_emotions
        }
        return filtered_emotions

    def get_emotion(self, text: str) -> str:
        emotion_frequencies = NRCLex(text).affect_frequencies
        filtered = self._filter_emotions(emotion_frequencies)
        overall_emotion = self._get_max_emotion(filtered)
        return overall_emotion


if __name__ == "__main__":
    emotion_analyzer = EmotionAnalyzer()
    text = "I love using this product, it's amazing!"
    print(emotion_analyzer.get_emotion(text))
