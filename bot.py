import telebot
from telebot import types


bot = telebot.TeleBot('6720448392:AAGmJjOMLIzfy0OlNNJguIvP7LbS1V7NCfQ')

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a custom keyboard with buttons
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Button 1')
    button2 = types.KeyboardButton('Button 2')
    button3 = types.KeyboardButton('Button 3')
    keyboard.add(button1, button2, button3)

    # Send a welcome message with the custom keyboard
    bot.reply_to(message, "Welcome to the bot! Please select an option:", reply_markup=keyboard)

# Start the bot
bot.polling()