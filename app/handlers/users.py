# users.py: Template for user-specific handlers
from aiogram import Router
from aiogram.types import Message

router = Router()  # Create a router for user-related handlers


@router.message()
async def handle_user_message(message: Message):
    """
    Placeholder for handling user-specific messages or commands.
    """
    pass  # No implementation yet


def register_user_handlers(dp):
    dp.include_router(router)
