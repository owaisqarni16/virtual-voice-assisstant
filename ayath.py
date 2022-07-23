# Author : shaikowais457@gmail.com
# Description : This script creates a virtual personal voice assisstant through which a user can perform basic operations by giving voicce commands.
# Note : user should have an active internet connection in order to make user's voice command recognizable.
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import datetime
import wikipedia
import socket
from requests_html import HTMLSession
#I named this virtual voice assisstant Ayat.
#I have defined different functions for particular operations.
engine=pyttsx3.init()
engine.setProperty('rate',150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# This function is to get ip address of your system.
def getip():
    hostname=socket.gethostname()
    hostaddress=socket.gethostbyname(hostname)
    return hostaddress
# This function is to convert text to speech.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# This function is to analyze or recognize the voice,
# Recognition is done by google engine, so we need to have an active internet connection.

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # r.pause_threshold=1
        r.energy_threshold=250
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in',)
            print('you said -> {}\n'.format(query))
        except Exception as e:
            print("sorry could not recognize")

            return "None"
        return query
# This function is to wish the user.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hi Good Morning!")
        print("Ayath ->Hi Good Morning!")
    elif hour>=12 and hour<16:
        speak("hi Good Afternoon!")
        print("Ayath ->Hi Good Afterrnoon!")
    elif hour>=16 and hour<19:
        speak("Hi Good Evening!")
        print("Ayath ->Hi Good Evening!")
    else:
        pass
    print("Ayath ->i am Ayath\nhow can i help you ?")
    speak('i am Ayath, how can i help you ?')
# This function is to get the weather information and name of the place is to be typed manually.
def weather():
    s=HTMLSession()
    query=input('Enter name of the place : ')
    url=f'https://www.google.com/search?q=weather+{query}'
    r=s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})
    temp=r.html.find('span#wob_tm',first=True).text
    unit=r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
    desc=r.html.find('div.VQF4g',first=True).find('span#wob_dc',first=True).text
    print('Ayath -> The climate is ',desc,'and the temperature is',temp,unit)
    speak('The climate is ')
    speak(desc)
    speak('and the temperature is')
    speak(temp)
    speak('degree celcius')


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print("Ayath -> ",results)
            speak(results)
        elif 'about' in query:
            speak('Searching Wikipedia...')
            query = query.replace("about", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print("Ayath -> ",results)
            speak(results)
        elif 'ip' in query:
            ip=getip()
            print('Ayath -> ',ip)
          
            speak(ip)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f" Sir, the time is {strTime}")
            speak(f" Sir, the time is {strTime}")
        elif 'bye' in query:
            print("Ayath -> Bye, see you soon..!")
            speak('Bye, see you soon...!')
            exit()
        elif 'how are you' in query:
            print("Ayath -> I am Fine")
            speak("i am fine")
        elif 'what is your name' in query:
            print("Ayath -> My name is Ayath!")
            speak("My name is Ayath!")
        elif 'where are you' in query:
            print("Ayath -> I am in your device!")
            speak('I am in your device!')
        elif 'weather' in query:
            weather()
        
        elif 'hi' in query:
            print('Ayath -> Hi!!')
            speak('Hi!!')
        elif 'hai' in query:
            print('Ayath -> Hai!!')
            speak('Hai!!')
        elif 'hello' in query:
            print('Ayath -> Hello!')
            speak('Hello!')
        elif 'thank you' in query:
            print('Ayath -> Your welcome!')
            speak('your welcome!')
        elif 'thank u' in query:
            print('Ayath -> Your welcome!')
            speak('your welcome!')
        elif 'thankyou' in query:
            print('Ayath -> Your welcome!')
            speak('your welcome!')
        elif 'bye' in query:
            print('Ayath ->Bye see you soon...')
            speak('Bye see you soon...')
            exit()
    
        else:
            pass

    exit()
