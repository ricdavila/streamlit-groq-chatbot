import time
import streamlit as st
import groq_ia

APP_TITLE = 'GroqTalk'
APP_ICON = '💻'
SLEEP_TIME = 0.005


def gerar_layout_pagina() -> None:
    '''Carrega os principais widgets e configurações do layout da página'''
    st.set_page_config(
        page_title=APP_TITLE, 
        page_icon='💻', 
        layout='centered',
    )    
    st.markdown(f'<h3><center>{APP_ICON}{APP_TITLE}', unsafe_allow_html=True)
    if len(st.session_state.mensagens) <= 1:
        st.markdown('<h2><center>Olá, posso ajudar?</center>', unsafe_allow_html=True)


def escrever_resposta_groq(mensagem: str) -> None:
    '''Escreve a resposta do Groq com efeito de digitação'''
    placeholder = st.empty()
    texto = ''
    for char in mensagem:
        texto += char
        placeholder.markdown(texto)
        time.sleep(SLEEP_TIME)


def adicionar_mensagem(role: str, mensagem: str) -> None:
    '''Adiciona mensagens ao histórico do chat'''
    st.session_state.mensagens.append({'role': role, 'content': mensagem})


def carregar_historico() -> None:
    '''Carrega e exibe cada mensagem presente no histórico'''
    for mensagem in st.session_state.mensagens:
        if not mensagem['role'] == 'system':
            with st.chat_message(mensagem['role']):
                st.markdown(mensagem['content'])

def main() -> None:
    st.session_state.setdefault('mensagens', [
        {'role': 'system', 'content': 'You are a helpful assistant that speaks portuguese with your users, unless they speak another language.'}
    ])
    gerar_layout_pagina()
    carregar_historico()

    # input do usuário
    entrada_usuario = st.chat_input(placeholder='Peça ao Groq', width='stretch')

    # atualiza o histórico, exibe o input do usuário e escreve a resposta do groq
    if entrada_usuario:
        # usuário
        adicionar_mensagem('user', entrada_usuario)
        with st.chat_message('user'):
            st.markdown(entrada_usuario)
        # Groq
        with st.chat_message('assistant'):
            with st.spinner('Só um segundo...'):
                resposta_ia = groq_ia.gerar_resposta(st.session_state.mensagens)
                adicionar_mensagem('assistant', resposta_ia)
                escrever_resposta_groq(resposta_ia)
    

if __name__ == '__main__':
    main()