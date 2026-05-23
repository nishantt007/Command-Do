import pyttsx3                      # library for text to speech conversion
import speech_recognition as sr     # library for speech recognition
import datetime
import wikipedia
import webbrowser                   # webbrowser module provides a high-level interface to allow displaying web-based documents to users
import os
import smtplib                      # to use less secure apps, we have to allow access to less secure apps in our google account settings, otherwise it will throw error while sending email using this code
# smtplib library defines an SMTP client session object for sending emails using the Simple Mail Transfer Protocol. Use it to send emails programmatically through an SMTP server, with support for authentication and secure connections

# credentials for email, stored in .env file for security reasons
from dotenv import load_dotenv
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

engine = pyttsx3.init('sapi5')              # sapi5 model used for converting text to speech
voices = engine.getProperty('voices')       # to retrieve the current value of various speech settings
print(voices[0].id)
engine.setProperty('voice', voices[0].id)   # 0 : Male voice, 1 : Female voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 4 and hour <= 12:
        speak("Good Morning!")
    elif hour > 12 and hour <= 17:
        speak("Good Afternoon!")
    elif hour > 17 and hour <= 20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am Jarvis. Please tell me how may I help you?")

'''this function takes microphone input from the user and returns it as a string. Returns "None" if there is error.'''
def takeCommand():
    r = sr.Recognizer()                # helps to detect audio
    with sr.Microphone() as source:    # using microphone as the source of input
        print("Listening...")
        r.pause_threshold = 1          # self.pause_threshold is seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 250       # minimum audio energy to consider for recording. Keep it high if there are background noises
        audio = r.listen(source)

    try:
        print("Recognizing...")         
        query = r.recognize_google(audio, language='en-in') # recognize_google/google_cloud can be used to recognize the user audio file and convert to string
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    if 1:
        query = takeCommand().lower()   # converts input audio converted string's uppercase letters to lowercase

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")          # query.replace replaces 'wikipedia' spoken word by blank/our query results
            results = wikipedia.summary(query, sentences=2) # sentence determines how many lines it will read from wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\username\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to nishant' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = os.getenv("EMAIL_ADDRESS")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I could not send that email.")
