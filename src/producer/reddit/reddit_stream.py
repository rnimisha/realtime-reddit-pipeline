import logging

import praw


class RedditStream:
    def __init__(
        self, client_id: str, client_secret: str, user_agent: str, subreddit: str
    ) -> None:
        self.subreddit = subreddit
        self.reddit_instance = self.__initialize_reddit(
            client_id, client_secret, user_agent
        )

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

        for submission in subreddit.stream.submissions():
            submission_data = {
                "id": submission.id,
                "title": submission.title,
                "upvotes": submission.ups,
                "downvotes": submission.downs,
                "created_at": submission.created_utc,
            }
            print(submission_data)
