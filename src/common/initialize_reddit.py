import logging

import praw

from src.config.settings import settings


def initialize_reddit() -> praw.Reddit:
    logging.info("Creating instance for reddit.")
    reddit = praw.Reddit(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        user_agent=settings.USER_AGENT,
    )
    logging.info("Reddit instance created successfully.")
    return reddit
