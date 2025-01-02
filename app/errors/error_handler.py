import logging
from aiogram import Dispatcher
from aiogram.types import Update

# Import updated/relocated exception classes
from aiogram.exceptions import TelegramAPIError

try:
    # Attempt to import RetryAfter from its possibly updated location
    from aiogram.client.exceptions import RetryAfter
except ImportError:
    # In case RetryAfter has been removed completely
    RetryAfter = None


async def errors_handler(update: Update, exception: Exception) -> bool:
    """
    Global error handler for aiogram 3.x.
    Logs exceptions based on their type.
    :param update: Incoming update during which the exception occurred.
    :param exception: Exception raised during processing.
    :return: True if the exception was handled, False otherwise.
    """
    if isinstance(exception, TelegramAPIError):  # Handles API-related errors generally
        logging.exception(f"TelegramAPIError: {exception} \nUpdate: {update}")
        return True

    if RetryAfter and isinstance(exception, RetryAfter):  # Handles rate-limiting errors
        logging.exception(f"RetryAfter: {exception} \nUpdate: {update}")
        return True

    # Removed CantParseEntities since it is no longer valid in recent aiogram versions

    # Custom logging for unrecognized exceptions
    logging.exception(f"Unhandled exception: {exception}\nUpdate: {update}")
    return True  # Return True to indicate the exception was handled


def register_error_handler(dp: Dispatcher):
    """
    Register the global error handler with the Dispatcher.
    :param dp: Dispatcher instance
    """
    dp.errors.register(errors_handler)
