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
    import modules.gp_insult as insult
    bot.reply_to(message, "Na du " + insult.be_mean() + "? Heute schon kassiert?")

# insult module
@bot.message_handler(commands=['insult'])
def send_insult(message):
    import modules.gp_insult as insult
    bot.send_message(message.chat.id, "Du " + insult.be_mean() + "!")

# start bot listening
bot.infinity_polling()