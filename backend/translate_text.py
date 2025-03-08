import requests

def translate_text(text, target_language):
    url = "http://localhost:5000/translate"  # Use self-hosted LibreTranslate
    translated_chunks = []

    for i in range(0, len(text), 5000):  # Chunking
        chunk = text[i:i+5000]
        payload = {"q": chunk, "source": "en", "target": target_language, "format": "text"}

        response = requests.post(url, json=payload)
        data = response.json()

        if "translatedText" in data:
            translated_chunks.append(data["translatedText"])
        else:
            print(f"❌ Error: {data}")
            return None

    return " ".join(translated_chunks)

# ✅ **Test**
if __name__ == "__main__":
    long_text = "This is a long text for translation." * 100
    translated_output = translate_text(long_text, "hi")
    print("Translated Output:", translated_output)




