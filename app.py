from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Substitua pelo seu token do BotFather
TOKEN = '8000016573:AAFEqkOwh279clP3m5PwfyiW-xQO_5BOHSc'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').lower()

    # Define a resposta baseada no texto recebido
    if text == '/start':
        reply = "Fala, fã da FURIA! 🐾 Escolha uma opção do menu ou mande uma mensagem!"
    elif text == '/elenco':
        reply = "Elenco atual:\n🎯 arT\n🔫 KSCERATO\n🧠 yuurih\n🔥 chelo\n⚡ FalleN"
    elif text == '/jogos':
        reply = "Últimos jogos:\n1. FURIA 2x1 NIP\n2. FURIA 1x2 NAVI\n3. FURIA 2x0 MIBR"
    elif text == '/quiz':
        reply = "Qual foi o primeiro campeonato que a FURIA ganhou? 🏆\n(a) CBCS\n(b) ESL Brasil\n(c) DreamHack"
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
    port = int(os.environ.get('PORT', 5000))  # Porta definida pelo Render ou 5000 localmente
    app.run(host='0.0.0.0', port=port)


