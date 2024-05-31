from aiogram import Router, types, F
from aiogram.types import FSInputFile

maps_router = Router()


@maps_router.message(F.text.lower() == "подрыв")
async def map_undermine(message: types.Message):
    photo = FSInputFile("img/maps/undermine.webp")
    await message.answer_photo(photo,
                               caption="Подрыв (англ. Undermine) — официальная карта для события Захват кристаллов.")


@maps_router.message(F.text.lower() == "штольня")
async def map_cavern_churn(message: types.Message):
    photo = FSInputFile("img/maps/cavern_churn.webp")
    await message.answer_photo(photo,
                               caption="Штольня (англ. Cavern Churn) — официальная карта для события Столкновение. Также являлась одной из самых старых карт в игре.")


@maps_router.message(F.text.lower() == "в центре внимания")
async def map_center_stage(message: types.Message):
    photo = FSInputFile("img/maps/center_stage.webp")
    await message.answer_photo(photo,
                               caption="В центре внимания (англ. Center Stage) - это карта сообщества для события Броулбол.")


@maps_router.message(F.text.lower() == "муравьиные бега")
async def map_dueling_beetles(message: types.Message):
    photo = FSInputFile("img/maps/dueling_beetles.webp")
    await message.answer_photo(photo,
                               caption="Муравьиные бега (англ. Dueling Beetles) - официальная карта события Горячая зона.")
