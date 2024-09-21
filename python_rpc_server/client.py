import grpc
from protoc.hello_pb2_grpc import HelloStub
from protoc.hello_pb2 import HelloRequest

if __name__=='__main__':
    channel = grpc.insecure_channel('0.0.0.0:4001')
    stub = HelloStub(channel)

    msg = HelloRequest(name='lishuo zhuang')
    response = stub.hello(msg)
    print(response.greeting)

    msg = HelloRequest(name='fei wu')
    response = stub.hello(msg)
    print(response.greeting)