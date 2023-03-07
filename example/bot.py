from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from .transcriber import youtube_transcribe
from os import getenv

# Define a few command handlers.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(text="hello world!")
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(text="help me!")
async def transcript(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.message.text.split(" ")[1]
    srt = youtube_transcribe(id)
    await update.message.reply_text(text=srt)

async def bot_tele(text):
    # Create application
    application = (
        Application.builder().token(getenv("TOKEN")).build()
    )

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("transcript", transcript))

    # Start application
    await application.bot.set_webhook(url=getenv("webhook"))
    await application.update_queue.put(
            Update.de_json(data=text, bot=application.bot)
        )
    async with application:
        await application.start()
        await application.stop()