import speech_recognition as sr
import pyttsx3
from googletrans import Translator, constants
r = sr.Recognizer()
 #init the Google API translator
translator = Translator()
keyWord = 'cafea '
engine=pyttsx3.init()
with sr.Microphone() as source:
    print('Please start speaking..\n')
    while True: 
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language='ro-RO') #for Romanian)
            if keyWord.lower() in text.lower():
                print('Keyword detected in the speech.')
                engine.say(text=keyWord)
                engine.runAndWait()
                 # specify source language
                translation = translator.translate(keyWord, src="ro")
                print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})") 
        except Exception as e:
            print('Please speak again.')