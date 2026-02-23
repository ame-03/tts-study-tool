from gtts import gTTS
import os

def synthesize(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)