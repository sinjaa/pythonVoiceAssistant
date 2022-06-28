import pyttsx3 as p
import speech_recognition as sr
import wiki_automation
import youtube_automation
import datetime
import pyjokes

engine = p.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Good morning. How may I help you?")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print("Listining...")
            audio= listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        print("You: " + command)

    except:
        speak("Warning:  Unable to reach u")

    return (command)

def runMe():
    query= take_command()
    if "time" in query:
        time= datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is {} now".format(time))
        print(time)

    elif "information" in query:
        speak("You want me to search what topic?")
        topic = take_command()
        speak("Searching {} on wikipedia".format(topic))
        assist = wiki_automation.wiki()
        assist.get_info(topic)

    elif "youtube" or "play music" or "song" or "play video" in query:
        speak("Which video u want me to play")
        video = take_command()
        speak("Playing {} on youtube".format(video))
        assist = youtube_automation.YouTube()
        assist.play_video(video)

    elif "joke" or "jokes" in query:
        speak(pyjokes.get_joke())
    else:
        print("Sorry? Can you tell it again?")


while 1:
    runMe()



















