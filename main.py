import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import random

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
    pass

main()