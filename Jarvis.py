import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


#print("Initializing Jarvis")

engine=pyttsx3.init('sapi5')


#speak func will pronounce

def speak(text):
    engine.say(text)
    engine.runAndWait()

#will greet me

def wishMe():
    hour=int(datetime.datetime.now().hour)


    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon boss")
    else:
        speak("Good evening boss")

    speak("I..am Jarvis and How may I help you?")

#this will take command


def take_command():

    if count>0:
        speak("......Do you need anything else boss?")

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("Say that again please!")
        query=''
    return  query



#main program starts here

if __name__== "__main__":

    speak("Initializing Jarvis")
    wishMe()
    count=0
    query=take_command()



    while("exit" not in query.lower()):

        if query=='':
            count=0
            query=take_command()



        elif 'wikipedia' in query.lower():

            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
            count += 1
            query = take_command()


        elif 'open youtube' in query.lower():

            url= 'https://youtube.com/'
            webbrowser.open(url)
            count += 1
            query = take_command()

        elif 'open google' in query.lower():

            url= 'https://google.com/'
            webbrowser.open(url)
            count += 1
            query = take_command()


        elif 'play music' in query.lower():

            songs_dir="C:\\Users\\Mohit aksha\\Downloads"
            songs=os.listdir(songs_dir)

            os.startfile(os.path.join(songs_dir,songs[1]))
            count += 1
            query = take_command()


        elif 'the time' in query.lower():

            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
            count+=1
            query = take_command()
        else:

            speak("command undefined")
            count=0
            query=take_command()
            count+=1

    speak("Good bye boss!...Have a nice day")
    exit()


