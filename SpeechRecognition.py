import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import comtypes.client
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour > 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis, Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None

    return query

if __name__ == '__main__':
    wishMe()
    
    while True:
        query = takeCommand()
        
        if query is not None:
            query = query.lower()
        
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        
            elif 'open youtube' in query:
                webbrowser.open('youtube.com')

            elif 'open google' in query:
                webbrowser.open('google.com')
                
            elif 'open gmail' in query:
                webbrowser.open('gmail.com')
                
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
