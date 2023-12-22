"""

"""

# get BOT_TOKEN as environment variable
import os
# telegram bot library
import telebot
# time for delays etc
import time


import modules.gp_capspam as gp_capspam
import modules.gp_insult as gp_insult

# create bot with imported token
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


# [LEGACY] send welcome message 
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Na du " + gp_insult.be_mean() + "? Heute schon kassiert?")

# insult module
@bot.message_handler(commands=['insult'])
def send_insult(message):
    bot.send_message(message.chat.id, "Du " + gp_insult.be_mean() + "!")

# test function for stickers
@bot.message_handler(commands=['t_sticker'])
def gp_send_sticker(message):
    bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEoW6plgto1t_V5gcGgCZtQX1BgkxH7HQACKDkAAqsKSEpQRYmZhRKHxDME')


# capspam call
@bot.message_handler()
def call_gp_capspam(*messages):
    for message in messages:
        print(message.text)
        capspam_result = gp_capspam.get_capspam_result(message)
        if(capspam_result != ""):
            for character in capspam_result:
                bot.send_message(message.chat.id, character)
                time.sleep(1000)


# start bot listening
bot.infinity_polling()