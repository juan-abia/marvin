import logging
import os
from dotenv import load_dotenv
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

from extras import start
from langchain import langchain

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
MARVIN_TOKEN = os.getenv('MARVIN_TOKEN')

if __name__ == '__main__':
    application = ApplicationBuilder().token(MARVIN_TOKEN).build()
    
    langchain_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), langchain)
    start_handler = CommandHandler('start', start)
    
    application.add_handler(start_handler)
    application.add_handler(langchain_handler)

    application.run_polling()