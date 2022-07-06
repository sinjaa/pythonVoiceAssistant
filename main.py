import pyttsx3 as p
import randfacts
import speech_recognition as sr
import wiki_automation
import youtube_automation
import datetime
from time import sleep
import pyjokes
import webbrowser

engine = p.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
listener = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def welcome():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak("Rise and shine! Have a great day my friend!")

    elif time >= 12 and time < 18:
        speak("Good Afternoon !I wish your Afternoon to be beautiful, buddy.")

    else:
        speak("Good Evening!I'm wishing you a lovely evening.")

    speak("I am here to help.")


def take_command():
    with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print("Listining...")
            audio= listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        print("You: " + command)

    except:
        speak("I can't hear you right now.")

    return (command)

welcome()

def runMe():
    speak("What can I do for you?")
    query= take_command().lower()

    if "information" in query or "wikipedia" in query:
        speak("You want me to search what topic?")
        topic = take_command()
        speak("Searching about {} on wikipedia".format(topic))
        assist = wiki_automation.wiki()
        assist.get_info(topic)

    elif "play song" in query or "play video" in query:
        speak("Which video u want me to play")
        video = take_command()
        speak("Playing {} on youtube".format(video))
        assist = youtube_automation.YTube()
        assist.play_video(video)

    elif "interesting fact" in query:
        x=randfacts.get_fact()
        print("Fact:"+x)
        speak("Did you know that: "+x)

    elif "joke" and "jokes" in query:
        speak(pyjokes.get_joke())

    elif 'how are you' in query:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        speak("I am having a great time with you, Thanks")

        # search google
    elif "search" in query or "google" in query:
        speak("What do you want me to search for?")
        keyword = take_command()
        # if "keyword" is not empty
        if keyword != '':
            url = "https://google.com/search?q=" + keyword
            speak("Here are the search results for " + keyword)
            webbrowser.open(url)
            sleep(3)

    elif "date" in query:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today is {} :".format(date))
        print(date)

    elif "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is {} now".format(time))
        print(time)

    elif "quit" in query or "bye" in query or "stop" in query:
        speak("Ok, I'm' going to take a nap. See you soon..")
        print("Ok, I'm' going to take a nap. See you soon..")
        exit()

    else:
        speak("Sorry! Your command is not clear to me. Can you simplify it please?")



while True:
    runMe()



















