import wave
import numpy as np

with wave.open('c:/Users/Adarsh/Desktop/vidooo/mohabbat-si/audio.wav', 'rb') as w:
    rate = w.getframerate()
    nframes = w.getnframes()
    data = np.frombuffer(w.readframes(nframes), dtype=np.int16)
    if w.getnchannels() == 2:
        data = data.reshape(-1, 2).mean(axis=1)

# Let's inspect energy envelopes in 100ms bins across the 4 phrases
def get_peaks(start_t, end_t, step=0.1):
    s_idx = int(start_t * rate)
    e_idx = int(end_t * rate)
    step_samples = int(step * rate)
    sub = data[s_idx:e_idx]
    bins = [np.abs(sub[i:i+step_samples]).mean() for i in range(0, len(sub)-step_samples, step_samples)]
    return [(start_t + i*step, b) for i, b in enumerate(bins)]

print("Phrase 1 (0 to 4.5s):")
for t, b in get_peaks(0.0, 4.5, 0.2):
    if b > 1500:
        print(f"  {t:.1f}s: {'#' * int(b / 300)}")

print("\nPhrase 2 (4.5 to 8.8s):")
for t, b in get_peaks(4.5, 8.8, 0.2):
    if b > 1500:
        print(f"  {t:.1f}s: {'#' * int(b / 300)}")

print("\nPhrase 3 (8.8 to 13.5s):")
for t, b in get_peaks(8.8, 13.5, 0.2):
    if b > 1500:
        print(f"  {t:.1f}s: {'#' * int(b / 300)}")

print("\nPhrase 4 (13.5 to 18.17s):")
for t, b in get_peaks(13.5, 18.17, 0.2):
    if b > 1500:
        print(f"  {t:.1f}s: {'#' * int(b / 300)}")
