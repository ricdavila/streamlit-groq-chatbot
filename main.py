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
    # mensagem inicial
    if len(st.session_state.mensagens) <= 1:
        st.container(height=150, border=False)
        st.markdown('<h2><center>Olá, posso ajudar?</center>', unsafe_allow_html=True)
    # sidebar
    with st.sidebar:
        st.markdown(f'<center><h1>{APP_ICON}{APP_TITLE}', unsafe_allow_html=True)
        st.divider()
        # salvar
        if len(st.session_state.mensagens) > 1:
            st.button(
                'Salvar', 
                icon=':material/download:', 
                width='stretch', 
                on_click=salvar_conversa)
        # apagar
        st.button(
            '**Apagar**',
            icon=':material/delete:',
            width='stretch',
            type='primary',
            on_click=apagar_conversa)


def carregar_historico() -> None:
    '''Carrega e exibe cada mensagem presente no histórico'''
    for mensagem in st.session_state.mensagens:
        if not mensagem['role'] == 'system':
            with st.chat_message(mensagem['role']):
                st.markdown(mensagem['content'])


def apagar_conversa() -> None:
    '''Apaga o histórico de mensagens'''
    st.session_state.mensagens = [
        {'role': 'system', 'content': 'You are a helpful assistant that speaks portuguese with your users, unless they speak another language.'}
    ]


def adicionar_mensagem(role: str, mensagem: str) -> None:
    '''
    Adiciona mensagens ao histórico do chat
    
    Args:
        role(str): 'assistant' ou 'user'
        mensagem(str): o conteúdo da mensagem
    '''
    st.session_state.mensagens.append({'role': role, 'content': mensagem})


def escrever_resposta_groq(mensagem: str) -> None:
    '''
    Escreve a resposta do Groq com efeito de digitação

    Args:
        mensagem(str): resposta do modelo
    '''

    placeholder = st.empty()
    texto = ''
    for char in mensagem:
        texto += char
        placeholder.markdown(texto)
        time.sleep(SLEEP_TIME)


def converter_para_download(historico: list) -> str:
    '''
    Converte o histórico de mensagens em formato passível de download
    
    Args:
        historico(list): lista contendo o histórico de mensagens
    '''
    role = ''
    mensagens = ''
    for mensagem in historico[1:]:
        if mensagem['role'] == 'assistant':
            role = 'Groq'
        else:
            role = 'User'
        mensagens += f'**{role}:** {mensagem['content']}\n'
    return mensagens


@st.dialog(':material/download: Salvar Conversa')
def salvar_conversa() -> None:
    '''Popup para salvamento da conversa'''

    conversa = converter_para_download(st.session_state.mensagens)
    st.markdown('Você deseja salvar o **histórico completo** dessa conversa ou somente a **última mensagem** enviada pelo Groq?', unsafe_allow_html=True)
    st.container(height=25, border=False)
    # todas as mensagens
    st.download_button(
        'Todas as mensagens',
        data=conversa,
        file_name='full_chat.txt',
        icon=':material/history:',
        width='stretch')
    # apenas a última mensagem
    st.download_button(
        'Apenas a última',
        data=st.session_state.mensagens[len(st.session_state.mensagens)-1]['content'],
        file_name='last_message.txt',
        icon=':material/chat:',
        width='stretch')


def main() -> None:

    st.session_state.setdefault('mensagens', [
        {'role': 'system', 'content': 'You are a helpful assistant that speaks portuguese with your users, unless they speak another language.'}
    ])

    gerar_layout_pagina()
    carregar_historico()

    # input do usuário
    entrada_usuario = st.chat_input(placeholder='Peça ao Groq', width='stretch')

    if entrada_usuario:
        # usuário
        adicionar_mensagem('user', entrada_usuario)
        with st.chat_message('user'):
            st.markdown(entrada_usuario)
        # Groq
        with st.chat_message('assistant'):
            with st.spinner('Só um segundo...'):
                try:
                    resposta_ia = groq_ia.gerar_resposta(st.session_state.mensagens)
                except Exception as e:
                    st.error(e)
                else:
                    adicionar_mensagem('assistant', resposta_ia)
                    escrever_resposta_groq(resposta_ia)
                

if __name__ == '__main__':
    main()
