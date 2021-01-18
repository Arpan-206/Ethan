from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import requests
from pprint import pprint
from datetime import datetime
import time
import numpy as np
import sys
import cv2
import random

current_time = time.strftime("%H:%M:%S")
url = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=cb4360e5dd232b18fbabd10b9842842a&units=metric'
res = requests.get(url)

data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...........")
            audio = R.listen(source)
        try:
            print("Recognising......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            qu1 = self.query
            if 'ethan' or 'Ethan' in self.query:
                if 'goodbye' in self.query:
                    sys.exit()
                elif 'who made you' in qu1 or 'who created you' in qu1:
                    speak('I was made by Mister Arpan Pandey. He is my developer, my creator and my teacher. He taught me how to be smart.')
                elif 'open google' in self.query:
                    speak("opening google")
                    webbrowser.open('www.google.co.in')
                elif "tell me a joke" in self.query or "Crack joke" in self.query or "crack a joke" in self.query:
                        jokes =["A Doctor said to a patient , I'm sorry but you suffer from a terminal illness and have only 10 to live , then the Patient said What do you mean, 10, 10 what, Months, Weeks, and the Doctor said Nine.","Once my Brother who never used to drink was arrested for over drinking,When I lates had gone and asked him why were you arressted, He replied he had not brushed since a week","A Teacher said Kids, what does the chicken give you? The Student replied Meat Teacher said  Very good Now what does the pig give you? Student said BaconTeacher said  Great  And what does the fat cow give you? Student said Homework!","A child asked his father, How were people born? So his father said, Adam and Eve made babies, then their babies became adults and made babies, and so on  The child then went to his mother, asked her the same question and she told him, We were monkeys then we evolved to become like we are now  The child ran back to his father and said, You lied to me  His father replied, No, your mom was talking about her side of the family."]
                        speak(random.choice(jokes))
    
                elif 'open youtube' in self.query:
                    speak("opening youtube")
                    webbrowser.open("www.youtube.com")
                elif 'play music' in self.query:
                    speak("playing music from pc")
                    self.music_dir ="C:/Users/user/Music"
                    self.musics = os.listdir(self.music_dir)
                    os.startfile(os.path.join(self.music_dir,self.musics[0]))
                elif 'exit' in self.query:
                    speak("Bye!Bye! Sad to see you go")
                    sys.exit()
                elif 'weather' in self.query:
                    speak("Temprature is{} degree Celsius".format(temp))
                    speak("WindSpeed is{} metres per second".format(wind_speed))
                    speak("Description is{}.".format(description))
                else:
                    speak("I failed to recognise that!")









FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,860)
        self.label_7 = QLabel
        self.label_10 = QLabel
        self.label_17 = QLabel
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_10 = QMovie("./Ethan.png", QByteArray(), self)
        self.label_10.setCacheMode(QMovie.CacheAll)
        self.label_2.setMovie(self.label_10)
        self.label_10.start()
        self.label_17 = QMovie("./HIHologram-unscreen.gif", QByteArray(), self)
        self.label_17.setCacheMode(QMovie.CacheAll)
        self.label_3.setMovie(self.label_17)
        self.label_17.start()

        self.ts = time.strftime("%A, %d %B")
        self.temp = str(temp)
        self.tt = current_time
        self.longi = str(longitude)
        self.lat = str(latitude)
        Dspeak.start()
        self.label.setPixmap(QPixmap("ETHANBG (1).png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
        self.label_6.setText("<font size=8 color='white'>Temp: "+self.temp+"&#8451;</font>")
        self.label_6.setFont(QFont(QFont('Acens',8)))
        self.LandL.setText("<font size=8 color='white'>Longitude: "+self.longi+ "<br> Latitude:"+self.lat+"</font>")
        self.LandL.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())