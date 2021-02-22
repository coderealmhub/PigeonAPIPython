from typing import Optional
from fastapi import FastAPI

title = "Pigeon SMS Gateway API"
description = "API Python to App Android Pigeon SMS Gateway."
version = "0.0.1 Beta"
docs = "http://127.0.0.1:1404/docs"
redoc = "http://127.0.0.1:1404/redoc"


app = FastAPI(title=title, description=description, version=version)


@app.get("/")
def read_root():
    return {
        "title": title,
        "description": description,
        "docs": docs,
        "redoc": redoc,
        "version": version,
    }

@app.get("/send/{device_id}")
def read_send(device_id: str):
    if device_id == "fd8095e0956a5216":
        request = {
            "error": False,
            "response": [
                {
                    "uuid": "33d9498-c4e6-4c3f-b2e3-fad37b743b1b",
                    "number": "88988463405",
                    "message": "Hello World Pigeon SMS Gateway Realm!",
                },
                {
                    "uuid": "33d9498-c4e6-4c3f-b2e3-fad37b743b1a",
                    "number": "88999133076",
                    "message": "Hello World Pigeon SMS Gateway Realm!",
                },
                {
                    "uuid": "33d9498-c4e6-4c3f-b2e3-fad37b743b1d",
                    "number": "88987652020",
                    "message": "Hello World Pigeon SMS Gateway Realm!",
                },
                {
                    "uuid": "33d9498-c4e6-4c3f-b2e3-fad37b743b1d",
                    "number": "88999151923",
                    "message": "Hello World Pigeon SMS Gateway Realm!",
                }
            ],
        }

    return request


@app.put("/status/{device_id}")
def write_status(device_id: str, message_uuid: str, status: int):
    # SENT, FAILED, DELIVERED
    return {"device_id": device_id, "message_uuid": message_uuid, "status": status}


@app.post("/receive/{device_id}")
def read_receive(device_id: str, number: int, message: str):
    return {"device_id": device_id, "number": number, "message": message}
