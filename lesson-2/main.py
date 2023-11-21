from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

from config import TOKEN_API


HELP_COMMAND = """
/help - список комманд
/start - начать работу с ботом
"""

dp = Dispatcher()


@dp.message(Command('help'))
async def help_message(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message(Command('start'))
async def help_message(message: types.Message):
    await message.answer(text='Добро пожаловать.')
    await message.delete()


async def main():
    bot = Bot(TOKEN_API)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
