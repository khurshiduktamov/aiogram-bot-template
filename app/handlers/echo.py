from aiogram import types, Dispatcher


async def echo_handler(message: types.Message):
    await message.answer(f"You said: {message.text}")


def register_echo_handler(dp: Dispatcher):
    dp.message.register(echo_handler)
