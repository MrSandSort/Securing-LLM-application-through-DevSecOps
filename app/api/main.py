from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os, re, json

app = FastAPI(title="Secure LLM API")

class Query(BaseModel):
    question: str = Field(..., max_length=4000)

def sanitize_input(text: str) -> str:
    # very light example: strip HTML and scripts
    text = re.sub(r"<[^>]+>", "", text)
    return text

def validate_output(obj):
    # Ensure schema-like shape
    if "answer" not in obj:
        raise ValueError("Missing 'answer' field")


@app.get("/")
def root():
    return {"status": "ok", "message": "Secure LLM API is running"}

@app.post("/ask")
def ask(q: Query):
    prompt = sanitize_input(q.question)
    # call model (mock)
    output = {"answer": f"Echo: {prompt}", "sources": []}
    try:
        validate_output(output)
    except Exception as e:
        raise HTTPException(500, str(e))
    # TODO: PII redaction, policy checks, logging with redaction
    return output
