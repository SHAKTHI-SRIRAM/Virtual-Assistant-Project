import os
import time
import speech_recognition as sr
import playsound
import random
from gtts import gTTS
from time import ctime
import webbrowser
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
import re
r = sr.Recognizer()

# Speech-Text converting function


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        voice_data = r.record(source, duration=5)
        try:
            print("Recognizing...")
            voice_data = r.recognize_google(voice_data)
        except sr.UnknownValueError:
            speak("SORRY, I CAN'T GET YOU")
            print(':-(')

        except sr.RequestError:
            speak('MY SPEECH SERVICE IS DOWN')
        return voice_data

# Text-Speech converting function


def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    r = random.randint(1, 100000000)
    ado_file = 'ado-' + str(r) + '.mp3'
    tts.save(ado_file)
    playsound.playsound(ado_file)
    print(text)
    os.remove(ado_file)

# Function for fetching data


def respond(voice_data):
    # Cookie inbuilt responses
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
    if 'thanks' in voice_data:
        speak('YOU ARE WELCOME')
        exit()
    if 'what is the time' in voice_data:
        print(ctime())
        speak(ctime())
    if 'what time is it' in voice_data:
        print(ctime())
        speak(ctime())
    if 'tell me the time' in voice_data:
        print(ctime())
        speak(ctime())

    # External searches
    # # Text search with wikipedia and google
    if voice_data.lower() == 'search':
        search = record_audio(speak('What I need to Search'))
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('HERE IS WHAT I HAVE FOUND FOR ' + search.upper())
    
    else:
        # # Wikipedia
        WIKI_BASE_URL = 'https://en.wikipedia.org/wiki/Special:Search?search={}'

        search_url = WIKI_BASE_URL.format(quote_plus(voice_data))
        response = requests.get(search_url)
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')
        search_title = soup.find_all('h1', {'class': 'firstHeading'})

        # # Google Search
        if search_title[0].text.upper() == "SEARCH RESULTS":
            search = record_audio(speak('What I need to Search'))
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('HERE IS WHAT I HAVE FOUND FOR ' + search.upper())
        # # Wikipedia search
        else:
            search_response = soup.find_all('p')
            first_search_response = search_response[0].text
            # Need to be converted into audio message
            search_response_text = re.sub(
                "[\(\[].*?[\)\]]", "", first_search_response)
            print(search_title[0].text)
            print(search_response_text)

    # # Location search with Google Maps
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


time.sleep(1)
speak('POWER ON')
speak('HI, HOW CAN I HELP YOU')
while 1:
    voice_data = record_audio()  # text is the line which we speak
    print(voice_data)
    respond(voice_data)
