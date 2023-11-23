from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

from config import TOKEN_API


dp = Dispatcher()
bot = Bot(TOKEN_API)


async def on_startup():
    print('Стартуем!')


@dp.message(Command(commands='start'))
async def command_start(message: types.Message):
    await message.answer(text='<em>Привет, <b>добро</b> пожаловать!</em>', parse_mode='HTML')


@dp.message(Command(commands='give'))
async def command_give(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEKzhNlX4kc2drn_QAB3OwrdgWqAaZTUZoAAjwgAAIPCGFIouAdASEMUD4zBA')


@dp.message()
async def message_handler(message: types.Message):
    await message.reply(text=message.text + u'\U00002600')


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot, on_startup=on_startup)
    


if __name__ == '__main__':
    asyncio.run(main())
