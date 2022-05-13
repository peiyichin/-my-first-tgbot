from telegram import Update
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters
)
import logging

API_KEY = '5347382763:AAGtVCjHIDEtNfkz7X2zm1AAAhQsQHjV8eQ'

updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Start commands
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello')

# Help command
def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Type me anything')

# Message handler
def echo(update: Update, context: CallbackContext):
    for message in update.message.text.split():
        if message.lower() in STRING:
            update.message.reply_text("Hello, nice to meet you.")
            return
    update.message.reply_text(f"What's mean by {update.message.text}")

# Set up the commands
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(echo_handler)

# Run and stop bot
updater.start_polling()

updater.idle()