from fastapi import FastAPI, Header, HTTPException
import base64
from .engine import behaviour_score, decide

app = FastAPI()

API_KEY = "VOICE_2026_KEY"

@app.post("/analyze")
async def analyze(data: dict, x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(401, "Invalid API Key")

    audio = data.get("audio_base64")

    with open("temp.mp3", "wb") as f:
        f.write(base64.b64decode(audio))

    score = behaviour_score("temp.mp3")
    result, conf = decide(score)

    return {
        "result": result,
        "confidence": conf
    }
