"""
Audio I/O for Quantum assistant.

Handles:
- Text-to-speech (pyttsx3 with macOS 'say' fallback)
- Speech recognition (Google Speech via SpeechRecognition)
- reply() and wish() output helpers
"""

import os
import platform
import datetime
import re

import speech_recognition as sr
import pyttsx3

import quantum.state as state

_EMOJI_RE = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "]+", flags=re.UNICODE
)

IS_MAC = platform.system() == 'Darwin'

# ---------------------------------------------------------------------------
# TTS initialisation
# ---------------------------------------------------------------------------
engine = None
TTS_AVAILABLE = False

try:
    if IS_MAC:
        try:
            engine = pyttsx3.init()
            TTS_AVAILABLE = True
        except Exception as e:
            print(f"pyttsx3 not available on macOS: {e}")
            print("Quantum will use macOS 'say' command for speech instead")
    else:
        engine = pyttsx3.init('sapi5')
        TTS_AVAILABLE = True

    if TTS_AVAILABLE and engine:
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
except Exception as e:
    print(f"Text-to-speech initialization failed: {e}")
    print("Quantum will run without voice feedback")

# ---------------------------------------------------------------------------
# Speech recogniser + microphone calibration
# ---------------------------------------------------------------------------
r = sr.Recognizer()

with sr.Microphone() as _source:
    r.energy_threshold = 500
    r.dynamic_energy_threshold = False


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def _speak_async(spoken: str):
    """Speak text in a background thread so the main loop is never blocked."""
    if TTS_AVAILABLE and engine:
        try:
            engine.say(spoken)
            engine.runAndWait()
            return
        except Exception:
            pass
    if IS_MAC:
        os.system(f'say "{spoken}"')


def reply(audio):
    """Send a response to the UI and speak it aloud (TTS runs async)."""
    spoken = _EMOJI_RE.sub('', audio).strip()
    import app  # deferred to avoid import-time circular dependency
    app.ChatBot.addAppMsg(audio)
    print(audio)

    from threading import Thread
    Thread(target=_speak_async, args=(spoken,), daemon=True).start()


def wish():
    """Greet the user based on the current time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        reply("Good Morning!")
    elif 12 <= hour < 18:
        reply("Good Afternoon!")
    else:
        reply("Good Evening!")
    reply(f"I am {state.assistant_name}, how may I help you?")


def record_audio():
    """Listen to the microphone and return the recognised text (lowercase)."""
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)
        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('Sorry my Service is down. Plz check your Internet connection')
        except sr.UnknownValueError:
            print('cant recognize')
        except OSError as e:
            if 'flac' in str(e).lower():
                print("FLAC not found. Install with: brew install flac")
            else:
                print(f"Audio error: {e}")
        return voice_data.lower()
