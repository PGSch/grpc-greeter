import grpc
from grpc_greeter.generated import greeter_pb2, greeter_pb2_grpc

def run():
    print("Initializing gRPC client...")  # Debug log
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        request = greeter_pb2.HelloRequest(name="Alice")
        print(f"Sending request: {request.name}")  # Debug log
        response = stub.SayHello(request)
        print(f"Received response from server: {response.message}")  # Debug log

if __name__ == "__main__":
    run()

