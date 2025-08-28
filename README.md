# 💻 GroqTalk

**GroqTalk** é uma aplicação de chatbot interativa, desenvolvida para demonstrar o poder da API da Groq em conjunto com uma interface de usuário amigável criada com Streamlit.

O objetivo deste projeto é oferecer uma experiência de conversação fluida, com respostas geradas quase em tempo real, aproveitando a performance única dos LPUs (Language Processing Units) da Groq.



## ✨ Features

* **Interface Direta:** Um layout limpo e simples construído com Streamlit.
* **Respostas Rápidas:** Integração com a API da Groq para uma geração de texto.
* **Gerenciamento de Conversa:**
    * 📥 **Salvar Histórico:** Opção para baixar a conversa completa ou apenas a última resposta do modelo.
    * 🗑️ **Apagar Conversa:** Limpe o histórico para iniciar um novo diálogo.



## 🛠️ Tecnologias

* **Frontend:** Streamlit
* **Backend (LLM):** Groq API
* **Linguagem:** Python
* **Gerenciamento de Chaves:** python-dotenv



## 🚀 Como Executar

Siga os passos abaixo para executar o GroqTalk localmente.

### Pré-requisitos

* Python
* Uma chave de API da [Groq](https://groq.com)

### Instalação

1.  **Clone o repositório:**

      ```bash
      git clone https://github.com/ricdavila/streamlit-groq-chatbot.git
      cd streamlit-groq-chatbot
      ```

2.  **Instale as dependências:**

      ```bash
      pip install -r requirements.txt
      ```

3.  **Configure sua chave de API:**
      - Crie um arquivo chamado `.env` na raiz do projeto.
      - Adicione sua chave da API da Groq da seguinte forma:

      ```bash
      GROQ_API_KEY=<SUA_CHAVE_API_AQUI>
      ```

### Execução

1.  **Inicie a aplicação Streamlit:** 
      ```bash
      streamlit run main.py
      ```

*Execute o comando do `streamlit`dentro do diretório do projeto.*

2. **O aplicativo será aberto automaticamente no seu browser.**



## 🏗️ Estrutura do Projeto

O projeto está organizado da seguinte forma para manter a clareza e a separação de responsabilidades:

`streamlit-groq-chatbot/`

├── `.env` — Arquivo para armazenar as chaves da API (não versionado)

├── `main.py` — Lógica principal da aplicação Streamlit (frontend e fluxo)

├── `groq_ia.py` — Módulo para interagir com a API da Groq (backend)

├── `requirements.txt` — Dependências do projeto

└── `README.md` — Esta documentação

* `main.py`: Responsável por toda a interface do usuário, gerenciamento de estado da sessão (`st.session_state`) e pela orquestração das chamadas ao backend.
* `groq_ia.py`: Gerencia a comunicação com a API da Groq, mantendo a lógica de IA separada da lógica de apresentação.

---

Desenvolvido com 🤍 e ☕ utilizando Python 🐍. Deseja conferir outros projetos? Acesse [meu perfil](https://github.com/ricdavila).
