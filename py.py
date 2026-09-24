import speech_recognition as sr
import subprocess
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

a=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
    a.adjust_for_ambient_noise(source)
    print("Listening ...")
    try:
        audio=a.listen(source,phrase_time_limit=10,timeout=4)

        text=a.recognize_google(audio)
        print(text)
        if "open firefox" in text.lower():
            subprocess.Popen(["firefox"])

        elif "search youtube" in text.lower():
            driver=webdriver.Firefox()
            driver.get("https://www.youtube.com/")
            time.sleep(40)
            driver.quit()
        else:
            print("what the fuck are you talking about gng ...")


    except sr.UnknownValueError:
        print("I couldn't understand you.")
    except sr.RequestError:
        print("Internet/API service failed Atm ...")
    except sr.WaitTimeoutError:
        print("Speak early gang ...")