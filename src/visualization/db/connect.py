from pymongo import MongoClient


def init_connect(
    username: str, password: str, host: str, port: int, db: str
) -> MongoClient:
    client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{db}")
    return client
