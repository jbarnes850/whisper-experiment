import subprocess
import os
from app.utils import check_and_create_directory, load_json_file, save_json_file, log_event
from app.config import WHISPER_MODEL, STORAGE_PATH

def transcribe_audio(audio_file_path):
    """
    Transcribe an audio file using the OpenAI Whisper model.
    
    Parameters:
    - audio_file_path: Path to the audio file to be transcribed.
    
    Returns:
    - A string containing the transcription of the audio file.
    """
    try:
        # Ensure the Whisper model is available and installed
        check_whisper_installation()
        
        # Define the output path for the transcription
        transcript_file_path = os.path.splitext(audio_file_path)[0] + ".txt"
        
        # Execute the Whisper model to transcribe the audio
        command = f"whisper {audio_file_path} --model {WHISPER_MODEL} --output {transcript_file_path}"
        process = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        
        # Read and return the transcription
        with open(transcript_file_path, 'r') as file:
            transcription = file.read()
        
        log_event(f"Transcription completed for {audio_file_path}")
        return transcription
    except subprocess.CalledProcessError as e:
        log_event(f"Error during transcription: {e}")
        raise RuntimeError(f"Transcription failed for {audio_file_path}. See event log for details.")

def check_whisper_installation():
    """
    Check if the Whisper model is installed. If not, attempt to install it.
    """
    try:
        subprocess.run(["whisper", "--help"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        log_event("Whisper model not found. Attempting to install.")
        subprocess.run(["pip", "install", "whisper"], check=True)
        log_event("Whisper model installed successfully.")

def save_transcription(transcription, file_name):
    """
    Save the transcription to a file.
    
    Parameters:
    - transcription: The transcription text to be saved.
    - file_name: The name of the file to save the transcription to.
    """
    # Ensure the storage directory exists
    storage_dir = os.path.join(STORAGE_PATH, "transcriptions")
    check_and_create_directory(storage_dir)
    
    # Define the full path for the transcription file
    file_path = os.path.join(storage_dir, file_name + ".txt")
    
    # Save the transcription
    with open(file_path, 'w') as file:
        file.write(transcription)
    
    log_event(f"Transcription saved to {file_path}")
    return file_path  # Return the path where the transcription is saved

if __name__ == "__main__":
    # Example usage
    audio_file_path = "path/to/your/audio/file.mp3"
    transcription = transcribe_audio(audio_file_path)
    file_name = os.path.basename(audio_file_path).split('.')[0]
    save_transcription(transcription, file_name)