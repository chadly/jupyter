from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound
from pytube import YouTube
import re

def sanitize_filename(filename):
    return re.sub(r'[\\/:"*?<>|]', '_', filename)

def format_srt(transcript):
    """Convert transcript to SRT format."""
    srt_string = ''
    for i, item in enumerate(transcript):
        start = item['start']
        duration = item['duration']
        end = start + duration
        start_time = format_time_srt(start)
        end_time = format_time_srt(end)

        srt_string += f"{i+1}\n"
        srt_string += f"{start_time} --> {end_time}\n"
        srt_string += f"{item['text']}\n\n"
    return srt_string

def format_time_srt(seconds):
    """Convert time in seconds to SRT time format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:06.3f}".replace('.', ',')

def download_transcript(video_url):
    video_id = video_url.split("v=")[1]

    yt = YouTube(video_url)
    title = yt.title

    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        sanitized_title = sanitize_filename(title)
        transcript_text = "\n".join([entry['text'] for entry in transcript_data])

        srt_transcript = format_srt(transcript_data)

        with open(f'agent_workspace/{sanitized_title}.txt', 'w', encoding='utf-8') as file:
            file.write(transcript_text)

        with open(f"agent_workspace/{sanitized_title}.srt", "w") as file:
            file.write(srt_transcript)

        print(f'Transcript saved as {sanitized_title}')
    except Exception as e:
        print(f'Error: {e}')
