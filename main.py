import asyncio
from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

# связываем код с ботом в телеграме
bot = Bot(token='6243605704:AAGgzm-snEoUUZzI9-tNqeNJA7NvNiGSdQU')

# создаем диспетчер для обработки команд
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет! Это бот про персонажей Brawl Stars!")


@dp.message()
async def echo(message: types.Message):
    await message.answer("Бот находится в разработке.\nПока он может только повторять за тобой.")
    user_text = message.text
    await message.answer(user_text)


# функция для старта бота
async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())

