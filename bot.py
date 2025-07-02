import telebot
from telebot import types
import dotenv,os
import pyfiglet
import importlib
from lib.json.JSONHelper import JSONHelper
from handlers import NewMemberHandler
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN, threaded=True)
os.system("clear")

base_dir = "commands"
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".py") and not file.startswith("__"):
            module_path = os.path.join(root, file).replace("/", ".").replace("\\", ".")
            module_name = module_path[:-3] 

            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "register"):
                    module.register(bot)
            except Exception as e:
                print(f"{module_name} modülü yüklenemedi: {e}")
NewMemberHandler.register(bot)

lang = JSONHelper.load_language(os.getenv("SelectedLanguage"))

try:
    ascii_art = pyfiglet.figlet_format("@"+bot.get_me().username,font="doom")
    print(ascii_art)
    print(lang["bot_started"])
    bot.infinity_polling()
except KeyboardInterrupt:
    bot.stop_bot()
    print("\n"+ lang["bot_stopped"])
