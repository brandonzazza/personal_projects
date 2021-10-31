# GenSci Intelligence Service Messenger
# Author Brandon Zazza

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def key_gen(pass_raw):

    password = pass_raw.encode()  # Convert to type bytes
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) 
    return key

def encrypt(message, password):
    key = key_gen(password)
    code = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(code)
    print(str(encrypted, 'UTF-8'))

def decrypt(encoded_message, password):
    key = key_gen(password)
    encrypted = str.encode(encoded_message)
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    print(str(decrypted, 'UTF-8'))

def Cypher():
    ans = input("Encrypt or Decrypt: ")
    if ans == "Encrypt" or ans == "encrypt":
        message = str(input("Input message: "))
        password = str(input("Input password: "))
        encrypt(message, password)
    elif ans == "Decrypt" or ans == "decrypt":
        message = str(input("Input Encrypted Message: "))
        password = str(input("Input password: "))
        decrypt(message, password)
    elif ans == "quit" or ans == "Quit":
        return
    elif ans == "Help" or ans == "help":
        print("Type 'encrypt' for encrypting a message or'decrypt'for decrypting a message else type 'quit'")
        Cypher()
    else:
        print("Please input Encrypt or Decrypt: ")
        Cypher()

Cypher()

