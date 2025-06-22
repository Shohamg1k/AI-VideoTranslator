import os
import yt_dlp

UPLOADS_DIR = "backend/uploads"

def download_youtube_video(youtube_url):
    """Downloads a YouTube video using yt-dlp."""
    try:
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': os.path.join(UPLOADS_DIR, '%(title)s.%(ext)s'),
            'quiet': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            video_title = info_dict.get('title', None)
            ext = info_dict.get('ext', 'mp4')
            downloaded_path = os.path.join(UPLOADS_DIR, f"{video_title}.{ext}")

        print(f"✅ Video downloaded: {downloaded_path}")
        return downloaded_path
    except Exception as e:
        print(f"❌ Error downloading video: {e}")
        return None
