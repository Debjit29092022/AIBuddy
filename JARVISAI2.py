import pyttsx3
import Speech_Recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def say(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        say("Good Morning sir!")
    elif 12 <= hour < 18:
        say("Good Afternoon sir!")
    else:
        say("Good Evening sir!")
    say("Hello, I am Alpha . How may I help you?")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please repeat.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""


def process_command(query):
    if 'about' in query:
        say('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=1)
            say("According to Wikipedia")
            print(results)
            say(results)
        except wikipedia.exceptions.DisambiguationError as e:
            say("There are multiple options. Please specify.")
            print("Disambiguation Error:", e.options)
        except wikipedia.exceptions.PageError:
            say("Sorry, I couldn't find any information on that topic.")
            
    elif 'play in youtube' in query.lower():
        say('Searching in YouTube....')
        query = query.replace("play in youtube", "")
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)

    elif "song" in query:
        say("Opening Spotify")
        webbrowser.open("https://www.spotify.com")

    elif "whatsapp" in query:
        say("Opening Whatsapp")
        webbrowser.open("https://web.whatsapp.com/")

    elif "instagram" in query:
        say("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "facebook" in query:
        say("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "zomato" in query:
        say("Opening Zomato")
        webbrowser.open("https://www.zomato.com")

    elif "swiggy" in query:
        say("Opening Swiggy")
        webbrowser.open("https://www.swiggy.com")

    elif "uber" in query:
        say("Opening Uber")
        webbrowser.open("https://www.uber.com")

    elif "linkedin" in query:
        say("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "twitter" in query:
        say("Opening Twitter")
        webbrowser.open("https://www.twitter.com")

    elif "gpt" in query:
        say("Opening Chat GPT")
        webbrowser.open("https://chat.openai.com")

    elif "gemini" in query:
        say("Opening Gemini")
        webbrowser.open("https://gemini.google.com")

    elif "google" in query:
        say("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "telegram" in query:
        say("Opening Telegram")
        webbrowser.open("https://web.telegram.org")

    elif "the time" in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Sir, the time is {strtime}")

    elif "vs code" in query:
        path = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif "camera" in query:
        say("Opening Camera")
        open_camera()

    else:
        say("Sorry, I don't understand that command.")


def open_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    wish()
    while True:
        query = listen()
        process_command(query)
