import logging
from concurrent import futures

# from app import db
# from app.udaconnect.models import Connection, Location, Person
#from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema
#from geoalchemy2.functions import ST_AsText, ST_Point
#from sqlalchemy.sql import text

import grpc
import person_pb2_grpc
from config import db
from person_pb2 import PersonList, Person
from person_pb2_grpc import PersonServiceServicer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")



class PersonService(PersonServiceServicer):
    # @staticmethod
    # def create(person: Dict) -> Person:
    #     new_person = Person()
    #     new_person.first_name = person["first_name"]
    #     new_person.last_name = person["last_name"]
    #     new_person.company_name = person["company_name"]
    #
    #     db.session.add(new_person)
    #     db.session.commit()
    #
    #     return new_person

    def Create(self, request, context):
        new_person = Person()
        new_person.first_name = request.first_name
        new_person.last_name = request.last_name
        new_person.company_name = request.last_name
        return Person(person=db.session.query(Person).get(request.person_id))

    # @staticmethod
    # def retrieve(person_id: int) -> Person:
    #     person = db.session.query(Person).get(person_id)
    #     return person

    def Retrieve(self, request, context):
        return Person(person=db.session.query(Person).get(request.person_id))

    # @staticmethod
    # def retrieve_all() -> List[Person]:
    #     return db.session.query(Person).all()

    def RetrieveAll(self, request, context):
        return PersonList(persons=db.session.query(Person).all())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_PersonServiceServicer_to_server(
        PersonService(), server
    )
    server.add_insecure_port("[::]:50002")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
