import os
import time
import speech_recognition as sr
import playsound
import random
from gtts import gTTS
from time import ctime
import webbrowser
import wikipedia
import pywhatkit as kit
def listen_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice_data = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(voice_data)
            print(said)
        except Exception as e:
            print('Recognizing' + str(e))
    return said
def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    r = random.randint(1,100000000)
    ado_file = 'ado-' + str(r) + '.mp3'
    tts.save(ado_file)
    playsound.playsound(ado_file)
    print(text)
    os.remove(ado_file)
def respond(voice_data):
    if 'good morning cookie' in voice_data:
        speak('Good Morning')
    if 'good afternoon cookie' in voice_data:
        speak('Good Afternoon')
    if 'how are you doing cookie' in voice_data:
        speak('Pretty Well')
    if 'how are you cookie' in voice_data:
        speak('I am fine how about you')
    if 'i am fine' in voice_data:
        speak('Great')
    if 'what is your name' in voice_data:
        speak('My name is Cookie')
    if "what's your name" in voice_data:
        speak('My name is Cookie')
    if 'who are you' in voice_data:
        speak('My name is Cookie. The Virtual Assistant. Version 2.0')
    if 'tell me about yourself' in voice_data:
        speak('I am Cookie. The Virtual Assistant. Version 2.0')
    if 'hey cookie what is the time' in voice_data:
        speak(ctime())
    if 'what is the time cookie' in voice_data:
        speak(ctime())
    if 'hey cookie what time is it' in voice_data:
        speak(ctime())
    if 'what time is it cookie' in voice_data:
        speak(ctime())
    if 'tell me the time cookie' in voice_data:
        speak(ctime())
    if 'hey cookie tell me the time' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search = listen_audio(speak('What I need to Search'))
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('HERE IS WHAT I HAVE FOUND FOR ' + search.upper())
    if 'open Google' in voice_data:
        search = listen_audio(speak('What I need to Search in Google'))
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('HERE IS WHAT I HAVE FOUND FOR ' + search.upper())
    if 'find location' in voice_data:
        location = listen_audio(speak('what is the name of the place'))
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('HERE IS THE LOCATION OF ' + location.upper())
    if 'open Google maps' in voice_data:
        location = listen_audio(speak('what is the name of the place'))
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('HERE IS THE LOCATION OF ' + location.upper())
    if 'open Wikipedia' in voice_data:
        search_wiki = listen_audio(speak('What I need to Search in wikipedia'))
        search_wiki = wikipedia.summary(search_wiki, sentences = 3)
        speak(search_wiki)
    if 'open YouTube' in voice_data:
        tube_search = listen_audio(speak('What I need to Search in Youtube'))
        kit.playonyt(tube_search)
        speak('Carry On I have opened it')
    if 'thanks' in voice_data:
        speak('YOU ARE WELCOME')
        exit()
print('>__<')
speak("YOUR VIRTUAL ASSISTANT IS READY TO WORK WITH YOU")
while 1:
    voice_data = listen_audio()#text is the line which we speak
    respond(voice_data)
