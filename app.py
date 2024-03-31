import os
import logging

from telegram import Update
from telegram.ext import Updater, filters, CallbackContext
from telegram.ext import MessageHandler, CommandHandler, InlineQueryHandler, CallbackQueryHandler


logging.basicConfig(level=logging.DEBUG)


def message_handler(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.message.chat.id, text=update.message.text)


updater = Updater(os.environ["6237216171:AAEM1ePcq957iiJ5zpZ2FjjWAeiKO3yVFYM"])
updater.dispatcher.add_handler(MessageHandler(
    filters=filters.text, callback=message_handler))


if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
    updater.stop()
