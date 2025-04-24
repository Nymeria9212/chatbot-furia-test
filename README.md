# 🤖 Bot Telegram da FURIA (CS:GO)

Um chatbot feito com Python e Flask para interagir com fãs do time de CS:GO da FURIA diretamente no Telegram! O bot responde comandos como elenco, últimos jogos e até um quiz.

---

## 🚀 Funcionalidades

- `/start` – Mensagem de boas-vindas
- `/elenco` – Lista de jogadores atuais
- `/jogos` – Últimos resultados da equipe
- `/quiz` – Mini quiz interativo
- Reconhecimento de mensagens como "oi"

---

## 📦 Requisitos

- Python 3.9+
- Conta no Telegram
- Bot criado via [BotFather](https://t.me/botfather)

---

## 🛠️ Instalação local

1. Clone este repositório:
```bash
git clone https://github.com/Nymeria9212/chatbot-furia-test.git
cd chatbot-furia-test
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode o app localmente:
```bash
python app.py
```

---

## 🌐 Deploy no Render

1. Faça login em [https://dashboard.render.com](https://dashboard.render.com)
2. Clique em **"New" > "Web Service"**
3. Conecte ao seu GitHub e selecione o repositório
4. Configure:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

5. Após o deploy, copie a URL pública gerada.

6. Configure o webhook no Telegram:
```bash
https://api.telegram.org/bot<SEU_TOKEN>/setWebhook?url=https://SEU-BOT.onrender.com/webhook
```

---

## 📁 Estrutura do projeto

```
furia-bot/
├── app.py               # Código principal do Flask
├── requirements.txt     # Dependências do projeto
└── render.yaml          # (opcional) Configuração automática para o Render
```

---

## 🙋‍♀️ Feito por

Jéssica – desenvolvedora em transição de carreira, estudante de Ciência da Computação e fã da FURIA.  
Com apoio do ChatGPT 🚀

---

## 📌 Observações

- O Render (plano gratuito) pode hibernar o serviço após inatividade.
- Em produção, é ideal proteger o token do bot com variáveis de ambiente.