import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import time


sr = 22050
N_CHUNKS = False
S_CHUNKS = 60

sd.default.device = 1

def record_batch(seconds: int):
    recording = sd.rec(int(seconds * sr), 
                       samplerate=sr, channels=1)
    sd.wait()
    name = str(time.time()).replace('.','_')
    write(f"records/{name}.mp3", sr, recording)

    
def record(seconds:int, stop_at_n_chunks = False):
    done = 0
    while True:
        print('recording started')
        record_batch(seconds = seconds)
        print('one more finished')
        if stop_at_n_chunks:
            done +=1
            if done == stop_at_n_chunks:
                print('done')
                break
                

if __name__ == "__main__":
    record(S_CHUNKS, N_CHUNKS)