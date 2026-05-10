from fastapi import FastAPI
from pydantic import BaseModel
from jarvis import process_command

app = FastAPI()


class Command(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Jarvis API is running"
    }


@app.post("/jarvis")
def jarvis_api(command: Command):

    try:
        response = process_command(command.text)

        return {
            "response": response
        }

    except Exception as e:
        return {
            "error": str(e)
        }