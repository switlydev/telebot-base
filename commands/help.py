from telebot import types
import os
from dotenv import load_dotenv
from lib.json.JSONHelper import JSONHelper

load_dotenv()

global lang 
lang = JSONHelper.load_language(os.getenv("SelectedLanguage"))

def help_command(bot,message):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(lang["keyboard_button_moderation"],callback_data="moderation")
        btn2 = types.InlineKeyboardButton(lang["keyboard_button_fun"], callback_data="fun")
        btn3 = types.InlineKeyboardButton(lang["keyboard_button_settings"], callback_data="settings")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, lang["help_command_response"], reply_markup=markup)

def callback_handler(bot):
     @bot.callback_query_handler(func=lambda call: True)
     def handle_callback(call):
          if call.data == "moderation":
               bot.send_message(call.message.chat.id,lang["callModeration_response"])
               bot.delete_message(call.message.chat.id,call.message.id)          
          """
          If you want, you can write bot responses here.
          """

def register(bot):
    @bot.message_handler(commands=['help'])
    def handle_help(message):
        help_command(bot,message)
    callback_handler(bot)