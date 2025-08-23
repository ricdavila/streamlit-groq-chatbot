import time
import streamlit as st

import groq_ia

def escrever_mensagem(mensagem):
    placeholder = st.empty()
    texto = ''
    for char in mensagem:
        texto += char
        placeholder.markdown(texto)
        time.sleep(0.005) # controla a velocidade de exibição do texto

# gera o atributo 'mensagens' na sessão atual, inicializando o histórico do chat
if not 'mensagens' in st.session_state:
    st.session_state.mensagens = [
        {'role': 'system', 'content': 'You are a helpful assistant that speaks portuguese with your users, unless they speak another language.'}
    ]

# gera o layout da página
st.set_page_config(page_title='GroqTalk', 
                   page_icon='💻', 
                   layout='centered'
                   )

st.title('💻GroqTalk')
st.divider()
chat_input = st.chat_input()

# carrega o histórico de mensagens no chat
for mensagem in st.session_state.mensagens:
    if not mensagem['role'] == 'system':
        with st.chat_message(mensagem['role']):
            st.markdown(mensagem['content'])

# escreve o input do usuário e a resposta do chatbot
if chat_input:
    st.session_state.mensagens.append({'role': 'user', 'content': chat_input})
    # carrega o último input e a resposta do chatbot
    with st.chat_message('user'):
        st.markdown(chat_input)
    # gera a resposta do chatbot e a escreve com efeito de digitação
    with st.chat_message('assistant'):
        with st.spinner('Só um segundo...'):
            escrever_mensagem(groq_ia.gerar_resposta(st.session_state.mensagens))
