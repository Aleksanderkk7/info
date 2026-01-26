import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost on port 8080
server_socket.bind(('localhost', 8080))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on http://localhost:8080")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    
    # Receive the HTTP request
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Request:\n{request}")
    
    # Parse the request line
    request_line = request.split('\n')[0]
    
    # Build HTTP response
    response_body = "hello world"
    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
    
    # Send the response
    client_socket.sendall(response.encode('utf-8'))
    
    # Close the connection
    client_socket.close()
