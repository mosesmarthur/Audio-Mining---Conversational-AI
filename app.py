#windows version
import speech_recognition as sr
import webbrowser as wb

path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    print('Done!')

try:
    text =r.recognize_google(audio, language="da-DK")
    print("Napster thinks, you said: \n" + text)

    f_text = 'https://www.google.com/search?q=' + text
    wb.get(path).open(f_text)

except Exception as e:
    print(e)
    
    
 #gerneral version
import speech_recognition as sr
import webbrowser as wb
import os


r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    os.system("Say Say something")
    print('Say Something!')
    audio = r.listen(source)
    print('Done!')

try:
    text = r.recognize_google(audio, language="EN")
    print('Google thinks you said:\n' + text)
    wb.get("chrome")
    wb.open_new('https://www.google.com/search?q=' + text)



except Exception as e:
    print(e)



