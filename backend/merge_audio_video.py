import os
import subprocess

def merge_audio_with_video(video_path, translated_audio_path, output_video_path):
    """Merge translated audio with the original video, ensuring sync."""
    if not os.path.exists(video_path):
        print(f"❌ Error: Video file '{video_path}' not found.")
        return False
    
    if not os.path.exists(translated_audio_path):
        print(f"❌ Error: Translated audio file '{translated_audio_path}' not found.")
        return False

    # Get durations
    video_duration = get_media_duration(video_path)
    audio_duration = get_media_duration(translated_audio_path)

    if video_duration is None or audio_duration is None:
        print("❌ Error: Failed to get media durations.")
        return False

    print(f"📏 Video Duration: {video_duration:.2f} sec, Audio Duration: {audio_duration:.2f} sec")

    # Adjust audio speed if necessary
    adjusted_audio_path = translated_audio_path
    if abs(video_duration - audio_duration) > 0.5:  # Only adjust if difference > 0.5 sec
        speed = audio_duration / video_duration  # Calculate speed factor
        adjusted_audio_path = translated_audio_path.replace(".mp3", "_adjusted.mp3")

        print(f"🔄 Adjusting audio speed by factor: {speed:.3f}")
        os.system(f'ffmpeg -i "{translated_audio_path}" -filter:a "atempo={speed}" "{adjusted_audio_path}" -y')

    # Merge video with the adjusted audio
    command = f'ffmpeg -i "{video_path}" -i "{adjusted_audio_path}" -c:v copy -map 0:v:0 -map 1:a:0 -shortest "{output_video_path}" -y'
    print("🔄 Merging translated audio with video...")
    os.system(command)

    if os.path.exists(output_video_path):
        print(f"✅ Translated video saved: {output_video_path}")
        return True
    else:
        print("❌ Error: Failed to generate translated video.")
        return False


def get_media_duration(file_path):
    """Get the duration of a media file using FFmpeg."""
    try:
        result = subprocess.run(
            ['ffmpeg', '-i', file_path, '-hide_banner'],
            stderr=subprocess.PIPE,
            text=True
        )
        duration_line = [line for line in result.stderr.split('\n') if "Duration" in line]
        if not duration_line:
            return None
        duration_str = duration_line[0].split(",")[0].split("Duration: ")[1].strip()
        h, m, s = map(float, duration_str.replace(":", " ").split())
        return h * 3600 + m * 60 + s
    except Exception as e:
        print(f"❌ Error getting duration: {e}")
        return None

