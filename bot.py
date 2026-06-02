from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = ""


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document

    if not document.file_name.lower().endswith(".txt"):
        await update.message.reply_text("Please send a .txt file.")
        return

    file = await document.get_file()
    await file.download_to_drive("temp.txt")

    with open("temp.txt", "r", encoding="utf-8") as f:
        content = f.read()

    for i in range(0, len(content), 4000):
        await update.message.reply_text(content[i:i+4000])


app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

print("Bot is running...")
app.run_polling()
