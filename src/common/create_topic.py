import logging

from confluent_kafka.admin import AdminClient, NewTopic

from src.common.get_kafka_conf import get_kakfa_conf


def create_topic(topic: str, num_partitions: int, replication_factor: int):
    conf = get_kakfa_conf()
    admin_client = AdminClient(conf)

    if not topic_exists(admin_client, topic):
        new_topic = NewTopic(topic, num_partitions, replication_factor)
        admin_client.create_topics([new_topic])
        logging.info(f"Topic '{topic}' created successfully")
    else:
        logging.error(f"Topic '{topic}' already exists")


def topic_exists(admin_client, topic):
    topics = admin_client.list_topics().topics
    return topic in topics
