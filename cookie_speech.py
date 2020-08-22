import os
import speech_recognition
import playsound
from gtts import gTTS
import random
import wikipedia

def speak(text):
    tts = gTTS(text=text, lang="en", slow=False)
    r = random.randint(1,100000000)
    file_name ='audio-' + str(r) + '.mp3'
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
result = wikipedia.summary('Dell', sentences = [2])
print(result)
speak(result)
