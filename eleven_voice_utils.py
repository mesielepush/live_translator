import os
import requests
from requests import Response
from typing import BinaryIO
import time
from dotenv import load_dotenv
load_dotenv('.env')
import elevenlabs

elevenlabs.set_api_key(os.getenv("ELEVENLABS_API_KEY")) 

def calculate_mean_price():
    import joblib
    elevenlabs_token = 22/100000
    elevenlabs_usage = joblib.load('usages/elevenlabs.pkl')
    differences = []
    for item in range(len(elevenlabs_usage)):
        if item == max(elevenlabs_usage.keys()):
            break
        differences.append(elevenlabs_usage[item + 1] - elevenlabs_usage[item])
    mean = sum(differences)/len(differences)
    mean_price = mean * elevenlabs_token
    return mean, mean_price

def log_usage():
    from elevenlabs.api import User
    import joblib
    if not os.path.exists('usages/elevenlabs.pkl'):
        elevenlabs_usage = dict()
        elevenlabs_usage[0] = User.from_api().subscription.character_count
        joblib.dump(elevenlabs_usage,'usages/elevenlabs.pkl')
        print('record for elevenlabs usage done at usages/elevenlabs.pkl')
    else:
        elevenlabs_usage = joblib.load('usages/elevenlabs.pkl')
        current_usage = User.from_api().subscription.character_count
        next_name = max(elevenlabs_usage.keys()) + 1
        if current_usage == elevenlabs_usage[next_name-1]:
            print(f'Usage is still: {elevenlabs_usage[next_name-1]}')
            return
        else:
            elevenlabs_usage[next_name] = current_usage
            joblib.dump(elevenlabs_usage,'usages/elevenlabs.pkl')
            print(f'new usage: {current_usage} saved at usages/elevenlabs.pkl')
            
def plot_usage():
    import matplotlib.pyplot as plt
    data = get_usage()
    plt.style.use('dark_background')
    plt.bar(['USED', 'LEFT', 'LIMIT'], data , color = ['r','g','blue'])
    plt.title('Usage ELEVENLABS')
    plt.show()
    
def get_usage():
    
    from elevenlabs.api import User
    user = User.from_api()
    used = user.subscription.character_count
    limit = user.subscription.character_limit
    left = limit - used
    print(f'{left} left ::: {used} out of {limit}')
    return [used, left,limit]
    
def get_models():
    from elevenlabs.api import Models
    models = Models.from_api()
    models = [f'{x.model_id}: {x.description }' for x in models]
    return models
def get_voices():
    from elevenlabs.api import Voices
    voices = Voices.from_api()
    names = [f'{x.name}: {x.voice_id }' for x in voices]
    return names
def create_voice(name, description, samples):
    from elevenlabs import clone

    voice = clone(
        name=name,
        description=description, 
        files=sample,
    )

def read_file(current_file_n):
    with open(f'transcripts/{current_file_n}.mp3.txt') as f:
        lines = f.readlines()
    return lines

def choose_lenguague_model(output_language):
    if output_language != 'english':
        model_id = "eleven_multilingual_v1"
    else:
        model_id = "eleven_monolingual_v1"
    return model_id

def send_voice_request(voice_id,
                       text,
                       output_language,
                       stability = 0.5,
                       similarity_boost = 0.5):
    
    model_id = choose_lenguague_model(output_language)
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"
    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": os.getenv("ELEVENLABS_API_KEY")
    }
    data = {
      "text": f'{text}',
      "model_id": f'{model_id}',
      "voice_settings": {
        "stability": stability,
        "similarity_boost": similarity_boost
      }
    }
    return requests.post(url, json=data, headers=headers)

def record_audio_file(request, title):
    with open(f'translated_voice/{title}_translation.mp3', 'wb') as f:
        for chunk in request.iter_content():
            if chunk:
                f.write(chunk)
def make_mp3(current_file_n, voice_id, output_language):
    text = read_file(current_file_n)[0]
    request = send_voice_request(voice_id = voice_id,
                             text = text,
                             output_language = output_language,
                             stability = 0.5, similarity_boost = 0.5)
    log_usage()
    record_audio_file(request, current_file_n)

def get_current_file_n():
    files = [int(x.split('_translation.mp3')[0]) for x in os.listdir('translated_voice') if x.endswith('.mp3')]
    if len(files) == 0:
        current_file_n = 0
    else:
        current_file_n = max(files) + 1
    return current_file_n