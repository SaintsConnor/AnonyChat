import os
import json

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = {}
        try:
            with open(filepath, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass
    
    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f)
    
    def set_server(self, server_id, server_name):
        self.data.setdefault('servers', {})[server_id] = server_name
        self.save()
    
    def get_server_name(self, server_id):
        return self.data.get('servers', {}).get(server_id)
    
    def set_username(self, username):
        self.data['username'] = username
        self.save()
    
    def get_username(self):
        return self.data.get('username')
    
    def add_blocked_user(self, user_id):
        self.data.setdefault('blocked', []).append(user_id)
        self.save()
    
    def remove_blocked_user(self, user_id):
        if user_id in self.data.get('blocked', []):
            self.data['blocked'].remove(user_id)
            self.save()
    
    def add_muted_user(self, user_id):
        self.data.setdefault('muted', []).append(user_id)
        self.save()
    
    def remove_muted_user(self, user_id):
        if user_id in self.data.get('muted', []):
            self.data['muted'].remove(user_id)
            self.save()
