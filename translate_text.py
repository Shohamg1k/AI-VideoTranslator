import requests

def translate_text(text, target_language):
    """
    Translates English text to the specified target language using LibreTranslate.
    `target_language` should be a code like 'hi', 'fr', 'es', etc.
    """
    url = "http://localhost:5000/translate"
    translated_chunks = []

    for i in range(0, len(text), 5000):  # LibreTranslate input limit
        chunk = text[i:i+5000]
        payload = {
            "q": chunk,
            "source": "en",
            "target": target_language,
            "format": "text"
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()
            if "translatedText" in data:
                translated_chunks.append(data["translatedText"])
            else:
                print("❌ LibreTranslate error:", data)
                return None
        except Exception as e:
            print(f"❌ Failed to connect to LibreTranslate: {e}")
            return None

    return " ".join(translated_chunks)
