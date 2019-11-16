import telebot


access_token = '689014667:AAEbrpA84JGFiy8z47-G0RWgHJJkEHN-bls'
# telebot.apihelper.proxy = {'https': 'https://69.15.2.22:8080'}
bot = telebot.TeleBot(access_token)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
