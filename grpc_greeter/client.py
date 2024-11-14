import grpc
import os
from grpc_greeter.generated import greeter_pb2, greeter_pb2_grpc

def run():
    # Dynamically resolve the path to server.crt
    project_root = os.path.abspath(os.path.dirname(__file__) + "/..")
    cert_path = os.path.join(project_root, "server.crt")

    # Load SSL/TLS credentials
    with open(cert_path, "rb") as cert_file:
        trusted_certs = cert_file.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)

    # Establish secure gRPC channel
    with grpc.secure_channel('localhost:50051', credentials) as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        request = greeter_pb2.HelloRequest(name="Alice")
        print(f"Sending request: {request.name}")
        response = stub.SayHello(request)
        print(f"Received response: {response.message}")

if __name__ == "__main__":
    run()

