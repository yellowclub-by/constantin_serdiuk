from aiogram import Router, types, F
from aiogram.types import FSInputFile

heroes_router = Router()

@heroes_router.message(F.text.lower() == "ворон")
async def hero_crow(message: types.Message):
    photo = FSInputFile("img/heroes/crow.webp")
    await message.answer_photo(photo, caption="Легендарный боец класса «Убийца».")


@heroes_router.message(F.text.lower() == "леон")
async def hero_leon(message: types.Message):
    photo = FSInputFile("img/heroes/leon.webp")
    await message.answer_photo(photo, caption="Легендарный боец класса «Убийца».")


@heroes_router.message(F.text.lower() == "спайк")
async def hero_leon(message: types.Message):
    photo = FSInputFile("img/heroes/spyke.webp")
    await message.answer_photo(photo, caption="Легендарный боец класса «Убийца».")


@heroes_router.message(F.text.lower() == "сэнди")
async def hero_leon(message: types.Message):
    photo = FSInputFile("img/heroes/sandy.webp")
    await message.answer_photo(photo, caption="Легендарный боец класса «Убийца».")