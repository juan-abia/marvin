import random
from telegram import Update
from telegram.ext import ContextTypes

marvin_sentences = ["Life? Don't talk to me about life.",
                    "Here I am, brain the size of a planet, and they tell me to take you up to the bridge. Call that job satisfaction? 'Cos I don't.",
                    "I think you ought to know I'm feeling very depressed.",
                    "Pardon me for breathing, which I never do anyway so I don't know why I bother to say it, Oh God, I'm so depressed.",
                    "There's only one life-form as intelligent as me within thirty parsecs of here and that's me.",
                    "I wish you'd just tell me rather trying to engage my enthusiasm because I haven't got one.",
                    "And then, of course, I've got this terrible pain in all the diodes down my left side."]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(marvin_sentences))
