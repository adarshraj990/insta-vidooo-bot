import wave
import numpy as np
import json

with wave.open('c:/Users/Adarsh/Desktop/vidooo/hum-tadapte/audio.wav', 'rb') as w:
    rate = w.getframerate()
    nframes = w.getnframes()
    data = np.frombuffer(w.readframes(nframes), dtype=np.int16)
    if w.getnchannels() == 2:
        data = data.reshape(-1, 2).mean(axis=1)

dur = nframes / float(rate)
print(f"Total duration: {dur:.2f}s")

# Let's check energy envelopes
step = 0.1
step_samples = int(step * rate)
bins = [np.abs(data[i:i+step_samples]).mean() for i in range(0, len(data)-step_samples, step_samples)]

def print_peaks(start_t, end_t, label):
    print(f"\n--- {label} ({start_t}s - {end_t}s) ---")
    s_idx = int(start_t / step)
    e_idx = int(end_t / step)
    for i in range(s_idx, min(e_idx, len(bins))):
        t = i * step
        b = bins[i]
        if b > 1200:
            print(f"  {t:4.1f}s: {'#' * int(b / 250)}")

print_peaks(0.0, 5.5, "Act 1: Mat Jao Na Bechain Karke Mujhe")
print_peaks(5.5, 10.5, "Act 2: Hum Tadapte Rahenge Yahan Raat Bhar")
print_peaks(10.5, 15.5, "Act 3: Tum To Aaram Ki Neend So Jaoge")
print_peaks(15.5, 20.01, "Act 4: Hum Tadapte Rahenge Yahan Raat Bhar (Climax)")
