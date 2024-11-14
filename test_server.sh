# brew install grpcurl
grpcurl -plaintext localhost:50051 list
grpcurl -plaintext localhost:50051 describe greeter.Greeter
grpcurl -plaintext -d '{"name": "TestUser"}' localhost:50051 greeter.Greeter/SayHello

