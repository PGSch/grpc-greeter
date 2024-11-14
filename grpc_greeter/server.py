import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import grpc
from concurrent import futures
from grpc_greeter.generated import greeter_pb2, greeter_pb2_grpc

class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Received request from client: {request.name}")  # Debug log
        response = greeter_pb2.HelloReply()
        response.message = f"Hello, {request.name}!"
        print(f"Sending response: {response.message}")  # Debug log
        return response

def serve():
    print("Initializing gRPC server...")  # Debug log
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051.")  # Debug log
    server.start()
    server.wait_for_termination()

# Add this block
if __name__ == "__main__":
    serve()

