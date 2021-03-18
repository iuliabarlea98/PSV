import speech_recognition as sr
import pyaudio
import pyttsx3
from googletrans import Translator, constants
from playsound import playsound

 #init the Google API translator
translator = Translator()
engine=pyttsx3.init()
yt=sr.AudioFile('Elon2.wav')
r = sr.Recognizer()
keyWord = 'technologies'
with yt as source:
   print('Please start speaking..\n')
   #playsound('Elon2.wav')
   while True: 
        audio = r.record(source)
        try:
            text = r.recognize_google(audio,language='en') 
            engine.say(text=keyWord)
           
            # specify source language
            translation = translator.translate(keyWord, src="ro")
            print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
            if keyWord.lower() in text.lower():
                 print('Keyword detected in the speech.')
                 engine.runAndWait()
                       
        except Exception as e:
            print('Please speak again.')
            