import requests
from utils import log_event, check_and_create_directory, save_json_file, load_encryption_key, encrypt_data
from config import ICLOUD_USERNAME, ICLOUD_PASSWORD, ICLOUD_API_URL, STORAGE_PATH, ENCRYPTION_KEY

def authenticate_icloud(username, password):
    """
    Authenticate with iCloud and return a session token.
    This is a simplified example and might not reflect the actual iCloud API.
    """
    auth_url = f"{ICLOUD_API_URL}auth"
    response = requests.post(auth_url, json={"username": username, "password": password})
    if response.status_code == 200:
        return response.json().get("token")
    else:
        log_event(f"Failed to authenticate with iCloud. Status Code: {response.status_code}")
        return None

def fetch_voice_memos(session_token):
    """
    Fetch the list of voice memos from iCloud.
    This is a simplified example and might not reflect the actual iCloud API.
    """
    voice_memos_url = f"{ICLOUD_API_URL}voice_memos"
    headers = {"Authorization": f"Bearer {session_token}"}
    response = requests.get(voice_memos_url, headers=headers)
    if response.status_code == 200:
        return response.json().get("voice_memos", [])
    else:
        log_event(f"Failed to fetch voice memos. Status Code: {response.status_code}")
        return []

def save_voice_memos(voice_memos):
    """
    Save the fetched voice memos to a local storage, encrypting the content.
    """
    check_and_create_directory(STORAGE_PATH)
    encrypted_voice_memos = encrypt_data(str(voice_memos), load_encryption_key())
    save_json_file(encrypted_voice_memos, f"{STORAGE_PATH}voice_memos_encrypted.json")
    log_event("Voice memos saved and encrypted successfully.")

def import_voice_memos():
    """
    Main function to handle the import process of voice memos from iCloud.
    """
    try:
        session_token = authenticate_icloud(ICLOUD_USERNAME, ICLOUD_PASSWORD)
        if session_token:
            voice_memos = fetch_voice_memos(session_token)
            if voice_memos:
                save_voice_memos(voice_memos)
                log_event("Voice memos import process completed successfully.")
            else:
                log_event("No voice memos found to import.")
        else:
            log_event("Failed to authenticate with iCloud. Check credentials and try again.")
    except Exception as e:
        log_event(f"An error occurred during the voice memos import process: {str(e)}")

if __name__ == "__main__":
    import_voice_memos()