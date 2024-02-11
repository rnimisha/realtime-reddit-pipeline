import json
import logging

import praw
from confluent_kafka import Producer


class RedditStream:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        user_agent: str,
        subreddit: str,
        kafka_topic: str,
        kafka_producer: Producer,
    ) -> None:
        self.subreddit = subreddit
        self.reddit_instance = self.__initialize_reddit(
            client_id, client_secret, user_agent
        )
        self.kafka_topic = kafka_topic
        self.kafka_producer = kafka_producer

    def __initialize_reddit(
        self, client_id: str, client_secret: str, user_agent: str
    ) -> praw.Reddit:
        logging.info("Creating instance for reddit.")
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )
        logging.info("Reddit instance created successfully.")
        return reddit

    def stream_submission(self):
        subreddit = self.reddit_instance.subreddit(self.subreddit)

        # for submission in subreddit.hot(limit=None):
        for submission in subreddit.stream.submissions():
            print(vars(submission))
            submission_data = {
                "id": submission.id,
                "title": submission.title,
                "body": submission.selftext,
                "upvotes": submission.ups,
                "upvote_ratio": submission.upvote_ratio,
                "created_at": submission.created_utc,
            }
            message = json.dumps(submission_data).encode("utf8")
            print(message)

            try:
                self.kafka_producer.produce(topic=self.kafka_topic, value=message)
                self.kafka_producer.flush()
                logging.info(f"Sent : {submission_data['id']}")
            except Exception as e:
                logging.error(f"Error while sending message {e}")
