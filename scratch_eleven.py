from voice_of_the_doctor import text_to_speech_with_elevenlabs
import sys

try:
    text_to_speech_with_elevenlabs("Hello! This is a test of the ElevenLabs voice synthesis using the voice ID.", "elevenlabs_testing.mp3")
    print("Success!")
except Exception as e:
    print("Error:", e)
    sys.exit(1)
