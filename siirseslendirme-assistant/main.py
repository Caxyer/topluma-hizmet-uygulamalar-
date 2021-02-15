import time
from datetime import datetime
import webbrowser
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import random
import os
import requests
from bs4 import BeautifulSoup



r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ''

        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            print("Üzgünüm Anlayamadım")
            speak("Üzgünüm Anlayamadım")
        except sr.RequestError:
            print("Bir sorun var sistem çalışmıyor.")
            speak("Bir sorun var sistem çalışmıyor.")
        return voice

def response(voice):
    if "nasılsın" in voice:
        print("İyiyim Sen nasılsın")
        speak("İyiyim sen nasılsın")
    if "saat kaç" in voice:
        print(datetime.now().strftime("%H:%M:%S"))
        speak(datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice:
        search = record("Ne aramak istiyorsun")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        print(search + " için bulduklarım")
        speak(search + " için bulduklarım")
    if "baybay" in voice:
        print("Görüşürüz")
        speak("Görüşürüz")
        exit()
    if "dinle" in voice:
        siirler = open("siirler\\siir3"
                       ".txt","r",encoding="utf-8")
        siiroku = siirler.read()
        print(siiroku)
        speak(siiroku)



def speak(string):
    tts = gTTS(string, lang="tr")
    rast = random.randint(1,10000)
    file = "ses-"+str(rast)+ '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

"""siirler = open("siirler\\siir1.txt","r",encoding="utf-8")
siiroku = siirler.read()
speak(siiroku)"""

"""dosya = open("siirler")
file_list = dosya.read()
rnd = random.choice(file_list)
print(rnd)"""


print("Nasıl Yardımcı olabilirim?")
speak("Nasıl Yardımcı olabilirim?")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)


url2 = "http://www.siirakademisi.com/index.php?/site/siir_liste"
req = requests.get(url2)
kaynak = BeautifulSoup(req.content, "lxml")

