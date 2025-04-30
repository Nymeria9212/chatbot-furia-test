from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Token do BotFather
TOKEN = '8000016573:AAFEqkOwh279clP3m5PwfyiW-xQO_5BOHSc'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# Função para definir os comandos do menu
def set_commands():
    commands = [
        {"command": "elenco", "description": "Ver elenco atual"},
        {"command": "jogos", "description": "Últimos resultados"},
        {"command": "quiz", "description": "Responder quiz"},
        {"command": "live", "description": "Status de jogo ao vivo"},
        {"command": "whatsapp", "description": "Contato inteligente da FURIA"}
    ]
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/setMyCommands",
        json={"commands": commands}
    )

# Define os comandos ao iniciar o bot
set_commands()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').lower()

    # Menu inicial
    if text == '/start':
        reply = "Fala, fã da FURIA! 🐾 Use os comandos abaixo para interagir:\n/elenco\n/jogos\n/quiz\n/live\n/whatsapp"

    # Comandos específicos
    elif text == '/elenco':
        reply = "Elenco atual:\n🎯 arT\n🔫 KSCERATO\n🧠 yuurih\n🔥 chelo\n⚡ FalleN"

    elif text == '/jogos':
        reply = "Últimos jogos:\n1. FURIA 2x1 NIP\n2. FURIA 1x2 NAVI\n3. FURIA 2x0 MIBR"

    elif text == '/live':
        reply = "🕐 Agora: FURIA x Vitality | MAPA 1 - 10x7 (em andamento)\n🔗 Acompanhe ao vivo: https://twitch.tv/furia"

    elif text == 'whatsapp':
        reply = "Você pode falar com o Contato Inteligente da FURIA (closed beta) pelo WhatsApp:\n👉 https://wa.me/5511993404466"

    elif text == '/quiz':
        reply = "🏆 Qual foi o primeiro campeonato que a FURIA ganhou?\n(a) CBCS\n(b) ESL Brasil\n(c) DreamHack"

    elif text in ['a', 'b', 'c']:
        if text == 'c':
            reply = "🎉 Acertou! DreamHack foi o primeiro título importante da FURIA!"
        else:
            reply = "❌ Resposta errada! A resposta certa é (c) DreamHack."

    elif text == 'oi':
        reply = "Salve, fã da FURIA! 😎🔥"

    else:
        reply = f"Você disse: {text}"

    # Envia a resposta pro Telegram
    requests.post(TELEGRAM_API_URL, json={
        'chat_id': chat_id,
        'text': reply
    })

    return 'ok'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Porta definida pelo Render ou 5000 local
    app.run(host='0.0.0.0', port=port)
