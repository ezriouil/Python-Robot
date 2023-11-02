import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import os
from playsound import playsound

son=pyttsx3.init() #pyttsx3.init() /pour active le bebliothéque/
voices=son.getProperty("voices")#.getProperty("voices") /give me prpriéte of song de pc/
son.setProperty("voices",voices[0].id)#.setProperty("voices",...[0].id) /da3 propriéte song of pc/

def Speak(audio):#audio : "c'est comme paramétre"
    son.say(audio) #.say("...") / pour dire /
    son.runAndWait() #.runAndWait() / pour run /

def TakeCommands():
    command = sr.Recognizer() #.Recognizer() / pour listenne de order /
    with sr.Microphone() as mic : #.Microphone() / pour listenne de order par microphone /
        print("Please Say Your Command...")
        command.phrase_threshold = 0.5 #.phrase_threshold = ... / di9a dyal listeen /
        audio=command.listen(mic)#.listen(...) listeen des commands par ...
        try:#حاول
            print("Recording...")
            query=command.recognize_google(audio,language='an')#.recognize_google(...,,language='...') / pour cree les parolle de ... , la language de audio /
            print(f'You Said: {query}')
        except Exception as Error:
            return None
        return query.lower()
playsound("welc1.mp3")
time.sleep(1)
playsound("welc2.mp3")
while True:
    choix = TakeCommands()
    if 'hi' in choix :
        playsound("goodmorning.mp3")
    if 'please open vs' in choix :
        playsound("iopennow.mp3")
        os.startfile("C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code")
    if 'please open google' in choix :
        playsound("iopengoogle.mp3")
    if "post" in choix :
        link='https://www.youtube.com'
        webbrowser.Chrome.open_new(link)




    

