import os
import whisper

def extract_text_from_audio(audio_path):
    """Extracts text from an audio file using Whisper."""
    print(f"🎵 Processing audio file: {audio_path}")

    if not os.path.exists(audio_path):
        print("❌ Error: Audio file not found.")
        return None

    print("🔄 Loading Whisper model...")
    model = whisper.load_model("base")
    print("✅ Whisper model loaded. Starting transcription...")

    try:
        result = model.transcribe(audio_path)
        print("✅ Transcription successful.")
        return result["text"]
    except Exception as e:
        print(f"❌ Error transcribing audio: {e}")
        return None
