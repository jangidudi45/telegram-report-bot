# bot.py - Simple Telegram Bot Example
import os
from telegram.ext import Updater, CommandHandler

# Command handler for /start
def start(update, context):
    update.message.reply_text("✅ Bot is running successfully!")

if __name__ == "__main__":
    # Get bot token from environment variable
    TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

    if TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("⚠ Please set the BOT_TOKEN environment variable!")
        exit(1)

    # Create updater and dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    print("🤖 Bot started...")
    updater.start_polling()
    updater.idle()
