import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import time


sr = 22050
seconds = 60

sd.default.device = 1

def record_batch(seconds = 60):
    recording = sd.rec(int(seconds * sr), 
                       samplerate=sr, channels=1)
    sd.wait()
    name = str(time.time()).replace('.','_')
    write(f"records/{name}.mp3", sr, recording)