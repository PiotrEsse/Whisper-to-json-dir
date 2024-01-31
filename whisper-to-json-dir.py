import json
import os
import whisper_timestamped as whisper
#import whisper
from whisper.utils import get_writer

# List of available Whisper models
# models = ["tiny", "base", "small", "medium", "large"]

# Load the model
model = whisper.load_model("tiny")

# Provide full path to your folder with audiofiles
directory = "/home/piotr/Whisper/Audio"


# List of audio extensions in different casings
audio_formats = (".mp4", ".MP4",  
                 ".mp3", ".MP3",
                 ".wav", ".WAV",
                 ".amr", ".AMR",
                 ".aac", ".AAC",
                 ".ogg", ".OGG",
                 ".m4a", ".M4A")

# Iterate over the files in the directory
for filename in os.listdir(directory):
    # Check if the file is an audio file
    if filename.endswith(audio_formats):
        # Load the audio file
        audio = whisper.load_audio(os.path.join(directory, filename))
        # Transcribe the audio file
        result = whisper.transcribe(model, audio, language="pl")
        # Save the result as a json file
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.json'), 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        # Save the result as a txt file
        audio_path = os.path.join(directory, filename)
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.txt'), 'w', encoding='utf-8') as f:
            txt_writer = get_writer("txt", directory)
            txt_writer(result, audio_path)
