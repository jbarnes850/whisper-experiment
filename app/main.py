import sys
from data_import import import_voice_memos
from transcription import transcribe_all_voice_memos
from metadata_extraction import extract_all_metadata
from summarization import summarize_all_transcriptions
from storage import save_all_data
from user_interaction import start_interaction_service
from metadata_extraction import extract_speaker_embeddings
from utils import log_event

def main():
    try:
        log_event("Starting Voice Memo AI Assistant...")

        # Step 1: Import voice memos from iCloud
        log_event("Importing voice memos from iCloud...")
        import_voice_memos()

        # Step 2: Transcribe all imported voice memos
        log_event("Transcribing voice memos...")
        audio_file_paths = transcribe_all_voice_memos()  # Get the paths of all transcribed audio files

        # New Step: Extract Speaker Embeddings
        log_event("Extracting speaker embeddings...")
        for path in audio_file_paths:
            extract_speaker_embeddings(path)

        # Step 3: Extract metadata from all voice memos
        log_event("Extracting metadata from voice memos...")
        extract_all_metadata()

        # Step 4: Summarize all transcriptions
        log_event("Summarizing transcriptions...")
        summarize_all_transcriptions()

        # Step 5: Save all data securely
        log_event("Saving all data securely...")
        save_all_data()

        # Step 6: Start user interaction service (SMS/Telegram)
        log_event("Starting user interaction service...")
        start_interaction_service()

        log_event("Voice Memo AI Assistant is ready for use.")
    except Exception as e:
        log_event(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
