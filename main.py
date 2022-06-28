import pyttsx3 as p
import speech_recognition as sr
import wiki_automation
import youtube_automation

engine = p.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

listener= sr.Recognizer()
speak("Hello dear. How are you?")

with sr.Microphone() as source:
    listener.energy_threshold= 10000
    listener.adjust_for_ambient_noise(source, 1.2)
    print("Listining...")
    audio= listener.listen(source)
    try:
        command= listener.recognize_google(audio)
        print("You:\t"+ command)
    except:
        speak("Sorry Sir! I didn't get it.")

    if "what" and "about" and 'you' in command:
        speak("I am Excellent.")

    speak("How may I help you?")


with sr.Microphone() as source:
    listener.energy_threshold= 10000
    listener.adjust_for_ambient_noise(source, 1.2)
    print("Listining...")
    audio = listener.listen(source)
    text2 = listener.recognize_google(audio)
    print("You:\t" + text2)

    if "information" in text2:
        speak("You want me to search what topic?")
        with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            print("Listining...")
            audio =listener.listen(source)
            topic =listener.recognize_google(audio)
            speak("Searching {} on wikipedia".format(topic))
            assist = wiki_automation.wiki()
            assist.get_info(topic)

    elif "youtube" or "play music" or "song" or "play video" in text2:
        speak("Which video u want me to play")
        with sr.Microphone() as source:
            listener.energy_threshold = 1000
            listener.adjust_for_ambient_noise(source, 1.2)
            print("Listining...")
            audio = listener.listen(source)
            video = listener.recognize_google(audio)
            speak("Playing {} on youtube".format(video))
            assist = youtube_automation.YouTube()
            assist.play_video(video)


