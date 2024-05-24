from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = KeyboardButton(text="Назад")

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Герои"),
            KeyboardButton(text="Об игре")
        ],
        [
            KeyboardButton(text="Режимы"),
            KeyboardButton(text="Карты")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите необходимый пункт в меню ниже."
)

heroes_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ворон"),
            KeyboardButton(text="Леон")
        ],
        [
            KeyboardButton(text="Спайк"),
            KeyboardButton(text="Сэнди")
        ],
        [
            back_btn
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите персонажа в меню ниже."
)

game_modes_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Захват кристаллов")
        ],
        [
            KeyboardButton(text="Броубол")
        ],
        [
            KeyboardButton(text="Одиночное столкновение")
        ],
        [
            KeyboardButton(text="Парное столкновение")
        ],
        [
            back_btn
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите режим в меню ниже."
)

maps_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подрыв"),
            KeyboardButton(text="Штольня")
        ],
        [
            KeyboardButton(text="В центре внимания"),
        ],
        [
            KeyboardButton(text="Муравьиные бега"),
        ],
        [
            back_btn
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите карту в меню ниже."
)
