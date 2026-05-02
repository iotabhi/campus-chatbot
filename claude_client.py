import os
from groq import AsyncGroq
from dotenv import load_dotenv
from system_prompt import get_system_prompt

load_dotenv()

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

async def get_claude_response(messages: list) -> str:
    
    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1024,
        messages=[
            {"role": "system", "content": get_system_prompt()},
            *messages
        ]
    )
    
    return response.choices[0].message.content