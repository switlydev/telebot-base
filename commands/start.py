import telebot
from telebot import types
from lib.json.JSONHelper import JSONHelper
from dotenv import load_dotenv
import os

load_dotenv()

def start(bot,message):
        lang = JSONHelper.load_language(os.getenv("SelectedLanguage"))
        bot.reply_to(message, lang["start_command_response"].format(username=message.from_user.username, botUsername=bot.get_me().username))

def register(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
         start(bot,message)
