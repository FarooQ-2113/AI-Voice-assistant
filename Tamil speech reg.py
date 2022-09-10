import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Say Something in Tamil and pause, no need to press any key")
    audio = r.listen (source)
    print ("Got you")
try:
    WhatUSpoke = r.recognize_google (audio, language="ta-IN")
    print ("What you spoke (Google):", WhatUSpoke)
except:
    pass