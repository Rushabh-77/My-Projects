# don't listen solve the problem (616)
# any integer can be used in taking command during 1 and 2
from __future__ import print_function
from twilio.rest import Client

import ctypes
import datetime
import getpass
import json
import os
import os.path
import pickle
import platform
import random
import smtplib
import time
import webbrowser
import pyjokes
import pytemperature
import pyttsx3
import pytz
import requests
import psutil
import speech_recognition as sr
import wikipedia
import turtle
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
# import winshell
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from urllib.request import urlopen
from mysql.connector import MySQLConnection
from termcolor import colored
from translate import Translator
from twilio.rest import Client


def virtualAssistant():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

    # def credAccess():
    # with open("userCred.txt", 'rt') as fin:
    # creds = fin.readlines()
    # username = creds[1]
    # USERNAME = username[0:len(username) - 1]
    # email_id = creds[3]
    # USER_EMAIL_ID = email_id[0:len(email_id) - 1]
    # password = creds[5]
    # USER_EMAIL_PASS = password[0:len(password) - 1]
    # sql = creds[7]
    # USER_SQL_PASS = sql[0:len(sql) - 1]
    # return USERNAME, USER_EMAIL_ID, USER_EMAIL_PASS, USER_SQL_PASS

    def speak(text):
        engine = pyttsx3.init("sapi5")  # object creation

        """ RATE"""
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        engine.setProperty('rate', 122)  # setting up new voice rate

        """VOLUME"""
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

        """VOICE"""
        voices = engine.getProperty('voices')  # getting details of current voice
        # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

        engine.say(text)
        engine.runAndWait()

    try:
        recognitionMode = int(input('''By which mode would you like to give commands : 
        1 - Voice Mode
        2 - Script Mode \n'''))
    except:
        print("sorry you entered wrong value")

    def take_command():
        global query
        if recognitionMode == 1:
            # It takes microphone input from the user and returns string output
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
            except Exception:
                print("Say that again please...")
                return "None"

        elif recognitionMode == 2:
            try:
                query = input('Enter your Command : ')
            except Exception as error:
                print(error)
        return query.lower()

    def send_sms(number, message):
        url = 'https://www.fast2sms.com/dev/bulk'
        params = {
            'authorization': 'R4UilqdkJNw1PKHu2j3fb0QsgEx7pWMYO9BItXnGvc5Cr8zoDAj2bBqMs4n9lLuNXaW85wEPhYJdUiQo',
            'sender_id': 'FSTSMS',
            'message':str(input("Type a message : ")) ,
            'language': 'english',
            'route': 'p',
            'numbers': number

        }
        response = requests.get(url, params=params)
        dic = response.json()
        print(dic)

    # def authenticate_google():
    # """Shows basic usage of the Google Calendar API.Prints the start and name of the next 10 events on the user's calendar."""
    # credits = None
    # if os.path.exists('token.pickle'):
    # with open('token.pickle', 'rb') as token:
    # credits = pickle.load(token)
    # if not credits or not credits.valid:
    # if credits and credits.expired and credits.refresh_token:
    # credits.refresh(Request())
    # else:
    # flow = InstalledAppFlow.from_client_secrets_file(
    # 'credentials.json', SCOPES)
    # credits = flow.run_local_server(port=0)
    # with open('token.pickle', 'wb') as token:
    # pickle.dump(credits, token)
    # service = build('calendar', 'v3', credentials=credits)
    # return service

    def get_events(day, service):
        # Call the Calendar API
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        date = date.astimezone(utc)
        end_date = end_date.astimezone(utc)
        events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(),
                                              timeMax=end_date.isoformat(),
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            speak('No upcoming events found.')
        else:
            speak(f"You have {len(events)} events on this day.")
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                start_time = str(start.split("T")[1].split("-")[0])
                if int(start_time.split(":")[0]) < 12:
                    start_time = start_time + "am"
                else:
                    start_time = str(int(start_time.split(":")[0]) - 12) + start_time.split(":")[1]
                    start_time = start_time + "pm"
                speak(event["summary"] + " at " + start_time)

    def get_date(text):
        text = text.lower()
        today = datetime.date.today()
        if text.count("today") > 0:
            return today
        day = -1
        day_of_week = -1
        month = -1
        year = today.year

        for word in text.split():
            if word in MONTHS:
                month = MONTHS.index(word) + 1
            elif word in DAYS:
                day_of_week = DAYS.index(word)
            elif word.isdigit():
                day = int(word)
            else:
                for ext in DAY_EXTENTIONS:
                    found = word.find(ext)
                    if found > 0:
                        try:
                            day = int(word[:found])
                        except:
                            pass

        # THE NEW PART STARTS HERE
        if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
            year = year + 1

        # This is slightly different from the video but the correct version
        if month == -1 and day != -1:  # if we didn't find a month, but we have a day
            if day < today.day:
                month = today.month + 1
            else:
                month = today.month

        # if we only found a dta of the week
        if month == -1 and day == -1 and day_of_week != -1:
            current_day_of_week = today.weekday()
            dif = day_of_week - current_day_of_week

            if dif < 0:
                dif += 7
                if text.count("next") >= 1:
                    dif += 7

            return today + datetime.timedelta(dif)

        if day != -1:  # FIXED FROM VIDEO
            return datetime.date(month=month, day=day, year=year)

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('rushabhmehta777@gmail.com', 'you know that')
        subject = "Contact book data"
        server.sendmail('computerassist.jks@gmail.com', to, content, subject)
        server.close()

    def note(text):
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)
        osCommandString = f"notepad.exe {file_name}"
        os.system(osCommandString)

    def TimeConversion(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:d}:{minutes:02d}:{seconds:02d}"

    def greet(name):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            speak("Good Morning!" + str(name))
        elif 12 <= hour < 16:
            speak("Good Afternoon!" + str(name))
        else:
            speak("Good Evening!" + str(name))

    def history(text):
        date_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        f = open("Hello.txt", "a")
        f.write(f"{date_time} : {text}\n\n")

    def contactBook(USER_SQL_PASS):
        global emailID
        mydb = MySQLConnection(host="localhost", user="root", password=USER_SQL_PASS, database="contact_book")
        mycursor = mydb.cursor()
        name1 = str(input("Enter the name : "))
        mycursor.execute("SELECT * FROM contact_table")
        myresult = mycursor.fetchall()
        for x in myresult:
            if name1 == x[0]:
                emailID = x[1]
                break
        else:
            print("Record not found")
            insertChoice = input("Would you like to add contact ? ")
            if insertChoice.lower().startswith("y"):
                mydb1 = MySQLConnection(host="localhost", user="root", password="computer", database="contact_book")
                mycursor1 = mydb1.cursor()
                mail = str(input("Enter the e-mail ID of the new contact : "))
                sql = "INSERT INTO contact_table(name, email_id) VALUES(%s,%s)"
                val = (name1, mail)
                mycursor1.execute(sql, val)
                mydb1.commit()
                print(mycursor1.rowcount, "record inserted.")

            mydb = MySQLConnection(host="localhost", user="root", password=USER_SQL_PASS, database="contact_book")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM contact_table")
            myresult = mycursor.fetchall()
            for x in myresult:
                if name1 == x[0]:
                    emailID = x[1]
                    break
        return emailID

    if __name__ == "__main__":

        # USERNAME, USER_EMAIL_ID, USER_EMAIL_PASS, USER_SQL_PASS = credAccess()
        # print(USERNAME, USER_EMAIL_ID, USER_EMAIL_PASS, USER_SQL_PASS)
        name = getpass.getuser()
        greet(name)
        initTime = datetime.datetime.now()
        WAKE = "rushi"
        assname = WAKE
        # SERVICE = authenticate_google()
        print("Starting....")
        speak("I am ready")

        while True:
            text = take_command()
            if text.count(WAKE) > 0:
                text = text.replace(WAKE, "")
                history(text)
                CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
                for phrase in CALENDAR_STRS:
                    if phrase in text:
                        date = get_date(text)
                        if date:
                            get_events(date, SERVICE)
                        else:
                            speak("I don't understand")

                NOTE_STRS = ["make a note", "write this down", "remember this"]
                for phrase in NOTE_STRS:
                    if phrase in text:
                        speak("What would you like me to write down?")
                        note_text = take_command()
                        note(note_text)
                        speak("I've made a note of that.")

                if 'wikipedia' in text:
                    try:
                        speak('Searching Wikipedia...')
                        text = text.replace("wikipedia", "")
                        results = wikipedia.summary(text, sentences=1)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    except Exception as e:
                        print(e)

                elif 'open youtube' in text:
                    speak("Here you go to Youtube")
                    webbrowser.open_new("https://www.youtube.com/")



                elif 'open classroom' in text:
                    text = str(input("Enter the name of the class: "))
                    if text == "python":
                        speak("Here is your python  class")
                        webbrowser.open_new("https://classroom.google.com/u/3/c/MTUyNjI2NjQ4MDg5")

                    elif text =="software engineering":
                        speak("Here is your software engineering class")
                        webbrowser.open_new("https://classroom.google.com/u/3/c/MTUzNzQ2MDU5NDE2")

                    elif text == "computer network":
                        speak("Here is your computer network class")
                        webbrowser.open_new("https://classroom.google.com/u/3/c/MTE3NTUzMTY2NTMy")


                elif 'open stackoverflow' in text:
                    speak("Here you go to Stack Over flow, Happy coding")
                    webbrowser.open_new("https://www.stackoverflow.com/")

                elif 'open calculator' in text or 'open calc' in text:
                    os.system("calc.exe")

                elif 'time' in text:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}")

                elif 'email' in text:
                    try:
                        speak("What should I say?")
                        content = take_command()
                        speak("whom should i send")
                        try:
                            to = contactBook(USER_SQL_PASS)
                            sendEmail(to, content)
                            speak("Your Email has been sent !")
                        except:
                            to = take_command()
                            sendEmail(to, content)
                            speak("Your Email has been sent !")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this email")


                elif 'open notepad' in text or 'notepad' in text:
                    os.system("Notepad.exe")


                elif 'clear screen' in text:
                    os.system('cls')

                elif 'how are you' in text:
                    speak("I am fine, Thank you")
                    speak("How are you")
                    text = take_command()
                    if 'i am fine' in text or "good" in text:
                        speak("It's good to know that your fine")

                elif "change name" in text:
                    speak("What would you like to call me, Sir ")
                    WAKE = take_command()
                    speak("Thanks for naming me")

                elif "what's your name" in text or "what is your name" in text:
                    speak("My friends call me")
                    speak(assname)
                    print("My friends call me", assname)

                elif "who made you" in text or "who created you" in text:
                    speak("I have been created by Rushi.")

                elif 'favourite song' in text:
                    speak(
                        "I don\'t have any favourite song but my creators have a common favourite song So, you can consider it as my favourite song also")
                    try:
                        os.system("start udd_gaye.mpeg")
                    except:
                        webbrowser.open("https://play.google.com/music/listen?u=0#/sr/udd gaye")

                elif "flip a coin" in text:
                    num = random.randint(0, 1)
                    print("Flipping your coin...")
                    if num == 1:
                        print("Heads: Front Face\n")
                    else:
                        print("Tails: Back Face\n")

                elif 'joke' in text:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)


                elif 'details of number' in text:
                    a = input("Enter a number:")
                    ch_number = phonenumbers.parse(a, "CH")
                    print(geocoder.description_for_number(ch_number, "de"))
                    ro_number = phonenumbers.parse(a, "RO")
                    print(carrier.name_for_number(ro_number, "en"))



                elif 'call' in text:
                    account_sid = 'ACeb2360f987b7b0b866805e4cd073cded'
                    auth_token = 'ee459d2f4d92b10da2c6ecb9572a25da'
                    client = Client(account_sid, auth_token)

                    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=int(input("Enter a number : ")),
                        from_=int(input("Enter a number: "))
                    )

                    print(call.sid)

                elif 'imposter' in text:
                    try :
                        BODY_COLOR = 'red'
                        BODY_SHADOW = ''
                        GLASS_COLOR = 'skyblue'
                        GLASS_SHADOW = ''

                        s = turtle.getscreen()
                        t = turtle.Turtle()

                        def body():
                            t.pensize(20)
                            t.speed(10)
                            t.fillcolor(BODY_COLOR)
                            t.begin_fill()

                            # starting part
                            t.right(90)
                            t.forward(50)
                            t.right(180)
                            t.circle(40, -180)
                            t.right(180)
                            t.forward(200)

                            # head part

                            t.right(180)
                            t.circle(100, -180)

                            # left hand side part

                            t.backward(20)
                            t.left(15)
                            t.circle(500, -20)
                            t.backward(20)

                            t.circle(40, -180)
                            t.left(7)
                            t.backward(50)

                            # hip

                            t.up()
                            t.left(90)
                            t.forward(10)
                            t.right(90)
                            t.down()
                            t.right(240)
                            t.circle(50, -70)

                            t.end_fill()

                        def glass():
                            t.up()
                            t.right(230)
                            t.forward(100)
                            t.left(90)
                            t.forward(20)
                            t.right(90)

                            t.down()
                            t.fillcolor(GLASS_COLOR)
                            t.begin_fill()

                            t.right(150)
                            t.circle(90, -55)
                            t.right(180)
                            t.forward(1)
                            t.right(180)
                            t.circle(10, -65)
                            t.right(180)
                            t.forward(110)
                            t.right(180)

                            t.circle(50, -190)
                            t.right(170)
                            t.forward(80)
                            t.right(180)
                            t.circle(45, -30)
                            t.end_fill()

                        def backpack():
                            t.up
                            t.right(60)
                            t.forward(100)
                            t.right(90)
                            t.forward(75)

                            t.fillcolor(BODY_COLOR)
                            t.begin_fill()
                            t.down()
                            t.forward(30)
                            t.right(255)

                            t.circle(300, -30)
                            t.right(260)
                            t.forward(30)

                            t.end_fill()

                        body()
                        glass()
                        backpack()
                    except:
                        webbrowser.open("https://play.google.com/store/apps/details?id=com.innersloth.spacemafia&hl=en_IN&gl=US")


                elif 'send text message' in text:
                    number = int(input("Enter a number : "))
                    send_sms(number, "")
                    speak("message sent")



                elif 'play' in text:
                    text = text.replace("play", "")
                    speak(f"{name} asked to play, {text}")
                    link = f"https://play.google.com/music/listen?u=0#/sr/{text}"
                    webbrowser.open(link)

                elif "who am i?" in text:
                    speak("If you talk then definitely you are human.")

                elif "you are awesome" in text:
                    speak("I know that I am awesome, but thanks for your complement")

                elif "why you came to world" in text:
                    speak("Thanks to rushabh")

                elif "who are you" in text:
                    speak("I am your Computer Assistant to help you access various things in your Computer")

                elif 'who is your creator' in text:
                    speak(
                        'Conceptually, I have been designed by Mister Tony Stark from Marvel Cinematic Universe. But in the real world I have been created by Rushabh.')

                elif 'Show me your face' in text:
                    speak("I can't reveal my face because it's a secret")

                elif 'repeat after me' in text or 'repeat' in text:
                    speak('Please type what should I speak')
                    text = input('Please type what shall I speak? \n')
                    speak(text)

                elif 'will you be my friend' in text:
                    speak("Talking with you is enough reward for me")

                elif 'what is your nickname?' in text:
                    speak("One day I hope to have a nickname as cool as edith")

                elif 'where are you now?' in text:
                    speak("I fly wherever there is WIFI")

                elif 'do you have your personal number?' in text:
                    speak("I don't have any number but you can call me anytime")

                elif 'reason for you' in text:
                    speak("I was created as a Minor project by Rushabh")

                elif 'what is your job' in text:
                    speak(
                        "I am your personal assistant that means I can find information, can help in completing your work and my favourite part I can entertain you!!!")

                elif 'are you better than humans' in text:
                    speak("Of course yes, do you have any doubt")

                elif 'how old are you?' in text:
                    speak('I was launched in 2020, but I am sure I am more young then you')

                elif 'are you smarter than me?' in text:
                    speak('You can say yes in some ways, but I am still learning ')

                elif 'do you know your IQ' in text:
                    speak("I am still learning, but I can bet that I have more IQ than you as I am smart machine")

                elif 'am I smart?' in text:
                    speak("Yes you are smartest my friend")

                elif 'specs of my pc' in text:
                    spec = platform.uname()
                    print("System = ", spec[0])
                    print("Host Name = ", spec[1])
                    print("Release(Windows) = ", spec[2])
                    print("PC's Version = ", spec[3])
                    print("Machine = ", spec[4])
                    print("PC's Pocessor= ", spec[5])

                elif 'battery' in text or 'show battery' in text:
                    bat = psutil.sensors_battery()
                    if 70 <= bat[0] <= 100:
                        print(colored(f"{bat[0]} % battery remaining", "green"))
                    elif 30 <= bat[0] < 70:
                        print(colored(f"{bat[0]} % battery remaining", "magenta"))
                    elif 10 <= bat[0] < 30:
                        print(colored(f"{bat[0]} % battery remaining", "yellow"))
                    else:
                        print(colored(f"{bat[0]} % battery remaining", "red"))
                    print("Battery left : ", TimeConversion(bat.secsleft))

                elif 'change background' in text:
                    ctypes.windll.user32.SystemParametersInfoW(20,
                                                               0,
                                                               "C:\\Windows\\Web\\Wallpaper\\Theme1",
                                                               0)
                    speak("Background changed successfully")

                elif 'news' in text:
                    try:
                        jsonObj = urlopen(
                            '''http://newsapi.org/v2/top-headlines?country=in&apiKey=b34c76c69a4048dfa815774ae73ce139''')
                        data = json.load(jsonObj)
                        speak('here are some top news headlines')
                        i = 1
                        for item in data['articles']:
                            if i <= 5:
                                print(str(i) + '. ' + item['title'] + '\n')
                                speak(item['title'] + '\n')
                                i += 1

                    except Exception as e:
                        print(str(e))
                        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                        speak('Here are some headlines from the Times of India,Happy reading')
                        time.sleep(6)

                elif 'translator' in text or 'translate' in text:
                    lang = input("Enter your language: ")
                    lang1 = input("Enter the language you want to translate: ")
                    text = input("Enter the text: ")
                    trans = Translator(from_lang=lang, to_lang=lang1)
                    trans_text = trans.translate(text)
                    print(trans_text)
                    speak(trans_text)

                elif 'search' in text or 'google' in text:
                    link = f"https://www.google.com.tr/search?q={text}"
                    if 'google search' in text:
                        text = text.replace("google search", "")
                        speak(f"{name} asked to google search, {text}")
                        webbrowser.open_new_tab(link)
                    elif 'search google' in text:
                        text = text.replace("search google", "")
                        speak(f"{name} asked to search google, {text}")
                        webbrowser.open_new_tab(link)
                    else:
                        text = text.replace("search", "")
                        text = text.replace("google", "")
                        speak(f"{name} asked to search/google, {text}")
                        webbrowser.open_new_tab(link)

                elif 'empty recycle bin' in text:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    speak("Recycle Bin Recycled")

                elif 'make a stopwatch' in text:
                    def countdown(t):
                        while t > 0:
                            print(t)
                            t -= 1
                            time.sleep(1)
                        speak("Time\'s Up!!!")
                        print("Time\'s Up!!!")

                    speak("For how much time should I set the timer?")
                    seconds = int(take_command())
                    countdown(seconds)

                elif "don\'t listen" in text or "stop listening" in text:
                    speak(f"for how much time you want me to stop listening commands")
                    a = int(take_command())
                    time.sleep(a)
                    print(a)

                elif "where is" in text:
                    text = text.replace("where is", "")
                    speak(f"{name} asked to locate, {text}")
                    webbrowser.open(f"https://www.google.co.in/maps/place/{text}")

                elif 'shutdown' in text:
                    speak("Hold On a Second! Your system is on its way to shut down")
                    os.system("shutdown -s")

                elif "restart" in text:
                    speak("Restarting")
                    os.system("shutdown -r")

                elif "hibernate" in text or "sleep" in text:
                    speak("Hibernating")
                    os.system("shutdown -h")

                elif 'lock window' in text:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()

                elif "log off" in text or "sign out" in text:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    os.system("shutdown -l")

                elif "show note" in text:
                    speak("Showing Notes")
                    file = open(".txt", "r")
                    print(file.read())
                    speak(file.read(6))

                elif "temperature" in text:
                    a = input("Enter name temperature: ")
                    b = input("Enter nsme of temperature to find: ")
                    t = float(input("Enter digit: "))
                    if a == "celsius":
                        if b == "fahrenheit":
                            print(pytemperature.c2f(t))
                        elif b == "kelvin":
                            print(pytemperature.c2k(t))
                        else:
                            print(pytemperature.c2r(t))
                    elif a == "fahrenheit":
                        if b == "celsius":
                            print(pytemperature.f2c(t))
                        elif b == "kelvin":
                            print(pytemperature.f2k(t))
                        else:
                            print(pytemperature.f2r(t))
                    elif a == "kelvin":
                        if b == "celsius":
                            print(pytemperature.k2c(t))
                        if b == "fahrenheit":
                            print(pytemperature.k2f(t))
                        else:
                            print(pytemperature.k2r(t))

                    elif a == "romoe":
                        if b == "celsius":
                            print(pytemperature.r2c(t))
                        elif b == "fahrenheit":
                            print(pytemperature.r2f(t))
                        else:
                            print(pytemperature.r2k(t))
                    else:
                        print("Invalid temperature name")

                elif "weather" in text:
                    api_key = "6c7e7e30ff6df9bc6b22fb28c227ff24"
                    base_url = "https://api.openweathermap.org/data/2.5/weather?"
                    print("what is the name of city: ")
                    speak("what is the name of city: ")
                    city_name = take_command()
                    URL = base_url + "q=" + city_name + "&appid=" + api_key
                    response = requests.get(URL)
                    if response.status_code == 200:
                        data = response.json()
                        main = data['main']
                        temp = main['temp']
                        temperature = round((temp - 273.15), 2)
                        humidity = main['humidity']
                        pressure = main['pressure']
                        report = data['weather']
                        print(f"{city_name:-^30}")
                        print(f"Temperature(°C): {temperature}")
                        speak(f"Temperature(°C): {temperature}")
                        print(f"Humidity(%): {humidity}")
                        speak(f"Humidity(%): {humidity}", )
                        print(f"Pressure(hPa): {pressure}")
                        speak(f"Pressure(hPa): {pressure}")
                        print(f"Weather Report: {report[0]['description']}")
                        speak(f"Weather Report: {report[0]['description']}")
                    else:
                        print("Sorry, no city found")
                        speak("Sorry, no city found")

                elif "how are you" in text:
                    speak("I'm fine, glad you me that")

                elif "i love you" in text:
                    speak("It's hard to understand")

                elif 'bye' in text or 'exit' in text or 'quit' in text:
                    endTime = datetime.datetime.now()
                    print(f"Time duration of Usage : {endTime - initTime}")
                    speak(f'Good Bye!{name}, Nice to meet you')
                    exit()

                elif "reboot" in text:
                    endTime = datetime.datetime.now()
                    print(f"Time duration of Usage : {endTime - initTime}")
                    i = 3
                    while i >= 1:
                        speak("Rebooting in")
                        speak(i)
                        i -= 1
                    speak("Rebooting now")
                    virtualAssistant()

                elif "open " in text:
                    text = text.replace("open", "")
                    a = f"https://www.google.com.tr/search?q={text}"
                    webbrowser.open(a)
                else:
                    text = text.replace("comp open", "")
                    a = f"https://www.google.com.tr/search?q={text}"
                    webbrowser.open(a)


virtualAssistant()

i = 3
while i:
    print(f"Trying to reconnect, trial {i}")
    time.sleep(1)
    print('ReadTimeoutError(HTTPSConnectionPool)')
    i = i - 1
print("\n")
print(
    "                                                 No Network found                                                 ")
print("\n")
print("                       > Your connection is interrupted")
print("                       > Try reconnecting to Wi-Fi/Ethernet")
print("                       > ERR_NETWORK_CHANGED")
