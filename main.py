from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from claude_client import get_claude_response

load_dotenv()

app = FastAPI()

# CORS (important for frontend)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://campus-chatbot-pd7gg3b3x-sahil-kumar-2428s-projects.vercel.app",
        "https://campus-chatbot.vercel.app",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request format
class ChatRequest(BaseModel):
    messages: list

# Health check route
@app.get("/")
def root():
    return {"status": "Campus Chatbot API is running"}

# ✅ FINAL CHAT ROUTE (uses your system prompt + FAQ)
@app.post("/chat")
async def chat(request: ChatRequest):
    reply = await get_claude_response(request.messages)
    return {"reply": reply}