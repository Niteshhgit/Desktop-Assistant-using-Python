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
    
#this fuction to wish me by using time

def wish_me():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning. What can i do for you")
    elif hour>=12 and hour<18:
        speak("Good afternoon. What can i do for you")
    else:
        speak("Good evening. What can i do for you")
    speak("I am your personal Assistant.")

if __name__=="__main__":
    wish_me()
    while True:
        query=takeCommand().lower()
        print(query)

        if "wikipedia" in query: 
            speak("Searching wikipedia")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif "google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif "github" in query:
            speak("Opening Github")
            webbrowser.open("github.com")
        elif "ndtv" in query:
            speak("Opening ndtv")
            webbrowser.open("ndtv.com")
        elif "instagram" in query:
            speak("Opening Instagam")
            webbrowser.open("instagram.com")
        elif "weather" in query:
            speak("Opening weather")
            webbrowser.open("weather.com")
        elif 'see you later' in query:
            speak("im always here for you")
            exit()
