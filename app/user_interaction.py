import telebot
from app.config import TELEGRAM_BOT_TOKEN, SMS_API_KEY
from app.storage import StorageManager
from app.utils import decrypt_data, load_encryption_key
from app.summarization import summarize_text
from app.transcription import transcribe_audio

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Initialize the Storage Manager
storage_manager = StorageManager()

# Load the encryption key for decrypting data
encryption_key = load_encryption_key()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to your Voice Memo AI Assistant. You can ask me about your voice memos or request summaries of them.")

@bot.message_handler(func=lambda message: True)
def handle_query(message):
    """
    Handle user queries, searching through transcriptions and summaries for relevant information.
    """
    query = message.text
    # For simplicity, this example assumes the user is asking for a summary of their latest memo.
    # In a real application, you would implement more sophisticated query handling.
    try:
        # Load the latest transcription (assuming a naming convention or retrieving the latest file)
        transcription = storage_manager.load_data("latest_transcription", "transcription")
        transcription = decrypt_data(transcription, encryption_key)
        
        # Summarize the transcription
        summary = summarize_text(transcription)
        
        # Send the summary back to the user
        bot.reply_to(message, f"Summary of your latest voice memo: {summary}")
    except Exception as e:
        bot.reply_to(message, "Sorry, I couldn't process your request. Please try again later.")

if __name__ == "__main__":
    bot.polling()
