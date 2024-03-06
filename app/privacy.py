import hashlib
from cryptography.fernet import Fernet
from config import ANONYMIZATION_SALT, ENCRYPTION_KEY

def anonymize_data(data):
    """
    Anonymize sensitive data using a hash function with a salt.
    
    Parameters:
    - data: The data to be anonymized (e.g., a string containing personally identifiable information).
    
    Returns:
    - An anonymized string.
    """
    salted_data = f"{data}{ANONYMIZATION_SALT}".encode()
    return hashlib.sha256(salted_data).hexdigest()

def encrypt_data(data):
    """
    Encrypt data using Fernet symmetric encryption.
    
    Parameters:
    - data: The data to be encrypted (e.g., a string or bytes).
    
    Returns:
    - Encrypted data as bytes.
    """
    fernet = Fernet(ENCRYPTION_KEY)
    if isinstance(data, str):
        data = data.encode()  # Ensure data is in bytes
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Decrypt data that was encrypted with Fernet symmetric encryption.
    
    Parameters:
    - encrypted_data: The encrypted data as bytes.
    
    Returns:
    - Decrypted data as bytes.
    """
    fernet = Fernet(ENCRYPTION_KEY)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

def remove_sensitive_metadata(metadata):
    """
    Remove or anonymize sensitive information from metadata.
    
    Parameters:
    - metadata: A dictionary containing metadata.
    
    Returns:
    - A dictionary with sensitive information removed or anonymized.
    """
    if 'location' in metadata:
        metadata['location'] = anonymize_data(metadata['location'])
    if 'speaker' in metadata:
        metadata['speaker'] = anonymize_data(metadata['speaker'])
    # Add more fields as necessary based on what is considered sensitive
    return metadata
