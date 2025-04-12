import openai
from openai import OpenAI
import os
from .elements import Room
from utils.prompts import ROOM_PROMPT

client = None

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except openai.OpenAIError:
    client = None

def flavor_room(room: Room, system: str = "OSE") -> str:
    if client:
        prompt = ROOM_PROMPT.format(size=room.size, system=system)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content.strip()
    else:
        return "Room description requires OPENAI Key"