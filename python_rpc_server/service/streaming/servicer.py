from protoc.streaming_pb2_grpc import StreamingServicer, add_StreamingServicer_to_server
from protoc.streaming_pb2 import StreamingResponse

class StreamingServicer(StreamingServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def call(self, request, context):
        code = request.code
        exec(code)

        yield StreamingResponse(response='1')
        yield StreamingResponse(response='2')
        yield StreamingResponse(response='3')


def add_servicer_to_server(server):
    add_StreamingServicer_to_server(StreamingServicer(), server)