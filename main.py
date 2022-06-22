import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r= sr.Recognizer()
speak("Hello dear. How are you?")

with sr.Microphone() as source:
    r.energy_threshold= 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listining...")
    audio= r.listen(source)
    text= r.recognize_google(audio)
    print("You:\t"+ text)
    if "what" and "about" and 'you' in text:
        speak("Excellent Boss.")

    speak("How may I help?")