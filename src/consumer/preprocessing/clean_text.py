import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
porter_stemmer = PorterStemmer()


def convert_to_lower(text: str) -> str:
    return text.lower()


def remove_unicode(text: str) -> str:
    text = re.sub(
        r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text
    )
    return text


def remove_stop_words(text: str) -> str:

    text = " ".join(word for word in text.split() if word not in stop_words)
    return text


def stem_words(text: str) -> str:
    words = word_tokenize(text)
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)


def clean_text(text: str) -> str:
    text = convert_to_lower(text)
    text = remove_unicode(text)
    text = remove_stop_words(text)
    text = stem_words(text)

    return text


if __name__ == "__main__":
    print(
        clean_text(
            "hey amazon - my package never arrived https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first please fix asap! @amazonhelp"
        )
    )
