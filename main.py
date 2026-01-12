from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler, filters)
import os
from dotenv import load_dotenv
load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): # this function will be called when the /start command is issued
    # async def means“This function might take time, don’t freeze everything.”
    await update.message.reply_text("Hello World!") # await means“Wait here until this is done, then move on.”

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()# This is the bot token 

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):#update = what just happened context = extra tools & memory
    text = update.message.text

    if text.lower() == "hi":
        await update.message.reply_text("Wassup")
    elif text.lower() == "hello":
        await update.message.reply_text("Hey there!")
    elif text.lower() == "who made you":
        await update.message.reply_text("I was created by sreevatsa.")
    elif text.lower() == "who made u":
        await update.message.reply_text("I was created by sreevatsa.")
    elif text.lower() == "who made you?":
        await update.message.reply_text("I was created by sreevatsa.")
    elif text.lower() == "who made u?":
        await update.message.reply_text("I was created by sreevatsa.")
    else:
        await update.message.reply_text(text)

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
