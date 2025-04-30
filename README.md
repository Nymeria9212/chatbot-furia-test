# 🤖 Bot Fã da FURIA (Telegram)

Este projeto é um chatbot para fãs do time de CS:GO da FURIA, integrado ao Telegram. Ele permite visualizar o elenco, resultados recentes, interagir com um quiz, acompanhar partidas ao vivo e muito mais!

## 🚀 Funcionalidades

- Ver elenco atual do time
- Últimos resultados de partidas
- Quiz com perguntas sobre a FURIA
- Status de partidas ao vivo
- Link para o Contato Inteligente da FURIA via WhatsApp
- Comunidade oficial no Discord
- Menu interativo diretamente no Telegram

## 📸 Demonstração

<img src="https://i.imgur.com/nqEXyRo.png" width="300"/>

## 📦 Tecnologias Usadas

- Python
- Flask
- Telegram Bot API
- Render (deploy)
- GitHub (repositório)

## 💡 Como Rodar Localmente:

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/bot-furia-chat.git
cd bot-furia-chat
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Exporte seu token do Telegram como variável de ambiente:

No Linux/Mac:

```bash
export BOT_TOKEN=seu_token_do_bot
```

No Windows (cmd):

```cmd
set BOT_TOKEN=seu_token_do_bot
```

5. Execute o servidor Flask:

```bash
python app.py
```

6. Use o [ngrok](https://ngrok.com) para gerar uma URL pública e configure seu webhook:

```bash
ngrok http 5000
```

Configure o webhook com o link fornecido:

```bash
https://api.telegram.org/botSEU_TOKEN/setWebhook?url=https://seulink.ngrok.io/webhook
```

---

### 🔐 Segurança do Token

Para proteger seu token do BotFather, utilize variáveis de ambiente em vez de colocá-lo diretamente no código.

**No código Python**, substitua:

```python
TOKEN = 'seu_token_aqui'
```

por:

```python
TOKEN = os.environ.get('BOT_TOKEN')
```

**No Render**, adicione a variável de ambiente:

1. Vá até seu serviço no [Render Dashboard](https://dashboard.render.com/).
2. Acesse a aba **Environment**.
3. Clique em **Add Environment Variable** e preencha:
   - **Name**: `BOT_TOKEN`
   - **Value**: seu token real do Telegram (copiado do BotFather).

✅ Com isso, seu token estará seguro, sem ficar exposto no repositório público.

---

## 🌐 Deploy no Render

1. Faça login em [https://render.com](https://render.com) e crie um novo Web Service.
2. Conecte com seu repositório GitHub.
3. Defina o comando de start: `python app.py`
4. Adicione a variável de ambiente `BOT_TOKEN` com o valor do token do seu bot.
5. Após o deploy, copie a URL do serviço e configure o webhook do Telegram.

---

## 🧠 Créditos

Desenvolvido por Jéssica 💜 com apoio do ChatGPT.