import logging

from src.common.create_topic import create_topic
from src.common.get_kafka_conf import create_kafka_producer
from src.config.settings import settings
from src.producer.reddit.reddit_stream import RedditStream

logging.basicConfig(level=logging.INFO)

create_topic(settings.KAFKA_TOPIC, 1, 1)

producer = create_kafka_producer()

reddit = RedditStream(
    settings.CLIENT_ID,
    settings.CLIENT_SECRET,
    settings.USER_AGENT,
    settings.SUBREDDIT,
    settings.KAFKA_TOPIC,
    producer,
)

reddit.stream_submission()
