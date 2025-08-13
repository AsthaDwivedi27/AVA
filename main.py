import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os  
import sys
import pywhatkit as kit
from hugchat import hugchat
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishMe() :
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning !")

    elif hour>=12 and hour<18 :
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    speak("I am AVA . Please tell me how may I help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print("User said:",query)

    except Exception as e :
        print(e) 
        print("Say that again please...")
        return "None"
    return query 

def chatBot(query) :
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response


if __name__ == "__main__":
    wishMe()
    
    while True:
    #if 1:
        query = takeCommand().lower() 

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'search youtube' in query:
            speak('searching Youtube')
            query = query.replace("search youtube","")
            webbrowser.open("youtube.com\\search = query")
            kit.playonyt(query)

        elif 'close youtube' in query: 
            os.system("taskkill /f /im msedge.exe")

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'search google' in query:
            speak('Searching please wait...')
            query = query.replace("search google","")
            webbrowser.open('google.com\\search = query')
            kit.search(query)
        
        elif 'close google' in query: 
            os.system("taskkill /f /im msedge.exe") 

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'close instagram' in query: 
            os.system("taskkill /f /im msedge.exe")

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'close stack overflow' in query: 
            os.system("taskkill /f /im msedge.exe")

        elif 'open amazon' in query:
            webbrowser.open('amazon.com')

        elif 'close amazon' in query: 
            os.system("taskkill /f /im msedge.exe")

        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

        elif 'close linkedin' in query: 
            os.system("taskkill /f /im msedge.exe")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\abhay\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play movie' in query:
            movie_dir = "C:\\Users\\abhay\\Desktop\\Rebel.Moon.Part.Two.The.Scargiver.2024.720p.WEB-DL.Hindi.English.Msubs.MoviesMod.org.mkv"     
            os.startfile(movie_dir)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'close vs code' in query:
            os.system("taskkill/f /im VS Code.exe")

        elif 'open c folder' in query:
            codePath1 = "D:\\C_Code"
            os.startfile(codePath1)

        elif 'open notepad' in query:
            codepath2 = "C:\\Windows\\notepad"
            os.startfile(codepath2) 

        elif 'close notepad' in query:
            os.system("taskkill/f /im notepad.exe")

        elif 'open task manager' in query:
            codepath3 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager"
            os.startfile(codepath3)

        elif 'open cmd' in query:
            codepath4 = "C:\\Users\\abhay\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            os.startfile(codepath4)

        elif 'close cmd' in query:
            os.system("taskkill/f /im cmd.exe")

        elif 'open word' in query:
            codepath5 ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
            os.startfile(codepath5)

        elif 'close word' in query:
            os.system("taskkill/f /im  winword.exe")

        elif 'open powerpoint' in query:
            codepath6 ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
            os.startfile(codepath6)

        elif 'close powerpoint' in query:
            os.system("taskkill/f /im powerpnt.exe")

        elif 'open excel' in query:
            codepath7 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
            os.startfile(codepath7)
        elif 'close excel' in query:
            os.system("taskkill/f /im excel.exe")

        elif "what is my ip address" in query: 
            speak("Checking") 
            try: 
                ipAdd = requests.get('https://api.ipify.org').text 
                print(ipAdd) 
                speak("your ip adress is") 
                speak(ipAdd) 
            except Exception as e: 
                speak("network is weak, please try again some time later") 

        elif "eva" in query or "ava" in query:
            chatBot(query)

        elif "go to sleep" in query: 
            speak(' alright then, I am switching off') 
            sys.exit()
