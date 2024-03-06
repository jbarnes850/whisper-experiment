# Voice Memo AI Assistant

## Project Description

The Voice Memo AI Assistant transforms your voice recordings into actionable insights. Whether you're using an iPhone or Apple Watch, your voice memos are securely processed from iCloud storage. Imagine having your own personal scribe that not only transcribes your words but also distills them into concise summaries. Beyond transcription, this app allows you to interact with your data through SMS or Telegram, asking questions and receiving context-specific responses. With a commitment to privacy and security, the Voice Memo AI Assistant evolves with you, continually enhancing its understanding of your needs and preferences.

## Data Pipeline Overview

### Import

- **Source**: Voice memos from iPhone/Apple Watch stored in iCloud.
- **Mechanism**: Secure access to iCloud using API interactions.
- **Trigger**: Automatic detection of new or updated recordings.

### Transcription

- **Model**: OpenAI Whisper Large V3.
- **Task**: Convert audio files into text transcripts.
- **Privacy**: Transcriptions are performed locally or in a secure environment to ensure privacy.

### Metadata Extraction

- **Features**: Extraction of timestamps, speaker identification (with privacy considerations), and location (if available).
- **Anonymization**: Personally identifiable information is removed or transformed to protect privacy.

### Summarization

- **Model**: GPT-4.
- **Task**: Generate concise summaries of voice memo transcripts.

### Storage

- **Data**: Transcripts and summaries are stored in a file system or a lightweight database.
- **Privacy**: Sensitive data is encrypted at rest to prioritize user privacy.

### User Interaction

- **Interface**: Users can interact with the assistant via SMS or Telegram.
- **Query Handling**: The assistant can understand queries about past voice memos and provide contextually relevant answers using stored transcripts, summaries, and metadata.

## AI Models Needed

- **Transcription**: OpenAI Whisper.
- **Summarization and Query Answering**: GPT-4.
- **Speaker Identification**: Basic ML models with anonymization.

## Privacy Emphasis

- A privacy-first mentality guides all design decisions.
- Collection of personally identifiable information is minimized.
- Sensitive data is securely stored.

## Requirements

- Python 3.8 or higher
- Compatible with macOS and Linux (Windows support coming soon)
- Internet connection for API interactions

## Getting Started

To set up the Voice Memo AI Assistant, follow these steps:

1. **Install Dependencies**: Ensure all required libraries are installed by running `pip install -r requirements.txt`.

2. ## Configuration

Before running the Voice Memo AI Assistant, you need to configure your environment variables to ensure the application can access necessary services like iCloud, OpenAI, and Telegram. This is crucial for the functionality of importing voice memos, transcribing audio, summarizing content, and interacting with users.

1. **Environment Variables**: Copy the `example.env.local` file to a new file named `.env.local` in the root directory of the project.

2. **Edit `.env.local`**: Fill in your specific details for the following keys:

    - `ICLOUD_USERNAME`: Your iCloud username.
    - `ICLOUD_PASSWORD`: Your iCloud password.
    - `GPT_4_API_KEY`: Your OpenAI API key for GPT-4.
    - `ENCRYPTION_KEY`: A generated encryption key for securing stored data.
    - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
    - `SMS_API_KEY`: Your SMS service API key.
    - `ANONYMIZATION_SALT`: A salt string for data anonymization processes.


3. **Load Environment Variables**: Ensure your application loads these environment variables at startup. This might involve adding code to your main script to read from `.env.local`.

By setting up these environment variables, you provide the necessary credentials and keys for the application to interact with external services securely and maintain user privacy.

4. **Running the Assistant**: Navigate to the project's root directory and start the assistant by running the main script:

```bash
python app/main.py
```

This script initializes the data pipeline, including importing voice memos, transcription, metadata extraction, summarization, and user interaction setup.

5. **Interacting with the Assistant**: Once the assistant is running, users can interact with it through Telegram using predefined commands or queries about their voice memos. The assistant can understand queries about past voice memos and provide contextually relevant answers using stored transcripts, summaries, and metadata.

## Contributing

Contributions to improve the Voice Memo AI Assistant are welcome. If you have suggestions for new features, bug reports, or contributions, please submit them as issues or pull requests on GitHub.

## License

This project is released under the MIT License.
