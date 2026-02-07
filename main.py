from fastapi import FastAPI

app = FastAPI()

@app.get("/wellcom")
def welcom():
    return {
        "message": "Hello world!"
    }
