openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes \
  -subj "/C=US/ST=California/L=San Francisco/O=Your Company/OU=Your Unit/CN=localhost"

