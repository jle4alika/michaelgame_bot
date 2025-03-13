from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Украсть шишки 🌰'),
        KeyboardButton(text='Рыбацкая бухта ⚓')
    ],
    [
         KeyboardButton(text='Профиль 👨‍💼'),
         KeyboardButton(text='Кланы 🛡️'),
         KeyboardButton(text='Реферальная программа ✌️')
    ],
    [
        KeyboardButton(text='Обменник 🤝'),
        KeyboardButton(text='Магазин улучшений 🛒'),
        KeyboardButton(text='Топ игроков 🔥')
    ]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...',
                           one_time_keyboard=True
)