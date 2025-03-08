import os
import argparse
from backend.speech_to_text import extract_text_from_audio
from backend.translate_text import translate_text
from backend.text_to_speech import generate_translated_audio
from backend.merge_audio_video import merge_audio_with_video

# Ensure necessary directories exist
os.makedirs("backend/uploads/translated", exist_ok=True)

def process_uploaded_video(video_path, target_language):
    """Processes an uploaded video: extracts, transcribes, translates, and regenerates it."""
    print(f"🚀 Processing video: {video_path} | Target Language: {target_language}")

    # Step 1: Extract audio
    print("🔄 Extracting audio...")
    audio_path = os.path.join("backend/uploads", os.path.basename(video_path).replace(".mp4", ".mp3"))
    
    if not os.path.exists(video_path):
        print(f"❌ Error: Video file '{video_path}' not found.")
        return
    
    os.system(f"ffmpeg -i \"{video_path}\" -q:a 0 -map a \"{audio_path}\" -y")

    if not os.path.exists(audio_path):
        print("❌ Error: Audio extraction failed.")
        return
    
    print(f"✅ Audio extracted: {audio_path}")

    # Step 2: Transcribe audio
    print("🔄 Loading Whisper model...")
    transcription = extract_text_from_audio(audio_path)
    
    if transcription is None:
        print("❌ Error: Failed to transcribe audio.")
        return

    # Save the transcription
    transcript_path = os.path.join("backend/uploads/translated", "transcript.txt")
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(transcription)
    
    print(f"✅ Transcription saved: {transcript_path}")

    # Step 3: Translate the text
    print("🔄 Translating text...")
    translated_text = translate_text(transcription, target_language)

    if translated_text is None:
        print("❌ Error: Translation failed. Skipping this step.")
        return

    translated_text_path = os.path.join("backend/uploads/translated", f"audio_{target_language}.txt")
    with open(translated_text_path, "w", encoding="utf-8") as f:
        f.write(translated_text)
    
    print(f"✅ Translated text saved: {translated_text_path}")

    # Step 4: Convert translated text to speech
    print("🔄 Generating translated audio...")
    translated_audio_path = os.path.join("backend/uploads/translated", f"audio_{target_language}.mp3")
    
    success = generate_translated_audio(translated_text, translated_audio_path, target_language)  # Pass language here

    if not success:
        print("❌ Error: Failed to generate translated audio.")
        return

    print(f"✅ Translated audio saved: {translated_audio_path}")

    # Step 5: Merge translated audio with video
    print("🔄 Merging translated audio with video...")
    final_video_path = os.path.join("backend/uploads/translated", f"video_{target_language}.mp4")
    merge_audio_with_video(video_path, translated_audio_path, final_video_path)

    if os.path.exists(final_video_path):
        print(f"✅ Translated video saved: {final_video_path}")
    else:
        print("❌ Error: Failed to generate translated video.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process video for translation.")
    parser.add_argument("--video", type=str, required=True, help="Path to the video file")
    parser.add_argument("--lang", type=str, required=True, help="Target language for translation")

    args = parser.parse_args()
    process_uploaded_video(args.video, args.lang)
