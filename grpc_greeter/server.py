import os
import grpc
import logging
from concurrent import futures
from grpc_greeter.generated import greeter_pb2, greeter_pb2_grpc

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logging.info(f"Received request from client: {request.name}")
        response = greeter_pb2.HelloReply()
        response.message = f"Hello, {request.name}!"
        logging.info(f"Sending response: {response.message}")
        return response

def serve():
    logging.info("Initializing gRPC server...")

    # Dynamically resolve the paths to server.key and server.crt
    project_root = os.path.abspath(os.path.dirname(__file__) + "/..")
    key_path = os.path.join(project_root, "server.key")
    cert_path = os.path.join(project_root, "server.crt")

    # Load SSL/TLS credentials
    private_key = open(key_path, "rb").read()
    certificate = open(cert_path, "rb").read()
    credentials = grpc.ssl_server_credentials([(private_key, certificate)])

    # Initialize gRPC server with SSL
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # Add secure port
    server.add_secure_port('[::]:50051', credentials)
    logging.info("Secure gRPC server started on port 50051.")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

