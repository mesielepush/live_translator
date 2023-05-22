import os
import requests
from requests import Response
from typing import BinaryIO
import time
from dotenv import load_dotenv
load_dotenv('.env')

def get_voices():
    
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
      "Accept": "application/json",
      "xi-api-key": f'{os.getenv("ELEVENLABS_API_KEY")}'
    }
    response = requests.get(url, headers=headers)
    names = [f'{x["name"]}: {x["voice_id"] }' for x in response.json()['voices']]
    return names


def get_next_file():
    files = os.listdir('transcripts')
    files = [x.replace('.txt','').replace('_','.') for x in files]
    files = [float(x) for x in files]
    return str(min(files)).replace('.','_')


def read_file(file_path):
    with open('transcripts/'+file_path+'.txt') as f:
        lines = f.readlines()
    return lines

def send_voice_request(voice_id, text, stability = 0.5, similarity_boost = 0.5):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": os.getenv("ELEVENLABS_API_KEY")
    }

    data = {
      "text": f'{text}',
      "model_id": "eleven_multilingual_v1",
      "voice_settings": {
        "stability": stability,
        "similarity_boost": similarity_boost
      }
    }
    
    return requests.post(url, json=data, headers=headers)

def record_audio_file(request, title):
    with open(f'translated_voice/{title}.mp3', 'wb') as f:
        for chunk in request.iter_content():
            if chunk:
                f.write(chunk)
                
def get_lines_to_read():
    file_path = get_next_file()
    file = read_file(file_path)
    return file,file_path

def read_transcript(voice_id):
    lines,title = get_lines_to_read()
    request = send_voice_request(voice_id, lines, stability = 0.5, similarity_boost = 0.5)
    record_audio_file(request, title)
    print(f'new_file at: {title}')
    os.remove('transcripts/' + title+'.txt')
    
def record_reading(voice_id = 'VR6AewLTigWG4xSOukaG'):
    
    while True:
        if len(os.listdir('transcripts')) == 0:
            time.sleep(5)
        else:
            read_transcript(voice_id)