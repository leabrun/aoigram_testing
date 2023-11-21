from aiogram import Bot, Dispatcher, types
import asyncio


TOKEN_API = "6394953027:AAEJjvY_ZWYt29l0u-GoRCohJb1r9QSgieQ"

dp = Dispatcher()


@dp.message()
async def echo_upper(message: types.Message):
    if message.text.count(' ') >= 1:
        print(message.text.count(' '))
        await message.answer(text=message.text.upper())


async def main():
    bot = Bot(TOKEN_API)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
