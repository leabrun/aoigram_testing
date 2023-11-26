from aiogram import Bot, Dispatcher, types
from aiogram.methods import DeleteWebhook
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio

from config import TOKEN_API


dp = Dispatcher()
bot = Bot(TOKEN_API)

HELP_COMMAND = """
<b>/start</b> - <em>запуск бота.</em>
<b>/help</b> - <em>список команд.</em>
<b>/location</b> - <em>начало нашей работы.</em>
<b>/photo</b> - <em>отправка картинки.</em>
"""


@dp.message(Command(commands='help'))
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML',
                           reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message(Command(commands='start'))
async def start_command(message: types.Message):
    buttons = [
        [KeyboardButton(text='/help')]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать в бота.',
                           parse_mode='HTML',
                           reply_markup=keyboard)


@dp.message(Command(commands='description'))
async def desc_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='держите описание',
                           parse_mode='HTML')
    await message.delete()


@dp.message(Command(commands='photo'))
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://ornella.club/uploads/posts/2023-02/1676288358_ornella-club-p-samaya-smeshnaya-obezyana-krasivo-66.jpg',)
    await message.delete()


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())
