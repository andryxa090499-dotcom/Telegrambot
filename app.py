```python
import os
import logging
import re
import random
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

BAD_WORDS = ["блять", "пизда", "хуй", "ебал", "нахер", "гондон", "мудак", "сука", "тварь", "блядь"]
THREAT_MESSAGES = [
    "⚠️ Мат обнаружен! Следующий шаг - звонок твоим родителям!",
    "👀 Я всё вижу! Ещё одно слово - и screenshot полетит в семейный чат!",
    "📞 Твоя мама уже набрала мой номер... Шучу! Пока что...",
    "🚫 Прекрати материться! Или я расскажу всё твоим родителям!"
]

def contains_bad_words(text):
    text = text.lower()
    return any(re.search(rf"\b{word}\b", text) for word in BAD_WORDS)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
        
    if contains_bad_words(update.message.text.lower()):
        threat = random.choice(THREAT_MESSAGES)
        await update.message.reply_text(threat)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    application.run_polling()

if __name__ == "__main__":
    main()
```
