import logging

from app import db
from app.udaconnect.models import Location
from app.udaconnect.schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-db-handler")
from kafka import KafkaConsumer

TOPIC_NAME = 'location'
consumer = KafkaConsumer(TOPIC_NAME)

for message in consumer:
    logger.info(f"Received message from Kafka producer: " + str(message))
    new_location = Location()
    new_location.person_id = message.person_id
    new_location.creation_time = message.creation_time
    new_location.coordinate = ST_Point(message.latitude, message.longitude)

    db.session.add(new_location)
    db.session.commit()