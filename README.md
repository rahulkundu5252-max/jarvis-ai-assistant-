# Jarvis AI Voice Assistant

Jarvis is a Python-based AI voice assistant designed to make your computing experience more hands-free and intuitive. It listens for a wake word, processes your voice commands, and responds with natural text-to-speech output — all while running efficiently in the background using multi-threading. It also includes a FastAPI backend, allowing Jarvis to be extended into a web-accessible service.

---

## Features

- **Wake Word Activation** — Jarvis stays idle until it hears its name ("Jarvis"), ensuring it only activates when you need it and doesn't consume unnecessary resources.
- **Sleep Mode** — You can put Jarvis to sleep with a voice command, allowing it to pause listening without fully shutting down the program.
- **Voice Command Recognition** — Using the SpeechRecognition library, Jarvis captures and processes spoken commands in real time with support for ambient noise adjustment.
- **Web Navigation** — Jarvis can instantly open popular websites like YouTube, Google, and GitHub directly in your default browser using a simple voice command.
- **Text-to-Speech Responses** — All responses are spoken aloud using `pyttsx3`, giving Jarvis a conversational feel without requiring an internet connection for speech output.
- **FastAPI Backend Support** — A built-in REST API layer built with FastAPI allows Jarvis's functionality to be triggered and explored via HTTP endpoints, making it easy to integrate with other tools or a frontend UI.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **SpeechRecognition** | Capturing and processing voice input from the microphone |
| **pyttsx3** | Offline text-to-speech engine for spoken responses |
| **FastAPI** | Lightweight web framework for exposing Jarvis features as REST API endpoints |
| **threading** | Running listening and processing tasks concurrently for smooth performance |

---

## Project Structure

```bash
project/
│
├── jarvis.py        # Core logic: wake word detection and command handling
├── voice_mode.py    # Microphone input, speech recognition, and activation loop
├── main.py          # FastAPI app entry point with route definitions
└── README.md        # Project documentation
```

---

## Installation

Make sure you have **Python 3.7+** installed, then install all required dependencies using:

```bash
pip install -r requirements.txt
```

> **Note:** `pyttsx3` may require additional system-level dependencies depending on your OS (e.g., `espeak` on Linux or `SAPI` on Windows). Refer to the [pyttsx3 documentation](https://pyttsx3.readthedocs.io/) if you run into issues.

---

## Run Voice Assistant

Launch Jarvis in voice mode by running:

```bash
python voice_mode.py
```

Once started, Jarvis will begin listening for the wake word **"Jarvis"**. Speak clearly near your microphone and follow up with a command after it acknowledges you.

**Example commands:**
- *"Jarvis, open YouTube"*
- *"Jarvis, open Google"*
- *"Jarvis, sleep"*

---

## Run FastAPI Server

To start the FastAPI backend server, run:

```bash
uvicorn main:app --port 8001
```

Once the server is running, open your browser and navigate to the interactive API documentation:

```text
http://127.0.0.1:8001/docs
```

This opens the auto-generated **Swagger UI**, where you can explore and test all available API endpoints directly from your browser — no additional tooling required.

---

## Future Improvements

The following features are planned for upcoming versions:

- **AI Chatbot Integration** — Connect Jarvis to a large language model (e.g., GPT or Gemini) so it can answer open-ended questions and hold natural conversations.
- **Frontend UI** — Build a visual interface to display conversation history, assistant status, and quick-action controls.
- **Memory System** — Enable Jarvis to remember user preferences, past interactions, and session context for a more personalized experience.
- **Application Automation** — Extend functionality to control desktop apps, manage files, set reminders, and perform system-level tasks.
- **Smart Assistant Features** — Add capabilities like weather updates, calendar integration, news briefings, and smart home control.

---

## Author

**Rahul Kundu**