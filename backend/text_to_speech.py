import os
from gtts import gTTS

UPLOADS_DIR = "backend/uploads/translated"

def generate_translated_audio(text, audio_path, target_language):
    """Convert text to speech and save as an audio file in the selected language."""
    os.makedirs(UPLOADS_DIR, exist_ok=True)

    try:
        tts = gTTS(text=text, lang=target_language)  # Now uses the user-selected language
        tts.save(audio_path)
        return os.path.exists(audio_path)  # Return True if the file is created successfully
    except Exception as e:
        print(f"❌ Error: Text-to-Speech conversion failed - {e}")
        return False
