import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time
import random
import wikipedia
import webbrowser

def hearing():
    r = sr.Recognizer()
    voice_data = " "
    with sr.Microphone() as source:
        print("Listening: ")
        audio = r.listen(source)
        
    try:
        voice_data = r.recognize_google(audio)      # converting speech to text
        print(voice_data)
    except Exception as e:
        print(e)
    return voice_data.lower()

def speak(voice_data):
    audio = gTTS(text = voice_data, lang = "en")    # converting text to audio
    random_num = random.randrange(9999999)
    audio_file = "audio" + str(random_num) + ".mp3" # saving audio file
    audio.save(audio_file)
    playsound.playsound(audio_file)                 # playing audio file
    os.remove(audio_file)                           # deleting audio file

def main():
    speak("Hey, what's up?")                        # greeting
    voice_data = hearing()

    if voice_data == "who are you" or voice_data == "what is your name" or voice_data == "what's your name":
        speak("I'm  Athena.")                       # gives introduction

    if voice_data == "what time is it" or voice_data == "what is the time" or voice_data == "tell me the time":
        local_time = time.asctime()
        local_time = local_time[11:19]
        time_words = f"{local_time[:2]} hours and {local_time[3:5]} minutes and {local_time[6:]} seconds."
        speak(time_words)                           # tells you time

    if "search wikipedia for" in voice_data:        # searches wikipedia
        voice_data = voice_data.split()
        results = wikipedia.search(voice_data[3:])
        speak("Here are the results I found.")
        for i in range(len(results)):
            print(f"{i+1}. {results[i]}")
        speak("What do you want to search in particular? Enter index of the result")
        choice = int(input("Enter index: "))
        print(wikipedia.summary(results[choice-1]) + "\n----")
        page_url = wikipedia.page(results[choice-1]).url
        print(f"Page url: {page_url}")
        speak("Would you like me to open the page?")
        choice_2 = input("Enter (y/n): ")
        if choice_2 == "y":
            webbrowser.open(page_url)
        else:
            speak("Ok!")

main()
