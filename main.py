import os
import streamlit as st

import groq_ia

if not 'mensagens' in st.session_state:
    st.session_state.mensagens = []

st.set_page_config(page_title='chat')
barra_input = st.chat_input()


if barra_input:
    #st.write(st.session_state.mensagens)
    st.session_state.mensagens.append({'role': 'user', 'content': barra_input})
    st.markdown(groq_ia.gerar_resposta(st.session_state.mensagens))