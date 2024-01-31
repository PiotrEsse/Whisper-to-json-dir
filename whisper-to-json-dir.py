import json
import os
import whisper
from whisper.utils import get_writer
import datetime
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
        
        # Add filename to result - this gives additional context to transcriptions you can use
        result["filename"] = filename
        # Get file creation date
        ctime = os.path.getctime(os.path.join(directory, filename))
        filedate = datetime.datetime.fromtimestamp(ctime)

        # Get file modification date
        mtime = os.path.getmtime(os.path.join(directory, filename))
        moddate = datetime.datetime.fromtimestamp(mtime)

        # Add to result
        result["filedate"] = filedate.strftime("%Y-%m-%d %H:%M:%S")
        result["moddate"] = moddate.strftime("%Y-%m-%d %H:%M:%S")

        ## Save the result as a json file
        #with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.json'), 'w', encoding='utf-8') as f:
        #    json.dump(result, f, ensure_ascii=False, indent=2)
        # Save the result as a txt file
        audio_path = os.path.join(directory, filename)
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.txt'), 'w', encoding='utf-8') as f:
            txt_writer = get_writer("txt", directory)
            txt_writer(result, audio_path)
        # Save the result as a tsv file
        audio_path = os.path.join(directory, filename)
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.tsv'), 'w', encoding='utf-8') as f:
            tsv_writer = get_writer("tsv", directory)
            tsv_writer(result, audio_path)
        # Save the result as a json file
        audio_path = os.path.join(directory, filename)
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.json'), 'w', encoding='utf-8') as f:
            json_writer = get_writer("json", directory)
            json_writer(result, audio_path)

        # Save the result as a SRT file
        audio_path = os.path.join(directory, filename)
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.srt'), 'w', encoding='utf-8') as f:
            srt_writer = get_writer("srt", directory)
            srt_writer(result, audio_path)
            # Save the result as a tsv file
        audio_path = os.path.join(directory, filename)
        with open(os.path.join(directory, filename.rsplit(".", 1)[0] + '.vtt'), 'w', encoding='utf-8') as f:
            vtt_writer = get_writer("vtt", directory)
            vtt_writer(result, audio_path)
        
        print(result["filename"])

