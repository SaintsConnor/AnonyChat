import socket
import threading
import json

from utils import encryption, validation

class Client:
    def __init__(self, username, server_address):
        self.username = username
        self.server_address = server_address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        self.socket.connect(self.server_address)
        self.connected = True
        print(f"Connected to server at {self.server_address}")

    def disconnect(self):
        self.socket.close()
        self.connected = False
        print("Disconnected from server")

    def send_message(self, message, recipient=None):
        encrypted_message = encryption.encrypt_message(
            message, recipient.public_key if recipient else None)
        validated_message = validation.validate_message(encrypted_message)
        message_data = {
            "sender": self.username,
            "recipient": recipient.username if recipient else "server",
            "message": validated_message
        }
        self.socket.sendall(json.dumps(message_data).encode())

    def receive_messages(self):
        while self.connected:
            message_data = self.socket.recv(4096)
            if not message_data:
                break
            message_data = json.loads(message_data.decode())
            sender = message_data["sender"]
            recipient = message_data["recipient"]
            message = message_data["message"]
            decrypted_message = encryption.decrypt_message(
                message, recipient=self.username)
            if not decrypted_message:
                print(f"Invalid message received from {sender}")
                continue
            print(f"{sender} -> {recipient if recipient != 'server' else 'SERVER'}: {decrypted_message}")

