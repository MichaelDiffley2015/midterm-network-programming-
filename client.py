import socket

HOST = "127.0.0.1"
PORT = 65432

def start_client():
    # Create a TCP socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

            # Connect to the server
            client_socket.connect((HOST, PORT))
            print(f"Connected to server at {HOST}:{PORT}")

            # Send a message to the server
            message = "Hello from the client!"
            client_socket.sendall(message.encode())
            print(f"Message sent: {message}")

            # Receive a response from the server
            response = client_socket.recv(1024)
            print(f"Server response: {response.decode()}")

        print("Client disconnected successfully.")

    except ConnectionRefusedError:
        print("Error: Server is not running or connection was refused.")

    except OSError as error:
        print(f"Connection error: {error}")


if __name__ == "__main__":
    start_client()