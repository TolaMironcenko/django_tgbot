"""
WSGI config for bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
# import threading
# import time
# from termcolor import cprint


# def startbot():
    # need_dir = '/Users/anatolijmironcenko/Documents/django_telegram_bot/bot/bot/'
    # os.system("python " + need_dir + "tgbot.py")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.settings')

application = get_wsgi_application()

# try:
#     threading.Thread(target=startbot).start()
# except Exception as e:
#     time.sleep(3)
#     cprint(str(e), 'red')
