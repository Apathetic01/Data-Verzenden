import socket
import time

def send_files(file_paths, target_ip, target_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target_ip, target_port))

        for file_path in file_paths:
            with open(file_path, 'rb') as file:
                file_data = file.read()

                # Send file size first
                s.sendall(len(file_data).to_bytes(8, byteorder='big'))
                time.sleep(1)  # Add a delay to ensure the receiver has enough time to process

                # Send file data with a larger buffer size
                buffer_size = 4096
                for i in range(0, len(file_data), buffer_size):
                    s.sendall(file_data[i:i + buffer_size])
                    time.sleep(0.1)  # Add a small delay

                time.sleep(1)  # Add an additional delay

    print("Files sent successfully.")

if __name__ == "__main__":
    files_to_send = ["tekst1.txt", "tekst2.txt", "tekst3.txt", "tekst4.txt","tekst5.txt","tekst6.txt"]  # Replace with your actual file paths
    target_ip = "10.0.1.85"
    target_port = 65000

    send_files(files_to_send, target_ip, target_port)
