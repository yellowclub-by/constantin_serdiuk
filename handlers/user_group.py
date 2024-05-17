from aiogram import Router, types, F

# Создаем роутер
group_router = Router()


# Создаем список запрещены
restricted_words = ["нуб", "оранжевый", "класс"]

# Делаем функцию, которая будет фильтровать сообщения
@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(" ")
    for word in words_lst:
        if word.lower() in restricted_words:
            await message.answer(f"{message.from_user.first_name}, ваше сообщение удалено. Соблюдайте правила чата.")
            await message.delete()
            break

    # for word in restricted_words:
    #     if word in message.text:
    #         await message.answer(f"{message.from_user.first_name}, ваше сообщение удалено. Соблюдайте правила чата.")
    #         await message.delete()
    #         break
