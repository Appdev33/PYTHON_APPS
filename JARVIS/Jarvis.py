import speech_recognition as sr
import pyttsx3
import time
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
engine = pyttsx3.init()


recognizer = sr.Recognizer()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Record(*argv):
    with sr.Microphone() as source:
        if(argv[0]!= None):
            speak(argv[0])
            print("Adjusting noise ")
            # recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Recording for 4 seconds")
            recorded_audio = recognizer.listen(source, timeout=5)

            print(type(recorded_audio))
            print("Done recording")
        else:
            print("Taking Reply")
            recorded_audio = recognizer.listen(source, timeout=3)


    return recorded_audio

''' recording the sound '''
def Command():
    while(True):



        try:

            Rec = Record("Hello Sir! How can I Help You!")
            print("Recognizing the text")
            text = recognizer.recognize_google(
                    Rec,
                    language="en-US"
                )
            print("Decoded Text : {}".format(text))
            time.sleep(2)

            speak("Do you Mean to say ?")
            speak(text)
            time.sleep(1)
            Reply = Record()
            print('hello')
            text = recognizer.recognize_google(
                Reply,
                language="en-US"
            )
            print(Reply)
            time.sleep(2)

            #
            if(Reply=="Yes"):
                speak("Searching what you said")




        except Exception as ex:
            print(ex)
            speak("Unable to Recognize your voice. Please try Again After beep")




# Additional Functionalities

Command()

def Time():
    pass
def Search():
    pass
def Email():
    pass
def Reminder():
    pass
def Bookings():
    pass
def TrackPrices():
    pass
def LocateThings():
    pass
def Call():
    pass
def SendMsg():
    pass
def SetAlarm():
    pass
def Weather():
    pass
def News():
    pass
def PlayMusic():
    pass
def PlayVideo():
    pass
def WhoisThere():
    pass


