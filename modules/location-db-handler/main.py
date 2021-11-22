import logging
from concurrent import futures
from kafka import KafkaProducer
import grpc
import location_pb2
import location_pb2_grpc

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-location-db-handler")

# Kafka config
TOPIC_NAME = 'location'
KAFKA_SERVER = 'kafka:9092'

class LocationServiceServicer(location_pb2_grpc.LocationServiceServicer):
    def create(self, request, context):
        logger.info(f"Received a message: " + str(request))
        location_message = location_pb2.LocationMessage(person_id=request.person_id, latitude=request.latitude,
                                                 longitude=request.longitude, creation_time=request.creation_time,
                                                 status=request.status)

        # Send location data to the Kafka broker
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        producer.send(TOPIC_NAME, location_message)
        producer.flush()

        location_pb2.LocationMessage.status = location_pb2.LocationMessage.Status.COMPLETED
        return location_pb2.CurrentStatus(location_pb2.LocationMessage.status)

def serve():
    """Initialize gRPC server"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(
        location_pb2_grpc.LocationServiceServicer(), server)

    logger.info(f"gPRC server starting on port 5005...")
    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()