import telebot
from telebot import types
bot = telebot.TeleBot("6720448392:AAGmJjOMLIzfy0OlNNJguIvP7LbS1V7NCfQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "wassap")




bot.infinity_polling()