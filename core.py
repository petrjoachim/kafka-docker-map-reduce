from os import environ
import json

from kafka import KafkaProducer, KafkaConsumer

KAFKA_URL = environ.get("KAFKA_URL")
CONSUMER_TOPIC = environ.get("KAFKA_CONSUME", "none")
PRODUCER_TOPIC = environ.get("KAFKA_PRODUCE", "none")

CONSUMER = KafkaConsumer(
    CONSUMER_TOPIC,
    bootstrap_servers=KAFKA_URL,
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
)

PRODUCER = KafkaProducer(
    bootstrap_servers=KAFKA_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)