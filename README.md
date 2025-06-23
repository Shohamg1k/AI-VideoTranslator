## 🎬 Video Translation Backend — README

This project processes uploaded or YouTube videos to:

1. Extract audio
2. Transcribe speech (via Whisper)
3. Translate the transcript (via LibreTranslate)
4. Generate translated audio (via gTTS)
5. Merge audio with video using FFmpeg

---


## ⚙️ Setup Instructions

### 1. 🔁 Clone & Navigate

```bash
git clone <https://github.com/Shohamg1k/AI-VideoTranslator>
cd VideoTrans-main/backend
```

### 2. 🐍 Create Virtual Environment

```bash
python -m venv venv
```

### 3. ✅ Activate Virtual Environment

* **Windows (Git Bash / MINGW64):**

  ```bash
  source venv/Scripts/activate
  ```


You should see `(venv)` at the beginning of your terminal prompt.

---

### 4. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. ⬇️ Install FFmpeg (Required for audio/video handling)

* Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
* Add `ffmpeg` to your system's PATH environment variable.
* Test it works:

  ```bash
  ffmpeg -version
  ```

---

### 6. 🌍 Run LibreTranslate Server Locally

This backend uses [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) for translation.

#### Option A: Use Docker (Recommended)
Download docker, Log in and then run the next cmd

```bash
docker run -p 5000:5000 libretranslate/libretranslate
```



## 🚀 Run the Server

From the `backend/` directory:

```bash
uvicorn main:app --reload
```

Server will start at: `http://127.0.0.1:8000`

---



