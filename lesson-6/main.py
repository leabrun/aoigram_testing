from aiogram import Bot, Dispatcher, types
from aiogram.methods import DeleteWebhook
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from config import TOKEN_API


dp = Dispatcher()
bot = Bot(TOKEN_API)


@dp.message(Command(commands='help'))
async def help_command(message: types.Message):
    ibuttons = [
        [InlineKeyboardButton(
            text='yandex',
            url='ya.ru'
        )]
    ]
    ikb = InlineKeyboardMarkup(inline_keyboard=ibuttons)
    await message.answer('Hello!', reply_markup=ikb)


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())
