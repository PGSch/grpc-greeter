from grpc_greeter.server import GreeterServicer
from grpc_greeter.generated import greeter_pb2

def test_say_hello():
    servicer = GreeterServicer()
    request = greeter_pb2.HelloRequest(name="TestUser")
    response = servicer.SayHello(request, None)
    assert response.message == "Hello, TestUser!"

