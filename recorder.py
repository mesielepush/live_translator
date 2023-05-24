import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import time
import os
import keyboard
import sys
from pygame import key

SAMPLE_RATE = 22050
S_CHUNKS = 10
stop = 5
pressed = key.get_pressed()
sd.default.device = 1


def record_batch(seconds: int, name: str) -> ".mp3":
    recording = sd.rec(int(seconds * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write(f"records/{name}.mp3", SAMPLE_RATE, recording)


def get_current_file_n():
    files = [
        int(x.split(".mp3")[0]) for x in os.listdir("records") if x.endswith(".mp3")
    ]
    if len(files) == 0:
        return 0
    else:
        return max(files) + 1


def start_recording(seconds: int, stop: bool = False) -> None:
    current_file_n = get_current_file_n()
    print("Recording...")
    session_record_n = 0
    try:
        while True:
            record_batch(seconds=seconds, name=current_file_n)
            session_record_n += 1
            current_file_n += 1
            if stop:
                if session_record_n == stop:
                    print("done")
                    break
    except KeyboardInterrupt:
        print("Recording stopped")


if __name__ == "__main__":
    start_recording(S_CHUNKS, stop)
