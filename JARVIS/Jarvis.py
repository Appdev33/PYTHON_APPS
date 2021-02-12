import speech_recognition as sr
import pyttsx3
import time
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
engine = pyttsx3.init()


recognizer = sr.Recognizer()

''' recording the sound '''
while(True):
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=6)
        print("Done recording")


    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio,
                language="en-US"
            )
        print("Decoded Text : {}".format(text))
        time.sleep(2)
        if(text=="hello"):
            engine.say("Hello Sir! How can I Help You!")
            engine.runAndWait()


    except Exception as ex:
        print(ex)