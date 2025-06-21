import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot is live and working! Type /help to see available commands.")

# /help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Available commands:\n"
        "/start - Check if bot is running\n"
        "/help - Show this help message"
    )

# Main block
if __name__ == '__main__':
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # Make sure to set this in Render environment
    if not BOT_TOKEN:
        raise Exception("❌ BOT_TOKEN not found in environment variables.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot started... waiting for commands.")
    app.run_polling()
