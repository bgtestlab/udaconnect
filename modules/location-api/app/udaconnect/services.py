import logging
from typing import Dict

from app import db
from app.udaconnect.models import Location
from app.udaconnect.schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point

import grpc
import location_pb2
import location_pb2_grpc

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-location-api")

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        """
        Write a message to gRPC server
        """
        logger.info(f"Sending location payload to gRPC server")
        channel = grpc.insecure_channel("localhost:5005")
        stub = location_pb2_grpc.LocationServiceStub(channel)

        # Update this with desired payload
        location = location_pb2.LocationMessage(
            person_id=location["person_id"],
            latitude=location["latitude"],
            longitude=location["longitude"],
            creation_time=location["creation_time"],
            status=location_pb2.LocationMessage.Status.QUEUED,
        )

        response = stub.Create(location)
        logger.info(f"Received location payload from gRPC server: " + str(response))
        new_location = Location()
        new_location.person_id = response.person_id
        new_location.creation_time = response.creation_time
        new_location.coordinate = ST_Point(response.latitude, response.longitude)

        # db.session.add(new_location)
        # db.session.commit()

        return new_location
