import os
import requests
from requests import Response
from typing import BinaryIO
import time
from dotenv import load_dotenv
load_dotenv('.env')
from record_voice_utils import *


def record_reading(voice_id = 'VR6AewLTigWG4xSOukaG'):
    
    while True:
        if len(os.listdir('transcripts')) == 0:
            time.sleep(5)
        else:
            read_transcript(voice_id)
            
            
if __name__ == '__main__':
    record_reading()