import os
import requests
from requests import Response
from typing import BinaryIO
import time
from dotenv import load_dotenv
load_dotenv('.env')

def create_new_voice(files_path,
                     output_path,
                     name,
                     accent,
                     gender,
                     promt):
    
    files = os.listdir(files_path)
    files = [files_path + x for x in files if x.endswith('.mp3') ]
    OUTPUT_PATH = output_path
    add_voice_url = "https://api.elevenlabs.io/v1/voices/add"
    
    
    headers = {
      "Accept": "application/json",
      "xi-api-key": os.getenv("ELEVENLABS_API_KEY")
    }
    
    labels = '{"accent": ' + f' "{accent}" ' + ', "gender": ' + f' "{gender}"' +'} '
    
    data = {
    'name': f'{name}',
    'labels': f'{labels}',
    'description': f'{promt}'}
    
    files = [
        ('files', ('sample1.mp3', open(x, 'rb'), 'audio/mpeg')) for x in files
    ]
    response = requests.post(add_voice_url, headers=headers, data=data, files=files)
    voice_id = response.json()["voice_id"]
    print(f'voice_id {voice_id} \n {name}')
    with open(f'voices/{name}.txt', 'w') as f:
            f.write(voice_id)
            
if __name__ =='__main__':
    create_new_voice(files_path = 'records/',
                     output_path = 'voices/',
                     name = 'borges',
                    accent = 'argentinian',
                    gender = 'male',
                    promt = 'Lecturer, famous writer, academic')