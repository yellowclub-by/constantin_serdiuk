from aiogram import Router, types
from aiogram.filters import CommandStart, Command

# создаем роутер
user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет! Это бот про персонажей Brawl Stars!")

@user_router.message(Command("heroes"))
async def heroes(message: types.Message):
    await message.answer("Здесь вы найдете список всех персонажей Brawl Stars!")

@user_router.message(Command("game"))
async def game(message: types.Message):
    await message.answer("Brawl Stars - это игра для мобильных устройств в жанрах MOBA и геройский шутер, разработанная и изданная финской компанией Supercell.")

@user_router.message(Command("game_modes"))
async def game_modes(message: types.Message):
    await message.answer("В игре есть несколько режимов сражений.")

@user_router.message(Command("maps"))
async def maps(message: types.Message):
    await message.answer("В игре много карт, которые меняются каждые 24 часа.")

@user_router.message()
async def echo(message: types.Message):
    await message.answer("Бот находится в разработке.\nПока он может только повторять за тобой.")
    user_text = message.text
    await message.answer(user_text)

