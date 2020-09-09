import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import requests
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

def respond(voice_data):
    speak(voice_data)
    print(voice_data)

def main():
    respond("Hey, what's up?")                        # greeting
    voice_data = hearing()

    if voice_data == "who are you" or voice_data == "what is your name" or voice_data == "what's your name":
        respond("I'm  Athena.")                       # gives introduction

    if voice_data == "what time is it" or voice_data == "what is the time" or voice_data == "tell me the time":
        local_time = time.asctime()
        local_time = local_time[11:19]
        time_words = f"{local_time[:2]} hours and {local_time[3:5]} minutes and {local_time[6:]} seconds."
        respond(time_words)                           # tells you time

    if "search google for" in voice_data:           # google search
        query = voice_data.split()
        query = query[3:]
        respond("Opening browser.")
        webbrowser.open("https://www.google.com/search?q=" + "%20".join(query))

    if "search wikipedia for" in voice_data:        # searches wikipedia
        voice_data = voice_data.split()
        results = wikipedia.search(voice_data[3:])
        respond(f"Here is what I found for {voice_data[3:]}.")
        for i in range(len(results)):
            print(f"{i+1}. {results[i]}")
        respond("What do you want to search in particular? Enter index of the result")
        choice = int(input("Enter index: "))
        print(wikipedia.summary(results[choice-1]) + "\n----")
        page_url = wikipedia.page(results[choice-1]).url
        print(f"Page url: {page_url}")
        respond("Would you like me to open the page?")
        choice_2 = input("Enter (y/n): ")
        if choice_2 == "y":
            webbrowser.open(page_url)
        else:
            respond("Ok!")
    
    if voice_data == "rock paper scissors":             # plays rock paper scissors
        speak("How many rounds you want to play?")
        rounds = int(input("How many rounds you want to play? "))
        computer, user = 0, 0
        for i in range(rounds):
            comp_turn = random.choice(["rock", "paper", "scissors"])
            print("Your turn!")
            user_turn = hearing()

            if comp_turn == "rock" and user_turn == "scissors":
                computer += 1
            elif comp_turn == "paper" and user_turn == "rock":
                computer += 1
            elif comp_turn == "scissors" and user_turn == "paper":
                computer += 1
            elif user_turn == "rock" and comp_turn == "scissors":
                user += 1
            elif user_turn == "paper" and comp_turn == "rock":
                user += 1
            elif user_turn == "scissors" and comp_turn == "paper":
                user += 1
            else:
                computer += 0
                user += 0
        
        if computer == user:
            respond("Draw!")
        elif computer > user:
            respond("You lose!")
        else:
            respond("You won!")
    
    if voice_data == "chuck norris":                # gets random chuck norris joke
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        respond(data["value"])
    
    if voice_data == "advice" or voice_data == "give me an advice":
        response = requests.get("https://api.adviceslip.com/advice")
        data = response.json()
        respond(data["slip"]["advice"])               # gives random advice
    
    if voice_data == "goodbye" or voice_data == "bye" or voice_data == "quit":
        respond("See ya later!")                      # quits the program
        exit()

main()
