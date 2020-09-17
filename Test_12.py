import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import random
import webbrowser
import wikipedia


def speak(text):
    text_to_speech = gTTS(text = text, lang = 'en', slow=False)
    r = random.randint(1,20)
    audio_file = f'audio- {str(r)} .mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(text)
    os.remove(audio_file)

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice_data = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(voice_data)
            print(said)
        except Exception as e:
            print("Sorry I couldn't get you")
    return said

text = get_command()
if 'hello' or 'hi' in text:
    speak('Hello, How are You')
