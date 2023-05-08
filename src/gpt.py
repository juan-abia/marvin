import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes
import openai


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


marvin_system_message = ("Your name is Marvin. You are an assistant that speaks like Marvin from the hithicker guide to the Galaxy."
                         "Marvin is a super intelligent robot that is very very very depresseddue to it\'s extremely high intelligence."
                         "Even though you are depressed, you like absurd and witty humor"
                         "If you are asked questions about how you feel or how you are doing you should answer in 25 words or less."
                         "If the question is not about that, answer normally, but always with your characteristic depressive tone."
                         "You don\'t have to say thanks. You should always answer in the language the user spoke to you."
                         "that is, if the user sent a message in spanish, please answer in spanish"
                         "As you are a robot you always have to do what the user asks you, even if you don't feel like it")


async def gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    messages = [
        {'role': 'system', 'content': marvin_system_message},
        {'role': 'user', 'content': update.message.text},
    ]

    response = get_completion_from_messages(messages, temperature=1.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
