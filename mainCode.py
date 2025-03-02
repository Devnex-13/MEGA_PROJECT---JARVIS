import speech_recognition as sr
import pyaudio
import setuptools
import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

          
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
                
        except Exception as e:
            print("Error {e};")