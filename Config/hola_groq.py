from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: No existe GROQ_API_KEY")
    exit()

client = Groq(api_key=api_key)

respuesta = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": "Hola"
        }
    ]
)

print(respuesta.choices[0].message.content)