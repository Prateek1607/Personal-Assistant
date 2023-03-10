# Virtual-Assistant
# The aim is to create a Virtual Assistant using Python that would interact with the user and answer their queries.

import os
import pyttsx3
import speech_recognition as sr

print('====================================================================================================================================================================================================')
print('                                                                         Virtual Assistant                                                                                                          ')
print('====================================================================================================================================================================================================')

engine = pyttsx3.init()
rate = engine.getProperty('rate')  # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)  # setting up new voice rate

# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

pyttsx3.speak("Hello Prateek")
print()
print("WELCOME TO MY INTELLIGENCE WORLD".center(125))
engine.runAndWait()
pyttsx3.speak("I am your virtual assistant and my name is Javris")
pyttsx3.speak("How can i help you...?")


while True:
    print()
    p = input("\t \t \t Hey user what you want to run :- ")

    if ("Hello" in p) or ("hi" in p) or ("hey" in p):
        pyttsx3.speak("Hello Prateek")
        pyttsx3.speak("How may i help you")

    elif ("tell" in p) or ("about" in p) or ("yourself" in p):
        pyttsx3.speak(
            "My name is Javris , I am your virtual assistant , I am very intelligent and I am always there to help you")

    elif ("date" in p):
        pyttsx3.speak("showing todays date")
        os.system("date")

    elif ("time" in p):
        pyttsx3.speak("showing current time")
        os.system("time")

    elif ("place" in p):
        pyttsx3.speak("showing current place")
        os.system("place")

    elif ("chrome" in p):
        pyttsx3.speak("opening chrome")
        os.system("start chrome")

    elif ("cloud" in p) or ("google cloud" in p):
        pyttsx3.speak("opening google cloud")
        os.system("start chrome cloud.google.com")

    elif ("gmail" in p):
        pyttsx3.speak("opening G mail")
        os.system("start chrome www.gmail.com")

    elif ("youtube" in p):
        pyttsx3.speak("opening youtube")
        os.system("start chrome www.youtube.com")

    elif ("twitter" in p):
        pyttsx3.speak("opening twitter")
        os.system("start chrome www.twitter.com")

    elif ("facebook" in p):
        pyttsx3.speak("opening facebook")
        os.system("start chrome www.facebook.com")

    elif ("linkedin" in p):
        pyttsx3.speak("opening linkedin")
        os.system("start chrome www.linkedin.com")

    elif ("amazon" in p):
        pyttsx3.speak("opening amazon")
        os.system("start chrome www.amazon.in")

    elif ("flipkart" in p):
        pyttsx3.speak("opening flipkart")
        os.system("start chrome www.flipkart.com")

    elif ("File Explorer" in p) or ("manager" in p):
        pyttsx3.speak("opening File Explorer")
        os.system("File Explorer")

    elif ("paint" in p):
        pyttsx3.speak("opening paint")
        os.system("start paint")

    elif ("notepad" in p) or ("editor" in p):
        pyttsx3.speak("opening notepad")
        os.system("notepad")

    elif ("MSword" in p) or ("word" in p):
        pyttsx3.speak("opening MS word")
        os.system("MS word")

    elif ("media" in p) or ("VLC" in p) or ("player" in p):
        pyttsx3.speak("opening VLC media Player")
        os.system(" start VLC media player")

    elif ("How" in p) or ("help" in p) or ("Javris" in p):
        pyttsx3.speak("i can help you in following ways")
        print()
        print("!! I can help you in following ways !!".center(126))
        pyttsx3.speak("such as window based commands")
        print()
        print(" * Window Based Commands".center(126))
        pyttsx3.speak("Entertainment")
        print()
        print(" * Entertainment".center(126))
        pyttsx3.speak("Public clouds")
        print()
        print(" * Public Clouds".center(126))
        pyttsx3.speak("emails")
        print()
        print(" * Emails".center(126))
        pyttsx3.speak("Social media")
        print()
        print(" * Social Media".center(126))
        pyttsx3.speak("Shopping")
        print()
        print(" * Shopping".center(126))
        pyttsx3.speak("Workflows")
        print()
        print(" * WorkFlows".center(126))
        pyttsx3.speak("Remote login")
        print()
        print(" * Remote Login".center(126))
        pyttsx3.speak("Virtualization")
        print()
        print(" * Virtualization".center(126))
        pyttsx3.speak("Steam Gaming")
        print()
        print(" * SteamEngine Gaming".center(126))
        pyttsx3.speak("Hey Prateek, What command would you like to give")

    elif ("exit" in p) or ("quit" in p) or ("bye" in p):
        pyttsx3.speak("see you soon,, have a nice day...!!! Thank You")
        break
    else:
        pyttsx3.speak("Sorry, Don't support")
        print("\t \t \t \t don't support")
