from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import re
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Bot token from BotFather
API_TOKEN = '8018321967:AAH4pvJSUKzYyUvVtBrcEXjRtd9SL7vA5ig'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("👋 Hello! I'm your link scanner bot.\nSend a Telegram link and I'll convert it to @username.")

# Help command
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(
        "📌 *Available Commands:*\n"
        "/start - Start the bot\n"
        "/help - Show help message\n"
        "/about - About this bot\n\n"
        "Just send any t.me link and I'll convert it to @username.",
        parse_mode='Markdown'
    )

# About command
@dp.message_handler(commands=['about'])
async def about_command(message: types.Message):
    await message.reply("🤖 *Bot by Jeesi*\nThis bot detects Telegram links and replies with @username.\nMade with ❤ using Python & aiogram.", parse_mode='Markdown')

# Auto detect t.me links
@dp.message_handler()
async def handle_message(message: types.Message):
    matches = re.findall(r'https?://t\.me/([\w\d_]+)', message.text)
    if matches:
        response = '\n'.join([f"@{username}" for username in matches])
        await message.reply(response)

# Start polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
