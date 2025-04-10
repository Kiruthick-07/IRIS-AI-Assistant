import datetime
import os
import speech_recognition as sr
import pyttsx3
import subprocess
import sys
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
recognizer = sr.Recognizer()

def listen_for_wake_word():
    with sr.Microphone() as source:  # ✅ Fixed: Properly instantiated Microphone
        print("Program Activated, waiting for command...")
        while True:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recognized_audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(recognized_audio, language='en-US').lower()  # ✅ Fixed: using recognize_google instead of recognize_bing
                print(f"Recognized: {text}")
                if "iris" in text:
                    print("Wake word detected: IRIS")
                    engine.say("Hello, how can I help you?")
                    engine.runAndWait()  # ✅ Added so it actually speaks
                    return True  # ✅ This allows main loop to proceed to command()
            except Exception as ex:
                print("Unable to fetch audio, please try again")
                engine.say("Command not detected, please try again")
                engine.runAndWait()  


def command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source , duration=0.5)
        recognized_audio= recognizer.listen(source)

    try:
        text= recognizer.recognize_google(recognized_audio,language='en_us').lower()
        print(text)
    except Exception as ex:
        print(ex)
        return
    if "stop" or "mute" in text:
        sys.exit()
    if "open" in text:
        program_name = text.replace('open', '').strip()
        open_program(program_name)
    elif "close" in text:
        program_name = text.replace('close', '').strip()
        close_program(program_name)
    elif "date" in text or "time" in text:
        current_time = datetime.datetime.now().strftime('%I:%M %P')
        print(current_time)
        speak(current_time)
    elif "who are you" or "about you" or "what is your name" in text:
        speak("Hello , Im IRIS an AI personal assistant")

def open_program(program_name):
    if "chrome" in program_name or "browser" in program_name:
        location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        speak_and_open("Opening Chrome browser", location)
    elif "edge" in program_name:
        location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        speak_and_open("Opening Edge browser", location)
    elif "brave" in program_name:
        path = r"C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
        speak_and_open("Opening Brave browser", path, is_shortcut=True)
    elif "whatsapp" in program_name:
        location = r"C:\Users\ADMIN\AppData\Local\WhatsApp\WhatsApp.exe"
        speak_and_open("Opening WhatsApp", location)
    elif "vs code" in program_name:
        path = r"C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
        speak_and_open("Opening VS Code", path, is_shortcut=True)
    elif "calculator" in program_name:
        subprocess.Popen(['calc.exe'])
        engine.say("Opening Calculator")
        engine.runAndWait()
    else:
        engine.say("Unable to open the program, try again or check my source code for more.")
        engine.runAndWait()

def speak_and_open(message, path, is_shortcut=False):
    engine.say(message)
    engine.runAndWait()
    if is_shortcut:
        os.startfile(path)
    else:
        subprocess.Popen([path])

    
def close_program(program_name):
    if "chrome" in program_name:
        engine.say("closing program")
        engine.runAndWait()
        os.system("taskkill /f/im chrome.exe")
    elif "edge" in program_name:
        engine.say("closing program")
        engine.runAndWait()
        os.system("taskkill /f/ im msedge.exe")
    elif "brave" in program_name:
        engine.say("closing program")
        engine.runAndWait()
        os.system("taskkill /f/ im brave.exe")
    elif "whatsapp" in program_name:
        engine.say("closing program")
        engine.runAndWait()
        os.system("taskkill /f/ im whatsapp.exe")
    else:
        engine.say("Unable to close the program,try again or check my source code for more.")
        engine.runAndWait()
    

while True:
    if listen_for_wake_word():
        while True:
            if command():
                break
            

    
