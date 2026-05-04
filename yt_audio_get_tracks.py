# yt_separator.py
# pip install yt-dlp demucs pydub (ffmpeg required)
import os, sys, subprocess
import shutil
import yt_dlp
from pydub import AudioSegment

def download_audio(url, video_id):
    temp_dir = 'separated'
    os.makedirs(temp_dir, exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(temp_dir, f'{video_id}.%(ext)s'),
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
        'keepvideo': True,
        'quiet': False,
        'no_warnings': False,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'http_headers': {'Referer': 'https://www.youtube.com/'},
        # 'cookiesfrombrowser': ('chrome', None, None),
    }

    if shutil.which('deno') is None:
        print("⚠️ Deno not found.")
        ydl_opts['compat_opts'] = ['no-youtube-js']

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return os.path.join(temp_dir, f'{video_id}.wav')

def separate_tracks(input_wav, video_id):
    if not os.path.exists(input_wav):
        raise FileNotFoundError(f"{input_wav} does not exist")
    
    output_dir = 'separated'
    subprocess.run(['demucs', '-n', 'htdemucs_6s', '--mp3', '--out', output_dir, input_wav], check=True)
    
    base = os.path.join(output_dir, 'htdemucs_6s', video_id)
    
    drums = f'{base}/drums.mp3'
    vocals = f'{base}/vocals.mp3'
    bass = f'{base}/bass.mp3'
    guitar = f'{base}/guitar.mp3'
    piano = f'{base}/piano.mp3'
    other = f'{base}/other.mp3'
    
    music = AudioSegment.from_mp3(bass).overlay(AudioSegment.from_mp3(other))
    music_path = os.path.join(base, 'music.mp3')
    music.export(music_path, format="mp3")
    
    os.remove(input_wav)
    
    return drums, vocals, guitar, bass, other, piano, music_path


def main():
    video_id = input("enter youtube video id: ")
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        wav = download_audio(url, video_id)
        d, v, g, b, o, p, m = separate_tracks(wav, video_id)
        print(d, v, g, b, o, p, m)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    main()
