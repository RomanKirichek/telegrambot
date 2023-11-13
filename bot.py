import telebot
from telebot import types
bot = telebot.TeleBot("6720448392:AAGmJjOMLIzfy0OlNNJguIvP7LbS1V7NCfQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "wassap")

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)


bot.infinity_polling()