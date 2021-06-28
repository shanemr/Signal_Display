import pyaudio

# Constants for recording
CHUNK = 1024 * 4  # Recording sample chunks of 1024 samples per chunk
SAMPLE_FORMAT = pyaudio.paInt16  # 16 bits per sample
FREQUENCY = 44100  # Record 44100 samples per second
CHANNEL = 1
