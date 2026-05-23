# Jarvis – Personal Voice Assistant

A Python-based desktop voice assistant that responds to spoken commands for tasks like web browsing, Wikipedia lookups, time queries, and sending emails.

## Features

- **Wikipedia Search** – Fetches and reads a brief summary aloud
- **Web Navigation** – Opens Google, YouTube, and Stack Overflow
- **App Launch** – Opens VS Code via voice command
- **Email Sending** – Composes and sends Gmail messages by voice

## Requirements

```bash
pip install pyttsx3 SpeechRecognition wikipedia python-dotenv
```

> Also requires **PyAudio** for microphone input. On Windows: `pip install pyaudio`

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/personal-voice-assistant.git
   cd personal-voice-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia python-dotenv
   ```

3. **Configure environment variables**  
   Create a `.env` file in the project root & hide it via gitignore (I have uploaded mine with fake credentials):
   ```
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

4. **Update the VS Code path** *(optional)*  
   Edit `codePath` in the script to match your local VS Code installation path.

5. **Run**
   ```bash
   python personal_voice_assistant.py
   ```
