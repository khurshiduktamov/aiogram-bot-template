from aiogram import Dispatcher
from .commands import register_command_handlers
from .echo import register_echo_handler
from .groups import register_group_handlers
from .channels import register_channel_handlers
from .users import register_user_handlers


def register_all_handlers(dp: Dispatcher):
    """
    Register all handlers from different files.
    """
    register_command_handlers(dp)  # Commands like /start, /help
    register_group_handlers(dp)  # Group-specific functionality
    register_channel_handlers(dp)  # Channel-specific functionality
    register_user_handlers(dp)  # User-specific interactions
    register_echo_handler(dp)  # Fallback for unhandled messages
