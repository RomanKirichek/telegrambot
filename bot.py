import telebot
token='6720448392:AAGmJjOMLIzfy0OlNNJguIvP7LbS1V7NCfQ'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет")
bot.infinity_polling()  