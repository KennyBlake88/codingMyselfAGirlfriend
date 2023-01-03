import numpy as np
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os

class ChatBot():
    def __init__(self, name):
        self.name = name
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.text = ""

        for voice in self.voices:
            print(voice.name)
            print(voice.gender)

        self.engine.setProperty('voice', self.voices[1].id)


    def speech_to_text(self):
    
        recognizer = sr.Recognizer()

        with sr.Microphone() as mic:
            print("listening")
            audio = recognizer.listen(mic)

        try:
           self.text = recognizer.recognize_google(audio)
        except:
            print("error")

    def wake_up(self, text):
        return True if self.name in text or "Sofia" in text else False


    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()



if __name__ == "__main__":
    ai = ChatBot(name="Sophia")
    while True:
        ai.speech_to_text()
        if ai.wake_up(ai.text) is True:
            res = "Hello, Kenny! How are you babe?"
            ai.text_to_speech(res)


