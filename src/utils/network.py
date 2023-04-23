import socket

class Network:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.server_address, self.server_port))

    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def receive_message(self):
        data = self.client_socket.recv(1024)
        return data.decode()

    def disconnect(self):
        self.client_socket.close()
