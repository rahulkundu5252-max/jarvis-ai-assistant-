import datetime
import webbrowser
import random
import pyttsx3
import threading

responses = [
    "Right away sir",
    "On it Rahul",
    "Processing your request",
    "Done"
]



# =========================
engine = pyttsx3.init()

engine.setProperty('rate', 170)

lock = threading.Lock()


def speak(text):
    print("Jarvis:", text)

    def run():
        with lock:
            engine.stop()
            engine.say(text)
            engine.runAndWait()

    threading.Thread(target=run, daemon=True).start()


# =========================
# COMMAND PROCESSOR
# =========================
def process_command(command):

    command = command.lower().strip()

    if "open google" in command:
        speak(random.choice(responses))
        webbrowser.open("https://google.com")
        return "opened google"

    elif "open youtube" in command:
        speak(random.choice(responses))
        webbrowser.open("https://youtube.com")
        return "opened youtube"

    elif "open github" in command:
        speak(random.choice(responses))
        webbrowser.open("https://github.com")
        return "opened github"

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
        return current_time

    elif "hello" in command:
        speak("Hello Rahul")
        return "hello"

    elif "sleep" in command:
        speak("Going to sleep")
        return "sleep"

    else:
        speak("Command not recognized")
        return "unknown command"