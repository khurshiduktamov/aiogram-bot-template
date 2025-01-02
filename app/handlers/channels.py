from aiogram import Router
from aiogram.types import Message

router = Router()  # Create a router for channel-related handlers


@router.message()
async def handle_channel_message(message: Message):
    """
    Placeholder for handling channel-specific messages.
    """
    pass  # No implementation yet


def register_channel_handlers(dp):
    dp.include_router(router)
