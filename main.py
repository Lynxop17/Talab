from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import re
import logging

# Logging for debug (optional)
logging.basicConfig(level=logging.INFO)

# Replace this with your actual bot token
API_TOKEN = '8018321967:AAH4pvJSUKzYyUvVtBrcEXjRtd9SL7vA5ig'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    # Find all Telegram t.me links
    matches = re.findall(r'https?://t\.me/([\w\d_]+)', message.text)
    
    if matches:
        # Create response: @username for each link
        response = '\n'.join([f"@{username}" for username in matches])
        await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
  
