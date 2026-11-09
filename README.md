# 🩺 AI Doctor — Vision & Voice Medical Assistant

An AI-powered doctor assistant that can **see** (analyze medical images), **listen** (transcribe patient speech), and **speak** (respond with a natural voice). Built with Groq, ElevenLabs, and Gradio.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Gradio](https://img.shields.io/badge/Gradio-5.12-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **🧠 Medical Image Analysis** — Upload a photo (skin condition, rash, etc.) and get an AI-powered assessment using Groq's multimodal LLM (`qwen/qwen3.6-27b`).
- **🎤 Voice Input** — Speak your symptoms via microphone; audio is transcribed to text using Groq's Whisper model (`whisper-large-v3`).
- **🔊 Voice Response** — The doctor's response is converted to natural speech using **ElevenLabs** (high quality) or **gTTS** (free fallback).
- **🖥️ Web UI** — Clean Gradio interface for easy interaction.

## 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  voice_of_the   │     │   brain_of_the      │     │  voice_of_the       │
│  patient.py     │────▶│   doctor.py         │────▶│  doctor.py          │
│  (Speech→Text)  │     │   (Image Analysis)  │     │  (Text→Speech)      │
│  Groq Whisper   │     │   Groq Multimodal   │     │  ElevenLabs / gTTS  │
└─────────────────┘     └─────────────────────┘     └─────────────────────┘
         ▲                        ▲                           │
         │                        │                           ▼
         └────────────── gradio_app.py ◀──────────────────────┘
                        (Web Interface)
```

## 📋 Prerequisites

- **Python 3.11+**
- **FFmpeg** — required by `pydub` for audio processing
- **PortAudio** — required by `PyAudio` for microphone access
- **API Keys:**
  - [Groq API Key](https://console.groq.com/) — for image analysis & speech transcription
  - [ElevenLabs API Key](https://elevenlabs.io/) — for high-quality text-to-speech (optional; gTTS works without it)

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd AI_DOCTOR
```

### 2. Install system dependencies

<details>
<summary><strong>Windows</strong></summary>

```powershell
# Install FFmpeg via winget
winget install Gyan.FFmpeg

# PyAudio wheel is included in requirements.txt; if it fails:
pip install pipwin
pipwin install pyaudio
```

</details>

<details>
<summary><strong>macOS</strong></summary>

```bash
brew install ffmpeg portaudio
```

</details>

<details>
<summary><strong>Linux (Ubuntu/Debian)</strong></summary>

```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev python3-pyaudio
```

</details>

### 3. Set up a virtual environment

**Option A — Using `pipenv` (recommended):**

```bash
pip install pipenv
pipenv install
pipenv shell
```

**Option B — Using `pip` + `venv`:**

```bash
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

> [!IMPORTANT]
> If you are **not** using `pipenv`, uncomment the `dotenv` lines at the top of each Python file:
> ```python
> from dotenv import load_dotenv
> load_dotenv()
> ```

### 5. Run the app

```bash
python gradio_app.py
```

Then open **http://127.0.0.1:7860** in your browser.

## 🎮 How to Use

1. **Record** your symptoms using the microphone button in the web UI.
2. **Upload** an image of the medical condition (skin rash, acne, etc.).
3. **Submit** — the AI doctor will:
   - Transcribe your voice to text
   - Analyze the image with your query
   - Respond with a spoken diagnosis

## 📁 Project Structure

```
AI_DOCTOR/
├── gradio_app.py              # Main app — Gradio web interface
├── brain_of_the_doctor.py     # Image analysis with Groq multimodal LLM
├── voice_of_the_patient.py    # Mic recording + speech-to-text (Groq Whisper)
├── voice_of_the_doctor.py     # Text-to-speech (ElevenLabs & gTTS)
├── scratch_test.py            # Test script for image analysis
├── scratch_eleven.py          # Test script for ElevenLabs TTS
├── .env                       # API keys (DO NOT commit!)
├── Pipfile                    # Pipenv dependency file
├── Pipfile.lock               # Pipenv lock file
├── requirements.txt           # pip dependency file
└── README.md                  # You are here
```

## 🔧 Configuration

| Setting | File | Default |
|---|---|---|
| Vision model | `brain_of_the_doctor.py` | `qwen/qwen3.6-27b` |
| STT model | `voice_of_the_patient.py` | `whisper-large-v3` |
| TTS engine | `gradio_app.py` | ElevenLabs (`text_to_speech_with_elevenlabs`) |
| TTS voice ID | `voice_of_the_doctor.py` | `Xb7hH8MSUJpSbSDYk0k2` |
| Recording timeout | `voice_of_the_patient.py` | 20 seconds |

To switch to the **free gTTS** engine, change line 35 in `gradio_app.py`:

```python
# From:
voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3")
# To:
voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath="final.mp3")
```

## ⚠️ Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'pyaudio'` | Install PortAudio first (see prerequisites), then `pip install pyaudio` |
| `FileNotFoundError: ffmpeg not found` | Install FFmpeg and ensure it's on your `PATH` |
| `groq.AuthenticationError` | Check your `GROQ_API_KEY` in `.env` |
| `elevenlabs` errors | Check your `ELEVENLABS_API_KEY` or switch to gTTS |
| `.env` not loading | Uncomment the `load_dotenv()` lines if not using `pipenv` |

## ⚠️ Disclaimer

> This project is for **educational/learning purposes only**. The AI doctor does **not** provide real medical advice. Always consult a qualified healthcare professional for medical concerns.

