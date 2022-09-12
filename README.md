# virtual-voice-assistant
## Project description
This repository contains a python program which can be used to operate  some basic operations using voice commands. Platform used is AI (Artificial Intelligence).
This is a simple python program which takes voice commands as input, processes the query and performs tasks according to the query.

#### Important modules
### pyttsx3
* `pyttsx3` is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3
* #### Installation
   `pip install pyttsx3`
   
   If you recieve errors such as No module named `win32com`.client, No module named win32, or No module named win32api, you will need to additionally install `pypiwin32`.
* #### Usage :
    import pyttsx3 <br />
    engine = pyttsx3.init() <br />
    engine.say("I will speak this text") <br />
    engine.runAndWait()
### speech_recognition
A Library for performing speech recognition, with support for several engines and APIs, online and offline.
* #### Installation
   `pip install SpeechRecognition`
   
   
