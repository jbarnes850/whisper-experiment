import openai
from app.config import GPT_4_API_KEY, GPT_4_MODEL
from app.utils import load_json_file, save_json_file, log_event
from typing import List

def summarize_transcription(transcription: str) -> str:
    """
    Summarize a given transcription using OpenAI's GPT-4 model.

    Parameters:
    - transcription: The transcription text to be summarized.

    Returns:
    - A string containing the summary of the transcription.
    """
    try:
        openai.api_key = GPT_4_API_KEY
        response = openai.Completion.create(
            model=GPT_4_MODEL,
            prompt=f"Summarize the following voice memo:\n{transcription}",
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        log_event(f"Error during summarization: {e}")
        raise RuntimeError(f"Summarization failed. See event log for details.")

def batch_summarize_transcriptions(transcriptions: List[str]) -> List[str]:
    """
    Summarize a batch of transcriptions.

    Parameters:
    - transcriptions: A list of transcription texts to be summarized.

    Returns:
    - A list of strings containing the summaries of the transcriptions.
    """
    summaries = []
    for transcription in transcriptions:
        summary = summarize_transcription(transcription)
        summaries.append(summary)
    return summaries

if __name__ == "__main__":
    # Example usage
    transcription_file_path = "path/to/your/transcription/file.json"
    transcriptions = load_json_file(transcription_file_path)
    
    # Assuming transcriptions is a list of transcription texts
    summaries = batch_summarize_transcriptions(transcriptions)
    
    # Save or process the summaries as needed
    print("Summaries generated:", summaries)