import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


class CleanText:
    def __init__(self) -> None:
        self.stop_words = set(stopwords.words("english"))
        self.porter_stemmer = PorterStemmer()

    def _convert_to_lower(self, text: str) -> str:
        return text.lower()

    def _remove_unicode(self, text: str) -> str:
        text = re.sub(
            r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text
        )
        return text

    def _remove_stop_words(self, text: str) -> str:

        text = " ".join(word for word in text.split() if word not in self.stop_words)
        return text

    def _stem_words(self, text: str) -> str:
        words = word_tokenize(text)
        stemmed_words = [self.porter_stemmer.stem(word) for word in words]
        return " ".join(stemmed_words)

    def clean_text(self, text: str) -> str:
        text = self._convert_to_lower(text)
        text = self._remove_unicode(text)
        text = self._remove_stop_words(text)
        text = self._stem_words(text)

        return text


if __name__ == "__main__":
    cleantext = CleanText()
    text = "hey amazon - my package never arrived https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first please fix asap! @amazonhelp"
    print(cleantext.clean_text(text))
