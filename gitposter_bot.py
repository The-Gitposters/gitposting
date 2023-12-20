# get BOT_TOKEN as environment variable
import os
# telegram bot library
import telebot

# create bot with imported token
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


# [LEGACY] send welcome message 
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    import modules.gp_offend as offend
    bot.reply_to(message, "Na du " + offend.be_mean() + "? Heute schon kassiert?")

# offend module
@bot.message_handler(commands=['offend'])
def send_offense(message):
    import modules.gp_offend as offend
    bot.send_message(message.chat.id, "Du " + offend.be_mean() + "!")

# start bot listening
bot.infinity_polling()