import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import time


sr = 22050
duration = 60

sd.default.device = 1

