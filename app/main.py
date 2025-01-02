import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from app.config import BOT_TOKEN  # Import your BOT_TOKEN from the config
from app.handlers import register_all_handlers
from app.errors import register_error_handlers  # Import the error handler registration

# Configure logging to keep track of the bot's activity
logging.basicConfig(level=logging.INFO)


async def main():
    # Initialize bot and dispatcher
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(storage=MemoryStorage())

    logging.info("Bot is starting...")

    # Register handlers and error handler
    register_all_handlers(dp)
    register_error_handlers(dp)

    # Start polling
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
