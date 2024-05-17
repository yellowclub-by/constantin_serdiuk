from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command


# создаем роутер
user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет! Это бот про персонажей Brawl Stars!")


@user_router.message(Command("heroes"))
@user_router.message(F.text.lower() == "герои")
async def heroes(message: types.Message):
    await message.answer("Здесь вы найдете список всех персонажей Brawl Stars!")


@user_router.message(Command("game"))
@user_router.message(F.text.lower() == "об игре")
async def game(message: types.Message):
    await message.answer(
        "Brawl Stars - это игра для мобильных устройств в жанрах MOBA и геройский шутер, разработанная и изданная финской компанией Supercell.")


@user_router.message(Command("game_modes"))
@user_router.message(F.text.lower() == "режимы")
async def game_modes(message: types.Message):
    await message.answer("В игре есть несколько режимов сражений.")


@user_router.message(Command("maps"))
@user_router.message(F.text.lower() == "карты")
async def maps(message: types.Message):
    await message.answer("В игре много карт, которые меняются каждые 24 часа.")


# @user_router.message(F.text)                                                # фильтр текста
# @user_router.message(F.photo)                                             # фильтр текста
# @user_router.message(F.text.lower() == "доставка")                        # фильтр конкретного текста
# @user_router.message(F.text.lower().contains("доставк"))                  # фильтр по содержанию
# @user_router.message(F.text.lower().endswith("?"))                        # фильтр начинается с или заканчивается на
# @user_router.message(F.text.lower().startswith("как"), F.text.lower().endswith("?"))                   # фильтр И
# @user_router.message( (F.text.lower().contains("цен") ) | (F.text.lower().contains("стоимост") ) )      # фильтр ИЛИ
async def echo(message: types.Message):
    await message.answer("Сработал магический фильтр.")


