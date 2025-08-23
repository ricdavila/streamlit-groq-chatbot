import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def gerar_resposta(mensagens):
    
    stream = client.chat.completions.create(
        messages=mensagens,
        model="llama-3.3-70b-versatile"
    )

    resposta = stream.choices[0].message.content
    mensagens.append({'role': 'assistant', 'content': resposta})

    return stream.choices[0].message.content