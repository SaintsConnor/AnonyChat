import datetime

class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
    
    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file_path, "a") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")
