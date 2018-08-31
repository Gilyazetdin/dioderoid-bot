import requests
import datetime
import sys


class Bot:
    api_url = None


    def __init__(self, token):
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def getUpdates(self, offset=None, timeout=30):
         return requests.get(
             self.api_url + 'getUpdates',
             {'timeout': timeout, 'offset': offset}
        ).json()['result']

    def sendMessage(self, chat_id, text):
        return requests.post(self.api_url +'sendMessage', {'chat_id': chat_id, 'text': text})

    def getLastUpdate(self):
        result = self.getUpdates()

        if len(result) > 0:
            last_update = result[-1]
        else:
            last_update = result[0]

        return last_update

bot = Bot(sys.argv[1])


while True:
    new_offset = None
    bot.getUpdates(offset=new_offset)

    last_update = bot.getLastUpdate()

    update_id = last_update['update_id']
    chat_text = last_update['message']['text']
    chat_id = last_update['message']['chat']['id']
    chat_name = last_update['message']['chat']['first_name']

    if chat_text == "Hello!":
        bot.sendMessage(chat_id, "sosi")

    new_offset = update_id + 1
