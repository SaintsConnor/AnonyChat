import hashlib

def validate_message(message):
    """
    Validates a message by checking its hash against the expected hash.
    Returns True if the message is valid, False otherwise.
    """
    message_data, message_hash = message[:-64], message[-64:]
    expected_hash = hashlib.sha256(message_data.encode()).hexdigest()
    return message_hash == expected_hash

def hash_message(message):
    """
    Hashes a message using SHA-256 and returns the hash.
    """
    return hashlib.sha256(message.encode()).hexdigest()
