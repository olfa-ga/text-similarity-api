from fastapi import FastAPI
from app.models.schemas import TextPair
from app.services.similarity import compute_similarity

app = FastAPI(title="Text Similarity API")

@app.get("/")
def home():
    return {"message": "Text Similarity API is running"}

@app.post("/detect")
def detect_similarity(pair: TextPair):
    result = compute_similarity(pair.text1, pair.text2)
    return result

