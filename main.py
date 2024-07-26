import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#taking voice from my system
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[1].id)

engine.setProperty('rate',145)
engine.setProperty('volume',0.55)
#speak function

def speak(text):
    """This function takes text returns voices
    Args:
        text(_type_):String
        """

    engine.say(text)
    engine.runAndWait()

#speak("Hello I am your personal assistant,How can i help you")

#speech recognition function
def takeCommand():
    """This function will recognize and return text
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1  #stop for 1 millisecond
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said:{query}\n")

        except Exception as e:
            print("Can you say that again...")
            return "None"
        return query
    
text=takeCommand() 
speak(text)  
