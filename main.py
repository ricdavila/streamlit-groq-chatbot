import time
import streamlit as st

import groq_ia

APP_TITLE = 'GroqTalk'
APP_ICON = '💻'
SLEEP_TIME = 0.005


def gerar_layout_pagina() -> None:
    st.session_state.setdefault('mensagens', [{
        'role': 'system', 'content': 'You are a helpful assistant that speaks portuguese with your users, unless they speak another language.'
        }])

    st.set_page_config(page_title=APP_TITLE, 
                    page_icon='💻', 
                    layout='centered'
                    )

    if len(st.session_state.mensagens) <= 1:
        st.container(height=100, border=False)
        st.markdown('<h2><center>Olá, posso ajudar?</center>', unsafe_allow_html=True)
    else:
        st.markdown(f'<h3><center>{APP_ICON}{APP_TITLE}', unsafe_allow_html=True)
        st.divider()


def escrever_resposta_groq(mensagem):
    placeholder = st.empty()
    texto = ''
    for char in mensagem:
        texto += char
        placeholder.markdown(texto)
        time.sleep(SLEEP_TIME)


def adicionar_mensagem(role: str, mensagem: str) -> None:
    st.session_state.mensagens.append({'role': role, 'content': mensagem})


def carregar_historico():
    # carrega e exibe o histórico de mensagens no chat
    for mensagem in st.session_state.mensagens:
        if not mensagem['role'] == 'system':
            with st.chat_message(mensagem['role']):
                st.markdown(mensagem['content'])

def main():

    gerar_layout_pagina()
    carregar_historico()

    # barra de input do usuário
    chat_input = st.chat_input(placeholder='Peça ao Groq', width='stretch')


    # adiciona ao chat o input do usuário e a resposta do Groq
    if chat_input:
        # adicioan o input ao histórico
        adicionar_mensagem('user', chat_input)
        # escreve o input
        with st.chat_message('user'):
            st.markdown(chat_input)
        # gera e escreve a resposta do Groq
        with st.chat_message('assistant'):
            with st.spinner('Só um segundo...'):
                resposta_ia = groq_ia.gerar_resposta(st.session_state.mensagens)
                adicionar_mensagem('assistant', resposta_ia)
                escrever_resposta_groq(resposta_ia)
    

if __name__ == '__main__':
    main()