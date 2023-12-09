from aiogram import Bot, Dispatcher, types
from aiogram.methods import DeleteWebhook
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import asyncio

from config import TOKEN_API


dp = Dispatcher()
bot = Bot(TOKEN_API)

buttons = [
    [KeyboardButton(text='/help')],
    [KeyboardButton(text='/vote')]
]
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         keyboard=buttons
                        )


@dp.message(Command(commands='start'))
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to our bot',
                           reply_markup=kb)


@dp.message(Command(commands='vote'))
async def vote_command(message: types.Message):
    ibuttons = [
        [InlineKeyboardButton(text='❤️',
                              callback_data='like')],
        [InlineKeyboardButton(text='👎',
                              callback_data='dislike')],
        [InlineKeyboardButton(text='Главное меню',
                              callback_data='main')]
    ]
    ikb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=ibuttons)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://sportishka.com/uploads/posts/2022-02/1645539870_38-sportishka-com-p-peizazh-gori-turizm-krasivo-foto-63.jpg",
                         caption='Do you like this photo?',
                         reply_markup=ikb)


@dp.callback_query()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='You like it')
    elif callback.data == 'dislike':
        await callback.answer(text='You didn\'t like it')
    elif callback.data == 'main':
        await callback.message.answer(text='Welcome to main menu!',
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())
