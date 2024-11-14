
# gRPC Greeter

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.12-blue)
![gRPC](https://img.shields.io/badge/gRPC-1.67.1-brightgreen)

## 🚀 Project Overview

**gRPC Greeter** is a Python-based gRPC service that demonstrates the core capabilities of Remote Procedure Calls (RPC) with secure communication. It features:
- A `Greeter` service that responds to client requests with personalized greetings.
- Secure communication using **TLS/SSL**.
- Flexible logging for production-grade operations.

This project is a great starting point for developers looking to explore **gRPC** with Python.

---

## 📂 Directory Structure

```plaintext
grpc-greeter/
├── greeter.proto             # Protobuf definition file
├── grpc_greeter/
│   ├── __init__.py           # Package initialization
│   ├── server.py             # Server implementation
│   ├── client.py             # Client implementation
│   ├── generated/            # Generated Protobuf and gRPC code
│   │   ├── __init__.py
│   │   ├── greeter_pb2.py
│   │   └── greeter_pb2_grpc.py
├── pyproject.toml            # Poetry configuration
├── README.md                 # Project documentation
├── server.key                # Private key for SSL/TLS
├── server.crt                # Certificate for SSL/TLS
└── tests/                    # Unit tests
    └── test_server.py
```

---

## 🛠️ Installation

### Prerequisites

- **Python 3.12+**
- **Poetry** for dependency management:
  ```bash
  pip install poetry
  ```

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/grpc-greeter.git
   cd grpc-greeter
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

---

## 📡 Running the Project

### Start the Server

To start the secure gRPC server:
```bash
poetry run python -m grpc_greeter.server
```

**Expected Output:**
```
2024-11-14 12:00:00 - INFO - Initializing gRPC server...
2024-11-14 12:00:00 - INFO - Secure gRPC server started on port 50051.
```

### Run the Client

To send a request to the server:
```bash
poetry run python -m grpc_greeter.client
```

**Expected Output:**
```
Sending request: Alice
Received response: Hello, Alice!
```

---

## 🔒 Security: TLS/SSL

This project uses **SSL/TLS** to secure client-server communication.

- `server.key`: Private key for the server.
- `server.crt`: Self-signed certificate.

To generate new keys and certificates, use:
```bash
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes   -subj "/C=US/ST=California/L=San Francisco/O=Your Company/OU=Your Unit/CN=localhost"
```

---

## 🧪 Testing

Run unit tests to validate the server:
```bash
poetry run pytest
```

---

## 🛡️ Features

- **gRPC API**:
  - `SayHello`: Responds with a personalized greeting.

- **Production-Ready Enhancements**:
  - Secure communication using **SSL/TLS**.
  - Detailed logging with Python’s `logging` module.
  - Unit tests for reliability.

---

## 🚀 Future Enhancements

- Add support for more advanced gRPC features like **streaming**.
- Deploy the service to cloud platforms like AWS or GCP.
- Create a Dockerized version of the application for portability.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ❤️ Acknowledgments

- **gRPC** for enabling efficient RPC communication.
- **Poetry** for modern dependency management.
- Community contributors for making tools like OpenSSL easily accessible.
