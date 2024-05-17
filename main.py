import asyncio
from aiogram import types
from aiogram import Bot, Dispatcher

# связываем код с ботом в телеграме
TOKEN = '6243605704:AAGgzm-snEoUUZzI9-tNqeNJA7NvNiGSdQU'
bot = Bot(token=TOKEN)

# создаем диспетчер для обработки команд
dp = Dispatcher()

from handlers.user_private import user_router
from handlers.user_group import group_router
dp.include_router(user_router)
dp.include_router(group_router)


# функция для старта бота
async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())

