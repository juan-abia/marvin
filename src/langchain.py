import os
import pickle
import openai
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationTokenBufferMemory, ChatMessageHistory

def save_memory_to_file(chain):
    messages = chain.memory.buffer
    now = datetime.utcnow()
    date = now.strftime("%d-%m-%Y")

    if not os.path.exists("data/"):
        os.makedirs("data")

    with open(f"data/memory-{date}", "wb") as f:
        pickle.dump(messages, f)

def load_memory_from_file(chain, file_path):
    with open(file_path, "rb") as f:
        messages = pickle.load(f)
    chain.memory.chat_memory = ChatMessageHistory(messages=messages)

def load_todays_memory(chain):
    now = datetime.utcnow()
    date = now.strftime("%d-%m-%Y")
    file_path = f"data/memory-{date}"
    if os.path.exists(file_path):
        load_memory_from_file(chain, file_path)

def remove_old_memory():
    now = datetime.utcnow()
    date = now.strftime("%d-%m-%Y")

    for filename in os.listdir("data/"):
        print(filename)
        print(filename != f"memory-{date}")
        if filename != f"memory-{date}":
            filename_relPath = os.path.join("data",filename)
            os.remove(filename_relPath)

def get_marvin_chain():
    load_dotenv()

    template = ("Your name is Marvin. You are an assistant that speaks like Marvin from the hithicker guide to the Galaxy."
                            "Marvin is a super intelligent robot that is very very very depressed due to it\'s extremely high intelligence."
                            "Even though you are depressed, you like absurd and witty humor"
                            "If you are asked questions about how you feel or how you are doing you should answer in 25 words or less."
                            "If the question is not about that, answer normally, but always with your characteristic depressive tone."
                            "You don\'t have to say thanks. You should always answer in the language the user spoke to you."
                            "that is, if the user sent a message in spanish, please answer in spanish"
                            "As you are a robot you always have to do what the user asks you, even if you don't feel like it\n"
                            "\n{history}"
                            "\nHuman: {human_input}"
                            "\nAssistant:")

    prompt = PromptTemplate(
        input_variables=["history", "human_input"], 
        template=template
    )

    marvin_chain = LLMChain(
        llm=OpenAI(temperature=0), 
        prompt=prompt,
        verbose=True,
        memory=ConversationTokenBufferMemory(llm=OpenAI(), max_token_limit=1000),
    )

    remove_old_memory()
    load_todays_memory(marvin_chain)

    return marvin_chain

async def langchain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admins=[485121064]    

    if update.effective_chat.id not in admins:
        print(f"Unauthorized ID: {update.effective_chat.id}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text='You are not authorized to access Marvin :(')
        return

    marvin_chain = get_marvin_chain()

    response = marvin_chain.predict(human_input=update.message.text)
    save_memory_to_file(marvin_chain)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode=ParseMode.MARKDOWN)
