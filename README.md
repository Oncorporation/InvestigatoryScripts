# InvestigatoryScripts
scripts used to investigate data on the internet

Because search engines and many LLM are censored, it is difficult to find information on the internet. This repository contains scripts that can be used to investigate data on the internet.


## Installation

None. However, these scripts are written in Python and may require the custom libraries. These libraries links are included in the repository.

If you want to install the required Python packages from the command line, run:

```powershell
pip install -r requirements.txt
```

## Running the scripts

Run each script from the repository root with Python:

```powershell
python yt_audio_get_tracks.py
python yt_videos_get_json.py
python yt_get_json.py
```

`yt_audio_get_tracks.py` will prompt for a single YouTube video id.
`yt_videos_get_json.py` will prompt for a YouTube video id value.
`yt_get_json.py` will prompt for a YouTube channel id and an API key.

### yt_audio_get_tracks.py output

This script downloads audio, separates stems with Demucs, and writes the combined music track into a video-specific folder:

```powershell
separated\htdemucs\<video_id>\music.mp3
```

The other separated tracks are written alongside it in the same folder.

### yt_videos_get_json.py

Prompts for one YouTube video id and a filter string, then writes the filtered transcript JSON to a file named like:

```powershell
videos_<filter>_filtered.json
```

### yt_get_json.py

Prompts for a YouTube channel id, an API key, and a filter string, then writes the filtered channel transcript JSON to a file named like:

```powershell
<channel>_<filter>_filtered.json
```


Download: https://github.com/denoland/deno/releases/latest/download/deno-x86_64-pc-windows-msvc.zip
Extract deno.exe to script folder or PATH.
