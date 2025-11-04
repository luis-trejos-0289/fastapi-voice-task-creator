from openai import OpenAI

client = OpenAI()

speech_file_path = "audios/text-generated.wav"

text = "I want to learn a new skill weekly."

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="alloy",    
    input=text
) as response:
    response.stream_to_file(speech_file_path)