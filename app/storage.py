import os
import json
from cryptography.fernet import Fernet
from app.config import STORAGE_PATH, ENCRYPTION_KEY
from app.utils import check_and_create_directory, log_event

class StorageManager:
    def __init__(self):
        self.storage_path = STORAGE_PATH
        self.encryption_key = ENCRYPTION_KEY
        self.fernet = Fernet(self.encryption_key)

    def save_data(self, data, file_name, data_type):
        """
        Save data (transcription, summary, or metadata) to a file, encrypted if sensitive.

        Parameters:
        - data: The data to be saved.
        - file_name: The name of the file to save the data to.
        - data_type: The type of data being saved ('transcription', 'summary', 'metadata').
        """
        # Ensure the storage directory for the data type exists
        storage_dir = os.path.join(self.storage_path, data_type)
        check_and_create_directory(storage_dir)

        # Define the full path for the file
        file_path = os.path.join(storage_dir, file_name + (".json" if data_type == "metadata" else ".txt"))

        # Convert data to string if it's not already
        if isinstance(data, dict):
            data = json.dumps(data)

        # Encrypt data if it's sensitive
        if data_type in ['transcription', 'metadata']:
            data = self.fernet.encrypt(data.encode()).decode()

        # Save the data
        with open(file_path, 'w') as file:
            file.write(data)

        log_event(f"{data_type.capitalize()} saved to {file_path}")

    def load_data(self, file_name, data_type):
        """
        Load data from a file, decrypting it if it was encrypted.

        Parameters:
        - file_name: The name of the file to load the data from.
        - data_type: The type of data being loaded ('transcription', 'summary', 'metadata').

        Returns:
        - The loaded data.
        """
        # Define the full path for the file
        file_path = os.path.join(self.storage_path, data_type, file_name + (".json" if data_type == "metadata" else ".txt"))

        # Load the data
        with open(file_path, 'r') as file:
            data = file.read()

        # Decrypt data if it was encrypted
        if data_type in ['transcription', 'metadata']:
            data = self.fernet.decrypt(data.encode()).decode()

        # Convert data back from string if necessary
        if data_type == "metadata":
            data = json.loads(data)

        return data

if __name__ == "__main__":
    # Example usage
    storage_manager = StorageManager()
    # Example for saving a transcription
    transcription = "This is an example transcription."
    storage_manager.save_data(transcription, "example_transcription", "transcription")
    # Example for loading a transcription
    loaded_transcription = storage_manager.load_data("example_transcription", "transcription")
    print(loaded_transcription)
