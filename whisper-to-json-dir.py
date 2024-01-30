import json
import os
import whisper_timestamped as whisper

# List of available Whisper models
# models = ["tiny", "base", "small", "medium", "large"] 

model = whisper.load_model("tiny")

# provide full path to your folder with audiofiles
directory = "/home/piotr/Whisper/Audio"
audio_formats = (".mp4",".mp3", ".wav", ".amr", ".aac", ".ogg", ".m4a")

for filename in os.listdir(directory):
    if filename.endswith(audio_formats):
        audio = whisper.load_audio(os.path.join(directory, filename))
        result = whisper.transcribe(model, audio, language="pl")
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.json'), 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
