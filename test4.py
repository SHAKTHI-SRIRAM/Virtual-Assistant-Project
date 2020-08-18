import speech_recognition as sr
from gtts import gTTS
import os
r = sr.Recognizer()
print('Say Something')
with sr.Microphone() as source:
    voice_data = r.record(source, duration = 5)

    try:
        print("Recognizing...")
        text = r.recognize_google(voice_data)
        print(text)
    except sr.UnknownValueError:
        print('i cant get you, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech recognition error'+ e)
    print ('')
speech = gTTS(text)
speech.save('test_1.mp3')
os.system('start test_1.mp3')
