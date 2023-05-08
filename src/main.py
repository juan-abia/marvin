import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

from extras import start
from gpt import gpt

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

MARVIN_TOKEN = os.getenv('MARVIN_TOKEN')

if __name__ == '__main__':
    application = ApplicationBuilder().token(MARVIN_TOKEN).build()
    
    gpt_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), gpt)

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(gpt_handler)

    application.run_polling()