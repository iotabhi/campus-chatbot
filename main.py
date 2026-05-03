from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    messages: list

@app.get("/")
def root():
    return {"status": "Campus Chatbot API is running"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=request.messages,
    )
    return {"reply": response.choices[0].message.content}