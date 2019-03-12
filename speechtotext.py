audio = "harvard.wav"
name = "harvard.txt"

import speech_recognition as sr
import random

r = sr.Recognizer()

with sr.AudioFile(audio) as source:
    print("Audio Text Conversion in Progress")
    audio = r.record(source)
try:
    text = r.recognize_google(audio)
    print("Exporting Text File", name)
    textfile = open(name, 'w')
    textfile.write(text)
    textfile.close()
    print("File Generation Complete")

except Exception as e:
    print(e)

