import os
import json
import hashlib
from cryptography.fernet import Fernet
import torchaudio

def load_audio_file(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    return waveform, sample_rate

def load_config():
    """
    Load the configuration settings from the config.py file.
    """
    try:
        from app.config import CONFIG
        return CONFIG
    except ImportError as e:
        raise ImportError("Could not import CONFIG from config.py. Please ensure the file exists and is correctly formatted.") from e

def generate_encryption_key():
    """
    Generate a new encryption key for securing sensitive data.
    """
    return Fernet.generate_key()

def save_encryption_key(key, filename="encryption_key.key"):
    """
    Save the encryption key to a file.
    """
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_encryption_key(filename="encryption_key.key"):
    """
    Load the encryption key from a file.
    """
    try:
        with open(filename, "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Encryption key file {filename} not found.") from e

def encrypt_data(data, key):
    """
    Encrypt data using the provided key.
    """
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """
    Decrypt data using the provided key.
    """
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def anonymize_data(data, salt):
    """
    Anonymize sensitive information in the data using a hash function.
    
    Parameters:
    - data: The data to be anonymized.
    - salt: A salt to ensure the hash is unique.
    
    Returns:
    - The anonymized data.
    """
    anonymized_data = hashlib.sha256((data + salt).encode()).hexdigest()
    return anonymized_data

def log_event(event_message, log_file="event_log.txt"):
    """
    Log an event message to a specified log file.
    """
    with open(log_file, "a") as file:
        file.write(f"{event_message}\n")

def check_and_create_directory(directory_path):
    """
    Check if a directory exists, and if not, create it.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def load_json_file(file_path):
    """
    Load data from a JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"JSON file {file_path} not found.") from e

def save_json_file(data, file_path):
    """
    Save data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
