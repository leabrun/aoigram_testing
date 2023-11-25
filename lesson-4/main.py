from aiogram import Bot, Dispatcher, types
from aiogram.methods import DeleteWebhook
from aiogram.filters import Command
import asyncio

from config import TOKEN_API


dp = Dispatcher()
bot = Bot(TOKEN_API)

HELP_COMMAND = """
<b>/help</b> - <em>список команд.</em>
<b>/location</b> - <em>начало нашей работы.</em>
<b>/картинка</b> - <em>генерация картинки.</em>
"""


@dp.message(Command(commands='help'))
async def echo(message: types.Message):
    # await message.answer(message.text)
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='Hello!')
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message(Command(commands='картинка'))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, 
                         photo='https://ornella.club/uploads/posts/2023-02/1676288358_ornella-club-p-samaya-smeshnaya-obezyana-krasivo-66.jpg')
    await message.delete()


@dp.message(Command(commands='location'))
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, 
                            latitude=52,
                            longitude=69)
    await message.delete()


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())
