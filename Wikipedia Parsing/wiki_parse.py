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
# os.system('start test_1.mp3')


# Parsing through Wikipedia Phaase-2

WIKI_BASE_URL = 'https://en.wikipedia.org/wiki/Special:Search?search={}'

search_url = WIKI_BASE_URL.format(quote_plus(text))
response = requests.get(search_url)
data = response.text
soup = BeautifulSoup(data, features='html.parser')
search_title = soup.find_all('h1', {'class': 'firstHeading'})

if search_title[0].text.upper() == "SEARCH RESULTS":
    print("need to work on it")
else:
    search_response = soup.find_all('p')
    first_search_response = search_response[0].text
    search_response_text = re.sub("[\(\[].*?[\)\]]", "", first_search_response) #Need to be converted into audio message
    print(search_title[0].text)
    print(search_response_text)

