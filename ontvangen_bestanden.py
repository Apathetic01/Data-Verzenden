import socket

def receive_files(save_paths, listen_ip, listen_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((listen_ip, listen_port))
        s.listen()

        print("Waiting for connection...")
        conn, _ = s.accept()

        for save_path in save_paths:
            # Receive file size first
            file_size_bytes = conn.recv(8)
            file_size = int.from_bytes(file_size_bytes, byteorder='big')

            # Receive file data with a larger buffer size
            buffer_size = 4096
            with open(save_path, 'wb') as file:
                received_data = b''
                while len(received_data) < file_size:
                    data = conn.recv(buffer_size)
                    received_data += data

                file.write(received_data)

        print("Files received successfully.")

if __name__ == "__main__":
    files_to_save = ["received_verzenden_bestanden.txt", "received_ontvangen_bestanden.txt"]  # Replace with your desired save paths
    listening_ip = "10.0.1.207"  # Your computer's IP
    listening_port = 65000

    receive_files(files_to_save, listening_ip, listening_port)
