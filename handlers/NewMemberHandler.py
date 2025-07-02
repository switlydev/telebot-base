from dotenv import load_dotenv
import os
from lib.json.JSONHelper import JSONHelper
load_dotenv()
def register(bot):
    @bot.message_handler(content_types=['new_chat_members'])
    def greet_new_members(message):
        lang = JSONHelper.load_language(os.getenv("SelectedLanguage"))
        for new_member in message.new_chat_members:
            #new_member.username
            if new_member.id == bot.get_me().id:
                bot.send_message(message.chat.id, lang["bot_joins_to_group"]).format(group_name = message.chat.title)
            else:
                bot.send_message(message.chat.id,lang["new_member_greeting_response"].format(username = new_member.username,group_name = message.chat.title))

