import speech_recognition as sr
import pyaudio
import setuptools
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Hello, I am JARVIS. Your Personnel Assistance. How can i help You?")