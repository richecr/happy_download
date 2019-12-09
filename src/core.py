from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram.ext.dispatcher import run_async
import os

from config.settings import TELEGRAM_TOKEN

from utils import download_video, ydl_opts, tratar_url


def start(update, context):
    response_message = "Olá, queridx! Use o comando para nos enviar a URL do vídeo.\n"
    response_message += "Exemplo: /video <link>"
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

@run_async
def unknown(update, context):
    text = update['message']['text']
    if "/video" in text:
        download(text, context, update)
    else:
        response_message = "Comando inválido. Digite /start e veja como baixar um vídeo."
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

def download(text, context, update):
    url = text.split("/video ")[1]
    url = tratar_url(url)
    filename = download_video(url)
    try:
        context.bot.send_video(
            chat_id=update.message.chat_id,
            video=open(filename, 'rb'),
            timeout=100
        )
        os.remove(filename)
    except Exception as e:
        print(e)
        pass

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()