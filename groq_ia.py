import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def gerar_resposta(mensagens) -> str:
    
    stream = client.chat.completions.create(
        messages=mensagens,
        model="llama-3.3-70b-versatile"
    )

    return stream.choices[0].message.content
