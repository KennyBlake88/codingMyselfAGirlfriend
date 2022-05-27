from google.cloud import speech_v1 as speech
from enum import Enum
import pyaudio
from time import strftime

#i always type it wrong so:
true = True
false = False

class SpeechEvent(Enum):
    """
    I'm "smart" (lazy) and dont feel like memorizing what int means what, so I wrote an enum.
    #coding
    """
    STARTED_TALKING = 1 #User has started talking
    STOPPED_TALKING = 2 #User has stopped talking
    MUTED_LISTENER = 3 # User has muted the listeners

class SpeechRecognition:
    
    def __init__(self):
        #public members
        self.currentText: str = ""
        self.kennySpeaking: bool = False
        
        #private members
        self._client = speech.SpeechClient()
        self._subscribed: list = []
        self._pyaud = pyaudio.PyAudio()
        self._CHUNK = 1024
        self._RATE = 44100
        self._INTERVAL = 1
    
    def startAudioListening(self):
        self._pyaud.open(format = pyaudio.paInt16, 
        channels = 1,
        rate=self._RATE, 
        frames_per_buffer =self._CHUNK, 
        input = True)

        
    def _transcribeText(self): 
        pass


    def subscribe(self, subscriber):
        """
        The observers "subscribed" to this observed will be notified whenever an event that needs their attention takes place. 
        For example: The AI will stop speaking if it hears the user talk, or if the user presses the button to mute it or something.
        """
        if subscriber not in self._subscribed:
            self._subscribed.append(subscriber)

    def _notify(self, eventName: SpeechEvent):
        """
        The method used to notify the "subscribed" members that the user is speaking. 
        """
        for i in self._subscribed:
            i.post(eventName)