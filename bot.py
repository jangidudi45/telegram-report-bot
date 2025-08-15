# bot.py
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Environment variable se token lena

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is running successfully!\n\n"
                                    "Available commands:\n"
                                    "/report - Report a single target\n"
                                    "/ro - Alias for /report\n"
                                    "/massreport - Report multiple targets")

# /report command
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a username, link, or ID to report.\nExample: /report @username")
        return
    target = " ".join(context.args)
    # Here you would put the report logic
    await update.message.reply_text(f"📢 Reporting target: {target}")

# /ro command (alias for /report)
async def ro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await report(update, context)

# /massreport command
async def massreport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide multiple usernames, links, or IDs separated by spaces.\nExample: /massreport @user1 @user2")
        return
    targets = context.args
    for target in targets:
        # Here you would put the report logic
        await update.message.reply_text(f"📢 Reporting target: {target}")
    await update.message.reply_text("✅ Mass reporting completed.")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", report))
    app.add_handler(CommandHandler("ro", ro))
    app.add_handler(CommandHandler("massreport", massreport))

    print("🤖 Bot started...")
    app.run_polling()
