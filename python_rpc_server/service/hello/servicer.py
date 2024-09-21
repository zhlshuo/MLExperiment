from protoc.hello_pb2_grpc import HelloServicer, add_HelloServicer_to_server
from protoc.hello_pb2 import HelloResponse
from common.mysql import testSession
from models.hello import Hello

class HelloServicer(HelloServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def hello(self, request, context):
        hello = testSession.query(Hello).filter(Hello.name==request.name).first()
        return HelloResponse(greeting=str(hello))


def add_servicer_to_server(server):
    add_HelloServicer_to_server(HelloServicer(), server)
