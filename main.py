# import pyttsx3 for text to speech
import pyttsx3
# import pypiwin32 to use APIs [we dont have it for linux]

# import speechrecognition for umm.. speechrecognition
import speech_recognition as sr
#import pyaudio to use speakers
import pyaudio as pdo

import os
import datetime


# Initialize Text to Speech
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tts(text):
    return os.system("espeak  -s 155 -a 200 "+text+" " )

# Listen to user input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm Listening")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # speak('Recognizing')
        query = r.recognize_google(audio, language='en-CA')
        print(query)
        if (query == "what is the time"):
            m = datetime.datetime.now().strftime("%I %M %S")
            tts("' the time is"+str(int(m[0:2]))+" "+str(int(m[3:5]))+" : ' ")
        # print("User said: {}".format(query))
    except sr.UnknownValueError:
        print("I cannot hear you")
        speak("I cannot hear you")
    except sr.RequestError:
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query

listen()






