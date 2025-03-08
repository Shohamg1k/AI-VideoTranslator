import os
from pytube import YouTube

UPLOADS_DIR = "backend/uploads"

def download_youtube_video(youtube_url):
    """Downloads a YouTube video and saves it to the uploads directory."""
    try:
        os.makedirs(UPLOADS_DIR, exist_ok=True)
        
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

        video_path = os.path.join(UPLOADS_DIR, f"{yt.title}.mp4")
        stream.download(output_path=UPLOADS_DIR, filename=f"{yt.title}.mp4")

        print(f"✅ Video downloaded: {video_path}")
        return video_path
    except Exception as e:
        print(f"❌ Error downloading video: {e}")
        return None
