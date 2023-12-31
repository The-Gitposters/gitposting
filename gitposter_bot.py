"""
THIS IS THE GITPOSTER BOT, the bot that goes gitposting all the time.

Start this bot on a machine with an internet connection.

Please make sure to have a valid TOKEN for your own telegram bot participant
in a system environment variable called BOT_TOKEN.
For more information on how to set up and operate the Gitposter Bot, please
refer to README.md.


Supports the following commands:
/help: Display help text.

/start or /hello: Display an insulting welcome message.
/insult: Trigger the insult generator.
/pep: Trigger the pep talk generator.

Supports the following reactions:
CAPSPAM: Trigger on certain words and repeats them as capitalised one-letter
    messages.
"""

import os
import time

import telebot

import modules.gp_capspam as gp_capspam
import modules.gp_help as gp_help
import modules.gp_insult as gp_insult
import modules.gp_pep as gp_pep
import modules.gp_rant as gp_rant


# create bot with imported token
# BOT_TOKEN is imported from the system environment variables
# TODO: change bot token variable name to GP_BOT_TOKEN
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# [LEGACY] send welcome message 
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """"""
    bot.reply_to(message, "Na du " + gp_insult.be_mean() + "? Heute schon kassiert?")

# help call
@bot.message_handler(commands=['help'])
def call_gp_help(message):
    """"""
    print("help command was issued")
    help_result = gp_help.babysit_these_morons(message)
    bot.send_message(message.chat.id, help_result)

# insult module
@bot.message_handler(commands=['insult'])
def send_insult(message):
    """"""
    bot.send_message(message.chat.id, "Du " + gp_insult.be_mean() + "!")

# Pep talk module
@bot.message_handler(commands=['pep'])
def send_peptalk(message):
    """"""
    bot.send_message(message.chat.id, gp_pep.get_peptalk())

# Rant module
@bot.message_handler(commands=['rant'])
def send_rant(message):
    bot.send_message(message.chat.id, rant_collection.get_rant_message())

# test function for stickers
# @bot.message_handler(commands=['t_sticker'])
# def gp_send_sticker(message):
#     bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEoW6plgto1t_V5gcGgCZtQX1BgkxH7HQACKDkAAqsKSEpQRYmZhRKHxDME')

# capspam call (has to be changed to handle general non-command messages)
@bot.message_handler()
def handle_standard_message(message):
    """"""
    print("Message received!")
    # send capspam if necessary
    capspam_result = gp_capspam.get_capspam_result(message)
    if(capspam_result != ""):
        for character in capspam_result:
            bot.send_message(message.chat.id, character)
            time.sleep(1)


# Initialise additional functions
rant_collection = gp_rant.RantCollection()
rant_collection.read_file(r"resources/gp_res_rants.txt")


# start bot listening
bot.infinity_polling()