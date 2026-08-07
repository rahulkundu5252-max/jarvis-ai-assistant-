import speech_recognition as sr
from jarvis import process_command, speak

recognizer = sr.Recognizer()


def take_command():

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        except sr.WaitTimeoutError:
            return ""

    try:

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except:
        return ""



awake = False

speak("Say Jarvis to activate me")


while True:

    command = take_command()

    if not command:
        continue

    # =====================
    # SLEEP MODE
    # =====================

    if not awake:

        if "jarvis" in command:

            awake = True

            speak("Yes Rahul, I am listening")

    # =====================
    # ACTIVE MODE
    # =====================

    else:

        # SLEEP COMMAND
        if "sleep" in command:

            awake = False

            speak("Going to sleep")

        # IGNORE REPEATED JARVIS
        elif command == "jarvis":

            continue

        # PROCESS COMMANDS
        else:

            process_command(command)