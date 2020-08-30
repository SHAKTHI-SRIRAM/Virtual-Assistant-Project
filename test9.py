import os
import time
import speech_recognition as sr
import playsound
import random
from gtts import gTTS
from time import ctime
import webbrowser
import wikipedia
r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        voice_data = r.record(source, duration = 5)
        try:
            print("Recognizing...")
            voice_data = r.recognize_google(voice_data)
        except sr.UnknownValueError:
            speak("SORRY, I CAN'T GET YOU")
            print(':-(')
            exit()

        except sr.RequestError:
            speak('MY SPEECH SERVICE IS DOWN')
        return voice_data
def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    r = random.randint(1,100000000)
    ado_file = 'ado-' + str(r) + '.mp3'
    tts.save(ado_file)
    playsound.playsound(ado_file)
    print(text)
    os.remove(ado_file)
def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Cookie')
        speak('My name is Cookie')
    if "what's your name" in voice_data:
        print('My name is Cookie')
        speak('My name is Cookie')
    if 'who are you' in voice_data:
        print('My name is Cookie. The Virtual Assistant. Version 2.0')
        speak('My name is Cookie. The Virtual Assistant. Version 2.0')
    if 'tell me about yourself' in voice_data:
        print('I am Cookie. The Virtual Assistant. Version 2.0')
        speak('I am Cookie. The Virtual Assistant. Version 2.0')
    if 'what is the time' in voice_data:
        print(ctime())
        speak(ctime())
    if 'what time is it' in voice_data:
        print(ctime())
        speak(ctime())
    if 'tell me the time' in voice_data:
        print(ctime())
        speak(ctime())
    if 'search' in voice_data:
        search = record_audio(speak('What I need to Search'))
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('HERE IS WHAT I HAVE FOUND FOR ' + search.upper())
    if 'find location' in voice_data:
        location = record_audio(speak('what is the name of the place'))
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('HERE IS THE LOCATION OF ' + location.upper())
        speak('HERE IS THE LOCATION OF ' + location.upper())
    if 'location' in voice_data:
        location = record_audio(speak('what is the name of the place'))
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('HERE IS THE LOCATION OF ' + location.upper())
        speak('HERE IS THE LOCATION OF ' + location.upper())
    if 'open Wikipedia' in voice_data:
        search_wiki = record_audio(speak('What I need to Search in wikipedia'))
        search_wiki = wikipedia.summary(search_wiki, sentences = 2)
        print(search_wiki)
        speak(search_wiki)
    if 'thanks' in voice_data:
        speak('YOU ARE WELCOME')
        exit()
time.sleep(1)
speak('POWER ON')
speak('HI, HOW CAN I HELP YOU')
while 1:
    voice_data = record_audio()#text is the line which we speak
    print(voice_data)
    respond(voice_data)
