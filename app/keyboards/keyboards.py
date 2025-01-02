"""1. **`keyboards.py`: Modularizing Keyboards**
If you recall, adding custom inline and reply keyboards can help enhance the bot's usability."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_menu_keyboard():
    """
       Generates an inline menu keyboard.
       """
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Option 1", callback_data="opt1"),
        InlineKeyboardButton(text="Option 2", callback_data="opt2"),
        InlineKeyboardButton(text="Cancel", callback_data="cancel")
    ]
    keyboard.add(*buttons)
    return keyboard
