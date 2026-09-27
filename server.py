import socket

HOST = "127.0.0.1"
PORT = 65432

def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the local host and port
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server is listening on {HOST}:{PORT}")

        # Wait for a client to connect
        connection, address = server_socket.accept()
        print(f"Connected by {address}")

        with connection:
            # Receive a message from the client
            data = connection.recv(1024)

            if data:
                message = data.decode()
                print(f"Client says: {message}")

                # Send a response back to the client
                response = "Hello from the server!"
                connection.sendall(response.encode())

    except OSError as error:
        print(f"Server error: {error}")

    finally:
        server_socket.close()
        print("Server shut down.")

if __name__ == "__main__":
    start_server()