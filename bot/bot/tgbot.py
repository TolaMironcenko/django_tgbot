import telebot
from django.core.management.base import BaseCommand
import time
from termcolor import cprint
import django
import os
import sys

# путь до папки с проектом
project_path = os.path.dirname(os.path.abspath('tgbot.py'))
# добавляем его в PATH
sys.path.append(project_path)
# указываем какие настройки django нужно будет использовать
os.environ["DJANGO_SETTINGS_MODULE"] = "bot.settings"
# подключаем django
# django.setup()

from ..tgbot.models import UserInfo

TOKEN = '5123679189:AAHTMxCyOUwPSbaeof31m8SjRHVs4qKZci8'  # testbot

tgbot = telebot.TeleBot(TOKEN)
print('bot started')


@tgbot.message_handler(commands=['start'])
def start(message):
    tgbot.send_message(message.chat.id, 'hello')
    newuser = UserInfo(
                        # Name=message.from_user.first_name,
                        userName=message.from_user.username,
                        userId=message.chat.id
    )
    newuser.save()
    print(message)


try:
    tgbot.polling(none_stop=True)
except Exception as e:
    time.sleep(3)
    cprint(str(e), 'red')
