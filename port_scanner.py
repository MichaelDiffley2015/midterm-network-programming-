import socket
import time

def scan_ports(host, start_port, end_port):
    # Make sure the port numbers are valid
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: Enter a valid port range between 1 and 65535.")
        return

    try:
        # Resolve the host before scanning
        target_ip = socket.gethostbyname(host)
        print(f"\nScanning {host} ({target_ip})")
        print(f"Ports {start_port} through {end_port}\n")

        for port in range(start_port, end_port + 1):
            # Create a new TCP socket for each port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
                scanner.settimeout(0.5)

                result = scanner.connect_ex((target_ip, port))

                if result == 0:
                    print(f"Port {port}: OPEN")
                else:
                    print(f"Port {port}: CLOSED")

            # Small delay to avoid aggressive scanning
            time.sleep(0.05)

    except socket.gaierror:
        print("Error: Host could not be resolved.")

    except OSError as error:
        print(f"Network error: {error}")


def main():
    try:
        host = input("Enter target host: ")
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        scan_ports(host, start_port, end_port)

    except ValueError:
        print("Error: Port numbers must be integers.")


if __name__ == "__main__":
    main()