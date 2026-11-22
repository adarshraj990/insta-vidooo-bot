import subprocess
import os

ref_vid = r"C:\Users\Adarsh\.gemini\antigravity\brain\cd8a35e2-ce20-4432-b290-dba28a901dd0\.user_uploaded\media_1795250307826_b0663511.mp4"
new_aud = r"C:\Users\Adarsh\.gemini\antigravity\brain\cd8a35e2-ce20-4432-b290-dba28a901dd0\.user_uploaded\media_1795250316116_b4eb0cde.mpeg"
out_dir = r"c:\Users\Adarsh\Desktop\vidooo\ref_inspect"
os.makedirs(out_dir, exist_ok=True)

print("=== VIDEO PROBE ===")
res_v = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration,size,bit_rate", "-show_entries", "stream=codec_name,width,height,r_frame_rate", ref_vid], capture_output=True, text=True)
print(res_v.stdout)

print("=== AUDIO PROBE ===")
res_a = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration,size,bit_rate", "-show_entries", "stream=codec_name,sample_rate,channels", new_aud], capture_output=True, text=True)
print(res_a.stdout)

print("=== EXTRACTING VIDEO FRAMES ===")
subprocess.run(["ffmpeg", "-y", "-i", ref_vid, "-vf", "fps=1", "-frames:v", "20", os.path.join(out_dir, "frame_%02d.jpg")], check=True)

print("=== EXTRACTING AUDIO TO WAV FOR TRANSCRIPTION ===")
aud_wav = r"c:\Users\Adarsh\Desktop\vidooo\ref_inspect\new_audio.wav"
subprocess.run(["ffmpeg", "-y", "-i", new_aud, "-ar", "16000", "-ac", "1", aud_wav], check=True)
print("Done extracting audio to wav.")
