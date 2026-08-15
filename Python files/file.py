from pathlib import Path
import subprocess

src = Path("/mnt/data/vidssave.com Nadiya Chale Chale Re Dhara 144P.mp4")
out = Path("/mnt/data/Nadiya_Chale_instrumental.mp3")

subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

subprocess.run([
    "ffmpeg", "-y", "-i", str(src),
    "-vn", "-af", "pan=stereo|c0=c0-c1|c1=c1-c0",
    "-codec:a", "libmp3lame", "-q:a", "2", str(out)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"Created: {out}")
