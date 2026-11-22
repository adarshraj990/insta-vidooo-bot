"""Score, procedural foley, and voice mix for Ambani Ka Sach (50.0 s, 120 BPM)."""
import json
import os
import wave
import numpy as np
from scipy.signal import butter, lfilter, resample_poly

HERE = os.path.dirname(os.path.abspath(__file__))
TL = json.load(open(os.path.join(HERE, 'timeline.json'), encoding='utf-8'))
EV = json.load(open(os.path.join(HERE, 'events.json'), encoding='utf-8'))['ev']

SR = 44100
DUR = float(TL['dur'])
N = int(SR * DUR)
BEAT = 0.5
BAR = 2.0
rng = np.random.default_rng(1958)

music_L = np.zeros(N, dtype=np.float64)
music_R = np.zeros(N, dtype=np.float64)
sfx_L = np.zeros(N, dtype=np.float64)
sfx_R = np.zeros(N, dtype=np.float64)
voice_buf = np.zeros(N, dtype=np.float64)


def mtof(m):
    return 440.0 * 2.0 ** ((m - 69) / 12.0)


def add_stereo(bufL, bufR, sig, t0, gain=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N or i + len(sig) <= 0:
        return
    if i < 0:
        sig = sig[-i:]
        i = 0
    sig = sig[: N - i] * gain
    l = np.cos((pan + 1.0) * np.pi / 4.0)
    r = np.sin((pan + 1.0) * np.pi / 4.0)
    bufL[i:i + len(sig)] += sig * l * 1.414
    bufR[i:i + len(sig)] += sig * r * 1.414


def lp(x, fc, order=2):
    b, a = butter(order, min(fc / (SR / 2), 0.98))
    return lfilter(b, a, x)


def hp(x, fc, order=2):
    b, a = butter(order, max(fc / (SR / 2), 0.001), 'high')
    return lfilter(b, a, x)


def bp(x, lo, hi, order=2):
    b, a = butter(order, [max(lo / (SR / 2), 0.001), min(hi / (SR / 2), 0.98)], 'band')
    return lfilter(b, a, x)


def env(n, a=0.002, d=0.2, hold=None, rel=0.05):
    t = np.arange(n) / SR
    e = np.minimum(1.0, t / max(a, 1e-4))
    if hold is None:
        return e * np.exp(-np.maximum(0.0, t - a) / d)
    return np.where(t < hold, e, e * np.exp(-(t - hold) / rel))


# ---------- Instruments ----------
def kick(g=1.0):
    n = int(0.32 * SR)
    t = np.arange(n) / SR
    f = 48.0 + 105.0 * np.exp(-t * 28.0)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9.5)
    s += 0.2 * np.exp(-t * 280.0) * rng.standard_normal(n) * 0.25
    return np.tanh(s * 1.5) * g


def snare():
    n = int(0.20 * SR)
    t = np.arange(n) / SR
    noise = bp(rng.standard_normal(n), 1500, 7500) * np.exp(-t * 19.0)
    tone = np.sin(2 * np.pi * 195 * t) * np.exp(-t * 32.0)
    return noise * 0.65 + tone * 0.45


def snap():
    n = int(0.075 * SR)
    t = np.arange(n) / SR
    return bp(rng.standard_normal(n), 2100, 7200) * np.exp(-t * 68.0) * 0.75


def hat(open_=False):
    n = int((0.16 if open_ else 0.045) * SR)
    t = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7200) * np.exp(-t * (18.0 if open_ else 90.0)) * 0.30


def bass(m, dur=0.22):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = mtof(m)
    ph = 2 * np.pi * f * t
    # Fundamental + 2nd & 3rd harmonics so bass speaks on small speakers
    s = np.sin(ph) + 0.35 * np.sin(2 * ph) + 0.18 * np.sin(3 * ph)
    s = lp(s, 850)
    return s * env(n, 0.004, 0.16, hold=dur * 0.68, rel=0.03)


def pluck(m, dur=0.34, bright=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = mtof(m)
    s = (np.sin(2 * np.pi * f * t) * np.exp(-t * 7.2)
         + 0.34 * bright * np.sin(2 * np.pi * f * 3.99 * t) * np.exp(-t * 28.0)
         + 0.12 * np.sin(2 * np.pi * f * 2.0 * t) * np.exp(-t * 12.0))
    return s * np.minimum(1.0, t / 0.002)


def pizz(m, dur=0.18):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = mtof(m)
    s = lp(np.sign(np.sin(2 * np.pi * f * t)) * 0.55 + np.sin(2 * np.pi * f * t), 1450)
    return s * np.exp(-t * 15.0) * np.minimum(1.0, t / 0.003)


def pad(ms, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for m in ms:
        m = max(48, m)  # avoid sub-mud below MIDI 48
        f = mtof(m)
        for det in (-0.12, 0.12):
            ph = 2 * np.pi * f * (1 + det / 100.0) * t
            s += (2.0 / np.pi) * np.arcsin(np.sin(ph))
    s = lp(s / (len(ms) * 2), 2000)
    a = np.minimum(1.0, t / 0.10)
    r = np.minimum(1.0, (dur - t) / 0.16)
    return s * a * np.clip(r, 0.0, 1.0)


def bell(m, dur=1.6):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = mtof(m)
    s = (np.sin(2 * np.pi * f * t) * np.exp(-t * 2.5)
         + 0.38 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 6.0)
         + 0.18 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 11.0))
    return s * np.minimum(1.0, t / 0.001)


# ---------- Foley ----------
def sfx_stamp(big=False):
    n = int(0.85 * SR)
    t = np.arange(n) / SR
    f = 42.0 + 95.0 * np.exp(-t * 18.0)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (4.2 if big else 7.2))
    click = lp(rng.standard_normal(n), 3000) * np.exp(-t * 55.0)
    s = np.tanh((boom * 1.45 + click * 0.9) * 1.5)
    if big:
        s = s + hp(rng.standard_normal(n), 3800) * np.exp(-t * 3.4) * 0.35
    return s


def sfx_shutter():
    n = int(0.16 * SR)
    out = np.zeros(n)
    for off in (0.0, 0.06):
        i = int(off * SR)
        m = n - i
        t = np.arange(m) / SR
        out[i:] += bp(rng.standard_normal(m), 1200, 6000) * np.exp(-t * 110.0)
    return out * 0.9


def sfx_whoosh(dur=0.48):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    out = np.zeros(n)
    seg_n = 512
    for i in range(0, n, seg_n):
        p = i / n
        fc = 450 + 3400 * p
        chunk = bp(x[max(0, i - 2048):i + seg_n], fc * 0.7, fc * 1.3)
        out[i:i + seg_n] = chunk[-len(x[i:i + seg_n]):]
    return out * (np.sin(np.pi * t / dur) ** 2) * 1.15


def sfx_paper():
    n = int(0.28 * SR)
    t = np.arange(n) / SR
    return bp(rng.standard_normal(n), 1400, 5600) * (np.sin(np.pi * t / 0.28) ** 1.5) * 0.45


def sfx_click(f=2400):
    n = int(0.05 * SR)
    t = np.arange(n) / SR
    return (bp(rng.standard_normal(n), f * 0.8, f * 2.2) * 0.5 + np.sin(2 * np.pi * f * t) * 0.4) * np.exp(-t * 110.0)


def sfx_redact():
    n = int(0.11 * SR)
    t = np.arange(n) / SR
    f = 420 + 680 * (t / 0.11)
    out = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 24.0) * 0.42
    ck = sfx_click(3200) * 0.4
    out[:len(ck)] += ck[:n]
    return out


def sfx_zoom():
    n = int(0.75 * SR)
    t = np.arange(n) / SR
    f = 220 + 440 * (t / 0.75) ** 2
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / 0.75) * 0.28


# ---------- Score (D minor investigative groove, 120 BPM) ----------
# Chords per bar (25 bars = 50.0 s):
# Dm = [50, 53, 57], Bb = [46, 50, 53], Gm = [43, 46, 50], A7 = [45, 49, 52]
CHORDS = [
    # Bars 0-2 (0..6s): Cold Open
    (50, [50, 53, 57], 'intro'),
    (46, [50, 53, 58], 'intro'),
    (45, [49, 52, 57], 'intro'),
    # Bars 3-5 (6..12s): Exhibit 01 1958
    (50, [50, 53, 57], 'full'),
    (48, [48, 52, 55], 'full'),
    (46, [50, 53, 58], 'full'),
    # Bar 6 (12..14s): ends at 12.65 silence, resumes 14.0 on stamp
    (45, [49, 52, 57], 'split_sil1'),
    # Bars 7-10 (14..22s): Exhibit 02 1977 7x IPO
    (50, [50, 53, 57], 'drive'),
    (46, [50, 53, 58], 'drive'),
    (48, [48, 52, 55], 'drive'),
    (45, [49, 52, 57], 'drive'),
    # Bars 11-15 (22..32s): Exhibit 03 2000 Jamnagar
    (50, [50, 53, 57], 'tech'),
    (43, [50, 55, 58], 'tech'),
    (46, [50, 53, 58], 'tech'),
    (45, [49, 52, 57], 'tech'),
    (50, [50, 53, 57], 'cut_dark'),
    # Bars 16-19 (32..40s): Exhibit 04 2016 Dark Classified (sneak + Silence #2 39.15..40)
    (50, [50, 53, 57], 'sneak'),
    (43, [50, 55, 58], 'sneak'),
    (46, [50, 53, 58], 'sneak'),
    (45, [49, 52, 57], 'sneak_end'),
    # Bars 20-23 (40..48s): Evidence Board + Verdict
    (50, [50, 53, 57], 'resolve'),
    (46, [50, 53, 58], 'resolve'),
    (48, [48, 52, 55], 'resolve'),
    (50, [50, 53, 57], 'verdict_drop'),
    # Bar 24 (48..50s): Bell tag
    (50, [50, 53, 57], 'tag'),
]

MELODY_A = [62, 65, 69, 65, 67, 65, 64, 62]
MELODY_B = [69, 67, 65, 64, 62, 65, 67, 69]

for b_idx, (root, triad, mode) in enumerate(CHORDS):
    t_bar = b_idx * BAR
    if mode == 'tag':
        for k, note in enumerate([69, 74, 77, 81]):
            add_stereo(music_L, music_R, bell(note, 1.8), t_bar + k * 0.14, 0.28, -0.2 + 0.13 * k)
        continue

    if mode in ('intro', 'full', 'drive', 'tech', 'cut_dark', 'resolve'):
        add_stereo(music_L, music_R, pad(triad, BAR), t_bar, 0.14 if mode != 'intro' else 0.10)

    for step in range(8):
        t_st = t_bar + step * 0.25
        # Honour Silence #1 (12.65..13.50) and Silence #2 (39.50..40.00) and pre-VERIFIED breath (47.20..47.50)
        if 12.60 <= t_st < 13.50 or 39.15 <= t_st < 40.00 or 47.15 <= t_st < 47.55:
            continue

        if mode == 'sneak' or mode == 'sneak_end':
            if step in (0, 3, 6):
                add_stereo(music_L, music_R, bass(root - 12, 0.22), t_st, 0.26)
            if step in (2, 6):
                add_stereo(music_L, music_R, snap(), t_st, 0.38, 0.25)
            if step % 2 == 1:
                add_stereo(music_L, music_R, pizz(triad[step % len(triad)] + 12, 0.18), t_st, 0.22, -0.25)
            continue

        # Drums
        if mode != 'intro' and step in (0, 4):
            add_stereo(music_L, music_R, kick(0.75), t_st, 0.42)
        if mode in ('full', 'drive', 'tech', 'resolve') and step in (2, 6):
            add_stereo(music_L, music_R, snare(), t_st, 0.30)
        add_stereo(music_L, music_R, hat(step == 7), t_st, 0.16 if step % 2 == 0 else 0.10, 0.15)

        # 8th-note bass
        b_note = root - 12 if step % 2 == 0 else root
        add_stereo(music_L, music_R, bass(b_note, 0.20), t_st, 0.24)

        # Marimba pluck motif
        if step in (0, 2, 3, 5, 6):
            m_seq = MELODY_A if b_idx % 2 == 0 else MELODY_B
            add_stereo(music_L, music_R, pluck(m_seq[step], 0.30, 0.9), t_st, 0.20, -0.18 if step % 2 == 0 else 0.18)

# Subtle room tone & L-cut telecom hum for Scene 5 -> 6
room_noise = lp(hp(rng.standard_normal(N), 90), 320) * 0.014
# Zero out room tone in exact real silences
for s0, s1 in TL['silences']:
    room_noise[int(s0 * SR):int(s1 * SR)] = 0.0
music_L += room_noise
music_R += room_noise

# Subtle telecom pulse bed during Scene 5 (31.5..39.55, L-cutting 0.4s past 39.15)
t_hum = np.arange(int(8.05 * SR)) / SR
hum = (np.sin(2 * np.pi * 110 * t_hum) * 0.5 + np.sin(2 * np.pi * 220 * t_hum) * 0.25) * 0.045
hum *= np.minimum(1.0, t_hum / 0.25) * np.clip((8.05 - t_hum) / 0.45, 0.0, 1.0)
add_stereo(music_L, music_R, hum, 31.5, 1.0)

# ---------- Apply Event Foley ----------
for ev in EV:
    et = ev['t']
    tp = ev['type']
    if tp == 'paper_slide':
        add_stereo(sfx_L, sfx_R, sfx_paper(), et, 0.85, -0.15)
    elif tp == 'redact_lift':
        add_stereo(sfx_L, sfx_R, sfx_redact(), et, 0.75, 0.1)
    elif tp == 'typewriter':
        for k in range(7):
            add_stereo(sfx_L, sfx_R, sfx_click(2700 + (k % 3) * 280), et + k * 0.09, 0.55, -0.2 + 0.06 * k)
    elif tp == 'whoosh':
        add_stereo(sfx_L, sfx_R, sfx_whoosh(0.44), et - 0.12, 0.60)
    elif tp == 'stamp':
        add_stereo(sfx_L, sfx_R, sfx_stamp(ev.get('big', False)), et, 1.15 if ev.get('big') else 0.90)
    elif tp == 'shutter':
        add_stereo(sfx_L, sfx_R, sfx_shutter(), et, 0.85)
    elif tp == 'click':
        add_stereo(sfx_L, sfx_R, sfx_click(2100), et, 0.65)
    elif tp == 'zoom_swell':
        add_stereo(sfx_L, sfx_R, sfx_zoom(), et, 0.80)
    elif tp == 'pin_snap':
        add_stereo(sfx_L, sfx_R, sfx_click(1800), et, 0.70)


# ---------- Voice Compression, Placement & Music Ducking ----------
def compress(x, thresh_db=-18.0, ratio=3.5):
    env_sig = lp(np.abs(x), 35.0)
    thresh = 10 ** (thresh_db / 20.0)
    gain = np.where(env_sig > thresh, (thresh + (env_sig - thresh) / ratio) / (env_sig + 1e-9), 1.0)
    return x * gain


duck_env = np.ones(N, dtype=np.float64)
for v in TL['voices']:
    wav_path = os.path.join(HERE, 'voice', 'out', f"{v['id']}.wav")
    with wave.open(wav_path, 'rb') as wf:
        sr_in = wf.getframerate()
        raw = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float64) / 32768.0
        if wf.getnchannels() > 1:
            raw = raw.reshape(-1, wf.getnchannels()).mean(axis=1)
    if sr_in != SR:
        raw = resample_poly(raw, 441, 240)
    raw = compress(raw, thresh_db=-19.0, ratio=3.5)
    rms = np.sqrt(np.mean(raw ** 2)) + 1e-9
    raw = raw * (0.20 / rms)  # consistent strong narration RMS

    i0 = int(round(v['t0'] * SR))
    i1 = min(N, i0 + len(raw))
    voice_buf[i0:i1] += raw[: i1 - i0]

    # Duck music ~10 dB under voice with smooth ramps
    d0 = max(0, i0 - int(0.12 * SR))
    d1 = min(N, i1 + int(0.22 * SR))
    win = np.ones(d1 - d0) * 0.30
    atk = min(int(0.12 * SR), len(win) // 3)
    rel = min(int(0.22 * SR), len(win) // 3)
    if atk > 0:
        win[:atk] = np.linspace(1.0, 0.30, atk)
    if rel > 0:
        win[-rel:] = np.linspace(0.30, 1.0, rel)
    duck_env[d0:d1] = np.minimum(duck_env[d0:d1], win)

# Mix: music (ducked) + sfx + centered voice
mix_L = music_L * duck_env * 0.48 + sfx_L * 0.62 + voice_buf * 0.92
mix_R = music_R * duck_env * 0.48 + sfx_R * 0.62 + voice_buf * 0.92

# Gentle soft clip & clean fade out on final 0.5s
mix_L = np.tanh(mix_L * 1.1) * 0.88
mix_R = np.tanh(mix_R * 1.1) * 0.88
fade_n = int(0.45 * SR)
fade_curve = np.linspace(1.0, 0.0, fade_n)
mix_L[-fade_n:] *= fade_curve
mix_R[-fade_n:] *= fade_curve

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
out_wav = os.path.join(HERE, 'out', 'mix.wav')
pcm = np.stack([mix_L, mix_R], axis=1)
pcm = np.clip(pcm * 32767.0, -32767, 32767).astype(np.int16)
with wave.open(out_wav, 'wb') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(pcm.tobytes())

print(f'Wrote {out_wav} ({DUR:.1f}s, {SR}Hz stereo)')

