import os
import base64
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

KEY_SIZE = 256
BLOCK_SIZE = 16

def generate_aes_key():
    return os.urandom(KEY_SIZE//8)

def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def aes_encrypt(plaintext, key):
    iv = os.urandom(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))
    return iv + ciphertext

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_CBC,
