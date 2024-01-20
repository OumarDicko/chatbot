from flask import Flask, request, jsonify
from ultrabot import ultraChatBot
import json
import os

app = Flask(__name__)
historique = []
@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = ultraChatBot(request.json)
        reponseBot,inputuser =bot.Processingـincomingـmessages(historique)
        historique.append(inputuser)
        historique.append(reponseBot)
        return reponseBot

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
