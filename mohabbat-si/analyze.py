import wave
import numpy as np

with wave.open('c:/Users/Adarsh/Desktop/vidooo/mohabbat-si/audio.wav', 'rb') as w:
    rate = w.getframerate()
    nframes = w.getnframes()
    data = np.frombuffer(w.readframes(nframes), dtype=np.int16)
    if w.getnchannels() == 2:
        data = data.reshape(-1, 2).mean(axis=1)

dur = nframes / rate
print(f"Duration: {dur:.3f} s, Rate: {rate} Hz")

# Compute envelope over 20ms frames
frame_len = int(rate * 0.02)
num_frames = len(data) // frame_len
envelope = [np.abs(data[i*frame_len:(i+1)*frame_len]).mean() for i in range(num_frames)]
times = [i * 0.02 for i in range(num_frames)]

# Print energy summary around key phrase marks: 0s, 4.5s, 8.8s, 13.5s, 18.17s
print("Energy peaks / dips around suspected phrase boundaries:")
for target_t in [0.0, 1.0, 2.0, 3.0, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 8.8, 9.5, 11.0, 13.0, 13.5, 15.0, 17.0, 18.0]:
    idx = int(target_t / 0.02)
    if idx < len(envelope):
        print(f"t={target_t:5.2f}s : env={envelope[idx]:6.0f}")
