
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

import constants as c

# Create stream for audio
p = pyaudio.PyAudio()

stream = p.open(
    format=c.SAMPLE_FORMAT,
    channels=c.CHANNEL,
    rate=c.FREQUENCY,
    input=True,
    frames_per_buffer=c.CHUNK,
    input_device_index=1

)


while True:
    data = stream.read(c.CHUNK)
    data_int = np.frombuffer(data, dtype=np.int16) + 127
    plt.pause(0.05)
    plt.figure(figsize=(15, 7))
    plt.plot(data_int)



plt.show()

stream.stop_stream()
stream.close()

p.terminate()









