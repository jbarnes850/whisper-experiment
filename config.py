import os

# iCloud Access Configuration
ICLOUD_USERNAME = os.getenv('ICLOUD_USERNAME', 'default_username')
ICLOUD_PASSWORD = os.getenv('ICLOUD_PASSWORD', 'default_password')
ICLOUD_API_URL = 'https://api.icloud.com/'

# Whisper Model Configuration
WHISPER_MODEL = 'whisper-large-v3'

# GPT-4 Configuration
GPT_4_API_KEY = os.getenv('GPT_4_API_KEY', 'default_api_key')
GPT_4_MODEL = 'gpt-4'

# Storage Configuration
STORAGE_PATH = './data/'
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', 'default_encryption_key')

# User Interaction Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'default_bot_token')
SMS_API_KEY = os.getenv('SMS_API_KEY', 'default_sms_api_key')

# Privacy Configuration
ANONYMIZATION_SALT = os.getenv('ANONYMIZATION_SALT', 'default_salt')

# Metadata Extraction Configuration
# Using SpeechBrain's pre-trained ECAPA-TDNN model for speaker recognition
SPEAKER_IDENTIFICATION_MODEL = 'speechbrain/spkrec-ecapa-voxceleb'

# Ensure all sensitive information is kept secure and not hardcoded in production environments.
# Consider using environment variables or secure vaults for storing sensitive configuration in a real-world scenario.
