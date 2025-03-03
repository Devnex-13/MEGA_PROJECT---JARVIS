from urllib.request import Request
import speech_recognition as sr
import pyaudio
import setuptools
import webbrowser
import pyttsx3
import musicLib
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "2e2288b906d54fe1a668f9447a676d57"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiProcess(command):
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messeges=[
        {"role":"system","content":"You Are The Virtual Assistance like Alexa and google."},
        {"role":"user","content":"What is Coding"}
        ]
    )

    return completion.choices[0].messege.content

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

    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        # Search In GPT Hoe Fetch Titles of news from above link.
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
            
    else:
        output = aiProcess(c)
        speak(output)
                

if __name__=="__main__":
    speak("Hello, I am JARVIS. How can i help You?")

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