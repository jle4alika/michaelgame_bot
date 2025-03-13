from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Подписаться на тг канал бота', url='https://t.me/michaelgametex')
        ]
    ]
)


steal = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Попробовать ещё раз 🌰', callback_data='Украсть шишки 🌰')
        ],
        [
            InlineKeyboardButton(text='Магазин улучшений 🛒', callback_data='Магазин улучшений 🛒')
        ],
        [
            InlineKeyboardButton(text='Обменник 🤝', callback_data='Обменник 🤝')
        ],
        [
            InlineKeyboardButton(text='Профиль 👨‍💼‍', callback_data='Профиль 👨‍💼'),
            InlineKeyboardButton(text='Реферальная программа ✌️‍', callback_data='Реферальная программа ✌️'),
        ]
    ]
)

profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Изменить фото профиля 🖼', callback_data='Изменить фото профиля 🖼')
        ],
        [
            InlineKeyboardButton(text='Изменить никнейм 😎', callback_data='Изменить никнейм 😎')
        ],
        [
            InlineKeyboardButton(text='Реферальная программа ✌️', callback_data='Реферальная программа ✌️')
        ],
        [
            InlineKeyboardButton(text='Украсть шишки 🌰', callback_data='Украсть шишки 🌰')
        ],
        [
            InlineKeyboardButton(text='Топ игроков 🔥‍', callback_data='Топ игроков 🔥'),
            InlineKeyboardButton(text='Магазин улучшений 🛒', callback_data='Магазин улучшений 🛒'),
            InlineKeyboardButton(text='Обменник 🤝', callback_data='Обменник 🤝')
        ],
        [
            InlineKeyboardButton(text='Подписаться на тг канал бота', url='https://t.me/michaelgametex')
        ],
    ]
)

exchanger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Украсть шишки 🌰', callback_data='Украсть шишки 🌰'),
            InlineKeyboardButton(text='Профиль 👨‍💼‍', callback_data='Профиль 👨‍💼')
        ],
        [
            InlineKeyboardButton(text='Реферальная программа ✌️‍', callback_data='Реферальная программа ✌️')
        ]
    ]
)

top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Украсть шишки 🌰', callback_data='Украсть шишки 🌰')
        ],
        [
            InlineKeyboardButton(text='Профиль 👨‍💼‍', callback_data='Профиль 👨‍💼'),
            InlineKeyboardButton(text='Магазин улучшений 🛒', callback_data='Магазин улучшений 🛒'),
            InlineKeyboardButton(text='Обменник 🤝', callback_data='Обменник 🤝')
        ]
    ]
)

upgrades = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1️⃣', callback_data='1'),
            InlineKeyboardButton(text='2️⃣', callback_data='2'),
            InlineKeyboardButton(text='3️⃣', callback_data='3')
        ],
        [
            InlineKeyboardButton(text='4️⃣', callback_data='4')
        ],
        [
            InlineKeyboardButton(text='5️⃣', callback_data='5'),
            InlineKeyboardButton(text='6️⃣', callback_data='6')
        ],
        [
            InlineKeyboardButton(text='Меню', callback_data='Меню')
        ],
        [
            InlineKeyboardButton(text='Украсть шишки 🌰', callback_data='Украсть шишки 🌰')
        ],
        [
            InlineKeyboardButton(text='Профиль 👨‍💼‍', callback_data='Профиль 👨‍💼')
        ],
        [
            InlineKeyboardButton(text='Реферальная программа ✌️', callback_data='Реферальная программа ✌️')
        ],
        [
            InlineKeyboardButton(text='Обменник 🤝', callback_data='Обменник 🤝'),
            InlineKeyboardButton(text='Магазин улучшений 🛒', callback_data='Магазин улучшений 🛒')
        ]
    ]
)

choose_top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💸', callback_data='💸')
        ],
        [
            InlineKeyboardButton(text='🐟', callback_data='🐟'),
        ],
        [
            InlineKeyboardButton(text='🔥‍', callback_data='🔥'),
        ],
        [
            InlineKeyboardButton(text='👨‍💼‍', callback_data='👨‍💼'),
        ]
    ]
)

clan_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Создание клана', callback_data='Создать клан')
        ],
        [
            InlineKeyboardButton(text='Вступить в открытый клан', callback_data='Вступить в открытый клан')
        ],
        [
            InlineKeyboardButton(text='Вступить по коду', callback_data='Вступить по коду')
        ]
    ]
)

clan_delete = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='Удалить')
        ],
        [
            InlineKeyboardButton(text='Нет', callback_data='Не удалять')
        ]
    ]
)

clan_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пополнить казну', callback_data='Пополнить казну')
        ],
        [
            InlineKeyboardButton(text='Выйти из клана', callback_data='Выйти из клана')
        ],
    ]
)

clan_owner = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пополнить казну', callback_data='Пополнить казну'),
            InlineKeyboardButton(text='Улучшения', callback_data='Улучшения')
        ],
        [
            InlineKeyboardButton(text='Тип клана', callback_data='Тип клана'),
            InlineKeyboardButton(text='Заявки', callback_data='Заявки'),
            InlineKeyboardButton(text='Изгнать из клана', callback_data='Изгнать из клана'),
        ],
        [
            InlineKeyboardButton(text='Изменить название клана', callback_data='Изменить название клана'),
            InlineKeyboardButton(text='Изменить фото клана', callback_data='Изменить фото клана'),
        ],
        [
            InlineKeyboardButton(text='Удалить клан', callback_data='Удалить клан')
        ],
    ]
)

clan_type_change = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Открытый', callback_data='open'),
            InlineKeyboardButton(text='Приватный', callback_data='private')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='type_back')
        ]
    ]
)

clan_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Изменить тип клана', callback_data='change_type')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='type_back')
        ]
    ]
)

clan_upgrades = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='РУЛЕТКА', callback_data='РУЛЕТКА')
        ],
        [
            InlineKeyboardButton(text='мини-шишка', callback_data='мини-шишка'),
            InlineKeyboardButton(text='мини-бустик', callback_data='мини-бустик')
        ],
        [
            InlineKeyboardButton(text='ИП', callback_data='ИП'),
            InlineKeyboardButton(text='ПРЕДПРИНИМАТЕЛЬ', callback_data='ПРЕДПРИНИМАТЕЛЬ'),
            InlineKeyboardButton(text='МАЖОР', callback_data='МАЖОР')
        ]
    ]
)

event_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Медведь 🐻', callback_data='Медведь')
        ],
        [
            InlineKeyboardButton(text='Кража 💰', url='https://t.me/michaelgamechat/14')
        ],
        [
            InlineKeyboardButton(text='Рыбачить 🎣', callback_data='Рыбачить')
        ],
        [
            InlineKeyboardButton(text='Рыболовный магазин 🏪', callback_data='Рыболовный магазин')
        ]
    ]
)

event_fishing = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рыбачить 🎣', callback_data='Рыбачить')
        ],
        [
            InlineKeyboardButton(text='Рыболовный магазин 🏪', callback_data='Рыболовный магазин')
        ],
        [
            InlineKeyboardButton(text='Профиль 👨‍💼', callback_data='Профиль 👨‍💼')
        ]
    ]
)

event_fishing_shop = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рыбачить 🎣', callback_data='Рыбачить')
        ],
        [
            InlineKeyboardButton(text='Обновка! 🎣', callback_data='Обновка!')
        ],
        [
            InlineKeyboardButton(text='Вкуснотища! 🐛', callback_data='Вкуснотища!')
        ],
        [
            InlineKeyboardButton(text='По течению вверх! 🌊', callback_data='По течению вверх!')
        ]
    ]
)

event_steal = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Кража 💰', url='https://t.me/michaelgamechat/14')
        ]
    ]
)

not_reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Играть', url='https://t.me/michaelgame_bot')
        ]
    ]
)

event_exchanger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Обменять шишки 🌰', callback_data='Обменять шишки')
        ]
    ]
)


event_exchanger_fish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1 шт', callback_data='1 шт'),
            InlineKeyboardButton(text='3 шт', callback_data='3 шт'),
            InlineKeyboardButton(text='5 шт', callback_data='5 шт')
        ],
        [
            InlineKeyboardButton(text='10 шт', callback_data='10 шт')
        ]
    ]
)

event_bear = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Повысить силу атаки медведя 💪', callback_data='Повысить силу атаки медведя')
        ],
        [
            InlineKeyboardButton(text='Повысить защиту медведя 🛡️', callback_data='Повысить защиту медведя')
        ]
    ]
)

event_up_power = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1 раз', callback_data='1 power'),
            InlineKeyboardButton(text='3 раз', callback_data='3 power'),
            InlineKeyboardButton(text='5 раз', callback_data='5 power')
        ],
        [
            InlineKeyboardButton(text='10 раз', callback_data='10 power')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='bear_back')
        ]
    ]
)


event_up_protection = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1 раз', callback_data='1 protection'),
            InlineKeyboardButton(text='3 раз', callback_data='3 protection'),
            InlineKeyboardButton(text='5 раз', callback_data='5 protection')
        ],
        [
            InlineKeyboardButton(text='10 раз', callback_data='10 protection')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='bear_back')
        ]
    ]
)
