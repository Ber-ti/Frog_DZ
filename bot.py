from telegram import Update


# Твой ID
YOUR_TELEGRAM_ID = 1410672904

async def start(update: Update, context) -> None:
    await update.message.reply_text("Привет! Отправь мне сообщение, и я пересылаю его тебе.")

async def forward_to_me(update: Update, context) -> None:
    user = update.message.from_user
    text = update.message.text
    chat_id = update.message.chat_id

    message_to_send = f"Новое сообщение от @{user.username} (ID: {chat_id}):\n{text}"

    await context.bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=message_to_send)

