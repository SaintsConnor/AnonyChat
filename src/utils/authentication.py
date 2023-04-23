import uuid
import hashlib
import secrets

from .encryption import hash_password

class User:
    def __init__(self, username, password):
        self.username = username
        self.salt = None
        self.hashed_password = None
        self.generate_hashed_password(password)
        self.servers = []
        self.blocked = []
        self.muted = []
        
    def generate_hashed_password(self, password):
        hashed, salt = hash_password(password)
        self.salt = salt
        self.hashed_password = hashed
        
    def check_password(self, password):
        hashed, salt = hash_password(password, self.salt)
        return hashed == self.hashed_password
        
class Server:
    def __init__(self, name, owner):
        self.id = str(uuid.uuid4())
        self.name = name
        self.owner = owner
        self.invite_code = secrets.token_hex(8)
        self.members = [owner]
        self.channels = []
        
    def add_member(self, user):
        self.members.append(user)
        
    def remove_member(self, user):
        if user in self.members:
            self.members.remove(user)
