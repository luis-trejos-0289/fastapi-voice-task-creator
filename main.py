import os
import tempfile
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/index")
async def read_index():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):

    contents = await file.read()

    # # Create transcript
    # Unsupported file issue by sending the multipart file directly
    # transcript = client.audio.transcriptions.create(
    #     model="gpt-4o-mini-transcribe",
    #     file=file.file
    # )

    # print("Transcript:", transcript.text)

    suffix = os.path.splitext(file.filename)[1] or ".mp3"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    # Reopen the file as a standard binary file for the OpenAI client
    with open(tmp_path, "rb") as audio_file:
        # Transcribe audio file
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

        os.remove(tmp_path)

        # Summarize transcript
        summary = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract actionable insights and to-do items from this transcript."},
            {"role": "user", "content": transcript.text}
        ]
    )

    return {
        "transcript": transcript.text,
        "insights": summary.choices[0].message.content
    }