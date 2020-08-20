import os
import time
import speech_recognition as sr
import playsound
from gtts import gTTS
from time import ctime

r = sr.Recognizer()
def record_audio():
    with sr.Microphone() as source:
        voice_data = r.record(source, duration = 5)
        try:
            print("Recognizing...")
            voice_data = r.recognize_google(voice_data)
        except sr.UnknownValueError:
            print("SORRY, I CAN'T GET YOU")
        except sr.RequestError:
            print('MY SPEECH SERVICE IS DOWN')
        return voice_data
def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    file_name = 'Cookie_response.mp3'
    tts.save(file_name)
    playsound.playsound(file_name)


print('HOW CAN I HELP YOU?')
voice_data = record_audio()#text is the line which we speak
print(voice_data)
if 'what is your name' in voice_data:
    print('My name is Cookie')
    speak('My name is Cookie')
if 'tell me about yourself' in voice_data:
    print('I am Cookie. The Virtual Assistant. Version 2.0')
    speak('I am Cookie. The Virtual Assistant. Version 2.0')    
if 'what is the time' in voice_data:
    print(ctime())
    speak(ctime())
