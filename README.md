# FastAPI Voice Task Creator

## Overview

FastAPI Voice Task Creator is a web application that allows users to upload audio files, transcribe them using OpenAI Whisper, and extract actionable insights and to-do items from the transcript using GPT-4o. The app provides a simple interface for uploading audio and viewing both the transcript and summarized insights.

## Features

- Upload audio files (MP3, WAV, etc.) via a web interface.
- Automatic transcription of audio using OpenAI Whisper.
- Extraction of actionable insights and tasks from the transcript using GPT-4o.
- Simple, modern web UI built with FastAPI, Jinja2, and JavaScript.

## How It Works

1. User uploads an audio file through the web interface.
2. The backend transcribes the audio using OpenAI Whisper.
3. The transcript is summarized to extract key insights and to-do items.
4. Results are displayed on the web page.

## Installation

1. Clone the repository:
   ```zsh
   git clone https://github.com/luis-trejos-0289/fastapi-voice-task-creator.git
   cd fastapi-voice-task-creator
   ```
2. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
4. Run the application:
   ```zsh
   uvicorn main:app --reload
   ```
5. Open your browser and go to `http://localhost:8000/index`.

## File Structure

- `main.py`: FastAPI backend for handling uploads, transcription, and summarization.
- `audio_generator.py`: Example script for generating speech audio from text.
- `templates/index.html`: Web interface for uploading audio.
- `static/index.js`: JavaScript for handling form submission and displaying results.
- `audios/`: Folder for generated audio files.
- `requirements.txt`: Python dependencies.

## License

MIT License
