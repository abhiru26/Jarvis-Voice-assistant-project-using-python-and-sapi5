import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
# print(voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning')

    elif hour >= 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('good evening!')
    speak('hi i am jarvis. what is the plan for today sir ?')


def takeComand():
    # microphone input and string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        

    except Exception as e:
        #print(e)

        print('say that again please...')
        return "None"
    return query


if __name__ == "__main__":

    wishMe()
    
    #logic

    while True:
        query =  takeComand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
         
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'endgame' in query:
            movie_dir = 'G:\Avengers.Endgame.2019.720p.HDRip.999MB.x264-GalaxyRG[TGx]'
            movies = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir, movies[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,  the time is {strTime}")
        elif 'how ' in query:
            speak('taking some mango shake sir, and you ???')
        
        elif 'know' in query:
            speak('no sir, can you introduce me to her ?')
        
        elif 'can' in query:
            speak('thank tou sir, what is her name ?')
        elif 'name' in query:
            speak('oh that is very nice name somdutta')
        elif 'actually she ' in query:
            speak('ummm she is becoming mota day by day')
        elif 'tell' in query:
            speak('hey motu please eat lesser')
        elif 'ok' in query:
            speak('good night to you sir, bye')
        
            





    
