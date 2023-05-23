from dotenv import load_dotenv
import os
import openai
load_dotenv('.env')
import time
from datetime import datetime
openai.api_key = os.getenv("OPENAI_API_KEY")

base_languague = 'spanish'
promt = "I'ts a lecture about Don Quixote, is in spanish"
response_format = 'text'

def get_next_file():
    files = os.listdir('records')
    files = [x.replace('.mp3','').replace('_','.') for x in files]
    files = [float(x) for x in files]
    return str(min(files)).replace('.','_') + '.mp3'
def make_transcript(file):
    audio_file= open(f"records/{file}", "rb")
    return openai.Audio.translate("whisper-1",
                                  audio_file,
                                  promt = promt,
                                  response_format = 'text')

def transcribe():
    print('Transcribe started')
    while True:
        if len(os.listdir('records')) == 0:
            time.sleep(1)
            continue
        else:
            current_file = get_next_file()
            transcript = make_transcript(current_file)
            name_file = current_file.split('.mp3')[0]
            with open(f'transcripts/{name_file}.txt', 'w') as f:
                f.write(transcript)
            print('one more transcribe')
            os.remove('records/' + current_file)

if __name__ == "__main__":
    transcribe()