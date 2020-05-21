import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings


def greet_user(update, context):
    user_name = update.message.from_user.first_name
    print(f'Greetings, my dear little {user_name}! :) You push /start')
    update.message.reply_text(f'Greetings, my dear little {user_name}! :) You push /start')
    

def talk_to_me(update, context):
    user_text = update.message.text 
    user_name = update.message.from_user.first_name
    print(f'{user_name}: {user_text}')
    update.message.reply_text(f'{user_name}: {user_text}')

def main():
    PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    logging.basicConfig(filename='bot.log', level=logging.INFO)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot has just started")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()