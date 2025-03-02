import speech_recognition as sr
import pyaudio
import setuptools
import webbrowser
import pyttsx3
import musicLib

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube.")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening Linkedin.")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)

if __name__=="__main__":
    speak("Hello, I am JARVIS. Your Personnel Assistance. How can i help You?")

    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            command = r.recognize_google(audio)
            print(command)

            if(command.lower()=="jarvis"):
                speak("Yes")

                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    processCommand(command)
                
        except Exception as e:
            print("Error {e};")