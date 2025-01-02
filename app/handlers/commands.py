from aiogram import types, Dispatcher
from aiogram.filters import Command  # Import the Command filter


# The start command
async def start_command(message: types.Message):
    await message.answer("Welcome! This is a scalable bot template built with aiogram 3.16+")


# The help command
async def help_command(message: types.Message):
    await message.answer("Here is how I can help you:\n\n/start - Start the bot\n/help - Get help")


# Function to register the handlers properly
def register_command_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=["start"]))  # Apply the Command filter
    dp.message.register(help_command, Command(commands=["help"]))  # Apply the Command filter
