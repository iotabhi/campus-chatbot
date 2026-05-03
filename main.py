from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from claude_client import get_claude_response

app = FastAPI()

# Allow Sahil's frontend to talk to your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This defines what Sahil must send
class ChatRequest(BaseModel):
    messages: list

# This is your one and only endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    reply = await get_claude_response(request.messages)
    return {"reply": reply}

# Health check - just to confirm server is alive
@app.get("/")
def root():
    return {"status": "Campus Chatbot API is running"}
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)