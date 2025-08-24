import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError('Defina GROQ_API_KEY no .env')

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def gerar_resposta(mensagens) -> str:
    
    stream = client.chat.completions.create(
        messages=mensagens,
        model="llama-3.3-70b-versatile"
    )

    return stream.choices[0].message.content
