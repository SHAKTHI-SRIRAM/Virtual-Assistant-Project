import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
import re
# Packages from test 4
import speech_recognition as sr
from gtts import gTTS
import os


# Voice recognization Phase-1
r = sr.Recognizer()
print('Say Something')
with sr.Microphone() as source:
    voice_data = r.record(source, duration=5)

    try:
        print("Recognizing...")
        text = r.recognize_google(voice_data)
        print(text)
    except sr.UnknownValueError:
        print('i cant get you, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech recognition error' + e)
    print('')
speech = gTTS(text)
speech.save('test_1.mp3')

YOUTUBE_BASE_URL = 'https://www.youtube.com/results?search_query={}'

search_url = YOUTUBE_BASE_URL.format(quote_plus(text))
response = requests.get(search_url)
data = response.text
print(data)
soup = BeautifulSoup(data, features='html.parser')
search_result= soup.find('div', {'id': 'dismissable'})
print(search_result)

