import logging
import os
import json
from dotenv import load_dotenv
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

from extra_handlers import start
from langchain_handlers import langchain, reset_chat


class Marvin():
    def __init__(self) -> None:
        load_dotenv()
        self.telegram_token = os.getenv('MARVIN_TOKEN')
        self.application = ApplicationBuilder().token(self.telegram_token).build()

    def add_handlers(self) -> None:
        start_handler = CommandHandler('start', start)
        langchain_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), langchain)
        reset_chat_handler = CommandHandler('reset_chat', reset_chat)

        self.application.add_handler(start_handler)
        self.application.add_handler(langchain_handler)
        self.application.add_handler(reset_chat_handler)

    def run(self) -> None:
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        self.application.run_polling()


if __name__ == '__main__':
    marvin = Marvin()
    marvin.add_handlers()
    marvin.run()