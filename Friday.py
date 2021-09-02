from gtts import gTTS
import subprocess as sub
import speech_recognition as sr
import random as ran
import datetime
from pydub import AudioSegment
from pydub.playback import play
import time
from skills.weather.weather import weatherapi
from skills.weather import weather
from skills.news_Headlines import news

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    filename = AudioSegment.from_mp3(filename)
    play(filename)

def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
            # Logs
            file = open("logs.txt", "a")
            file.writelines("User: "+said+"\n")
        except Exception as e:
            print("Exception "+str(e))

    return said.lower()


# Skills

# Current time
def clock():
    time = datetime.datetime.now()
    return speak(time.strftime("%I:%M %p"))

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    hours = int(hours)
    mins = int(mins)
    sec = int(sec)
    return hours, mins, sec;

# Possible ways of inputs
greetings = ["hello", "It\'s nice to meet you", "It is my pleasure to meet you", "hi", "What is new", "It\'s good to see you", "howdy", "hey", "yo", "yo whats up", "whats up", "hello dude"]

# Input_user
Name = ["how you are called", "tell me your name", "whas your name", "what your name", "what do they call you", "what\'s yours", "what is your name"]
# Output_python
python_Name = ["hi there, I am python", "hello, I am python. developed by Karthikeya.Thota", "I am python", "I am python, a personal assistant at Farmington High School"]

# Thanking
user_thanking = ["thank you", "thanks", "cool dude", "thanks bro", "you are the best", "thanks python"]
python_thanking = ["You are welcomed", "any time dude", "sure no problem", "it is my pleasure to serve you"]


# Favorite_Teacher
Fav_Tec = "My Favorite teachers is mr.jason canfield"
# Question
Fav_Tec_Question = ["Who is your favorite teacher", "do you have a Favorite teacher", "whos your fav teacher"]


# Who build you
god = "Mr. Karthikeya Thota, he gave me this life. He is my God. He gives me regular update, and I am thanking him so much that he give me this life to serve students and teachers like you."
# Who Build You_Input
god_input = ["Who build you", "who is your god", "who gave you birth", "who is the found", "who is the found of you", "who made you"]

# Time
time_input = ["What\'s the time", "time", "up-time", "up time", "what is the time"]

# Weather
Current_Weather = ["what is the weather right now","weather today","today weather", "current weather", "weather current", "how hot it is", "how cold it is", "climate", "what is the climate", "how hot it is outside", "how cold it is outside"]
Conditions = ["what will it be like outside", "what should I expect outside", "what should I expect to see", "how is it outside", "outside condition", "current status of weather", "any I should except", "condition", "what should I expect today"]
wind_mile = ["how fast is the wind", "wind speed", "whats is the wind speed today",  "speed of wind", "wind speeds", "winds speeds"]
wind_direction = ["direction of the wind", "wind direction", "which way is the wind comes", "direction wind", "direction of wind", "wind directions"]
rain = ["chance of rain", "percipitation", "rain", "will it rain", "any rain", "rain percentage"]
snow = ["chance of snow", "percipitation", "snow", "will it snow", "any snow", "snow percentage"]
sunraise = ["when is the sunset", "when does the sunraise", "sunraise", "sunset", "what time is the sunraise", "what time is the sunset"]
all_weather = ["weather updates", "weather update", "weather", "weather all", "get all the weather updates"]


# Stopwatch
stopwatch_start = ["start stopwatch", "start stop watch", "stopwatch start", "stop watch start", "star the timer"]
stopwatch_stop = ["end stopwatch", "end stop watch", "stopwatch end", "stop watch end", "stop stopwatch", "stop stop watch"]

# News
current_news = ["headlines", "news", "today's news", "news flash", "telecast", "current news", "news today", "news report", "news broadcast", "report news", "public news", "public press", "press reports", "headline"]

WAKE = "python"

while True:
    text = audio()
    if text.count(WAKE) > 0:
        speak("I am ready")
        text = audio()

        # Greeting
        if text in greetings:

            ran.shuffle(greetings)
            speak(greetings[0])

        # Name
        elif text in Name:
            ran.shuffle(python_Name)
            speak(python_Name[0])

        # Teacher
        elif text in Fav_Tec_Question:
            speak(Fav_Tec)

        # Who made you
        elif text in god_input:
            speak(god)


        # Current time
        elif text in time_input:
            clock()


        # stopwatch
        elif text in stopwatch_start:
            speak_text = "...Stopwatch has been started"
            speak(speak_text)
            start_time = time.time()

        elif text in stopwatch_stop:
            end_time = time.time()
            time_lapsed = end_time - start_time
            hours, mins, sec = time_convert(time_lapsed)
            speak("Timelapsed for "+str(hours)+" hours "+str(mins)+" minutes and "+str(sec)+" seconds")


        # weather
        elif text in Current_Weather:
            speak(weatherapi.current_weather())

        elif text in Conditions:
            speak(weatherapi.conditions())

        elif text in wind_mile:
            speak(weatherapi.wind_mile())

        elif text in wind_direction:

            speak(weatherapi.wind_direction())
            print(weatherapi.wind_direction())

        elif text in rain:
            speak(weatherapi.rain())

        elif text in snow:
            speak(weatherapi.snow())

        elif text in sunraise:
            speak(weatherapi.sunraise())

        elif text in all_weather:
            speak("ok getting all the weather updates")
            time.sleep(2)
            speak(weatherapi.current_weather())
            speak(weatherapi.conditions())
            speak(weatherapi.wind_mile())
            speak(weatherapi.wind_direction())
            speak(weatherapi.rain())
            speak(weatherapi.snow())
            speak(weatherapi.sunraise())

        # Thanking the user

        elif text in user_thanking:
            ran.shuffle(python_thanking)
            speak(python_thanking[2])

        # News

        elif text in current_news:
            paper = news.News.news()
            for i in paper:
                speak(i)
