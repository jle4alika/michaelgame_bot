from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
import keyboards.inline as kb
from aiogram.enums import ParseMode
import database.requests.get as get
import database.requests.add as add
import database.requests.minus as minus
import database.requests.others as set
from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))

@router.message(F.text == 'Обменник 🤝')
async def exchanger(message: Message):
    await message.answer('Когда вы открываете старую деревянную дверь, перед глазами возникает уютный лесной уголок. '
                         'Ты видишь забавного медведя в фартуке, стоящего за прилавком, полный свежевыловленной рыбы. '
                         'Медведь улыбается и дружелюбно машет лапой, приглашая подойти.\n\n'
                         'Добро пожаловать в наш обменник! Поменяйте свои шишки на свежую рыбу у нашего рыжего мишки! 🍂🐟', reply_markup=kb.event_exchanger)


@router.callback_query(F.data == 'Обменник 🤝')
async def process_callback_exchanger(callback: CallbackQuery):
    await callback.message.answer('Когда вы открываете старую деревянную дверь, перед глазами возникает уютный лесной уголок. '
                                  'Ты видишь забавного медведя в фартуке, стоящего за прилавком, полный свежевыловленной рыбы. '
                                  'Медведь улыбается и дружелюбно машет лапой, приглашая подойти.\n\n'
                                  'Добро пожаловать в наш обменник! Поменяйте свои шишки на свежую рыбу у нашего рыжего мишки! 🍂🐟', reply_markup=kb.event_exchanger)


@router.callback_query(F.data == 'Обменять шишки')
async def event_change(callback: CallbackQuery):
    money = await get.get_money(callback.from_user.id)
    await callback.message.answer(f'Ваш баланс <b>{money}</b> 🌰\n\n'
                                  '<b>Обменник рыбы на шишки:</b>\n\n'
                                  '- <b>1 рыба</b> = 375,000 шишек\n'
                                  '- <b>3 рыбы</b> = 1,125,000 шишек\n'
                                  '- <b>5 рыб</b> = 1,875,000 шишек\n'
                                  '- <b>10 рыб</b> = 3,750,000 шишек\n',
                                  reply_markup=kb.event_exchanger_fish, parse_mode=ParseMode.HTML)

@router.callback_query(F.data == '1 шт')
async def event_change(callback: CallbackQuery):
    if await get.get_money(callback.from_user.id) >= 375000:
        await minus.minus_money(callback.from_user.id, 375000)
        await add.add_fish(callback.from_user.id, 1)
        await callback.answer('Вы успешно приобрели 1 рыбку 🌊🐟!')
    else:
        await callback.answer('У вас недостаточно денег для обмена.')

@router.callback_query(F.data == '3 шт')
async def event_change(callback: CallbackQuery):
    if await get.get_money(callback.from_user.id) >= 1125000:
        await minus.minus_money(callback.from_user.id, 1125000)
        await add.add_fish(callback.from_user.id, 3)
        await callback.answer('Вы успешно приобрели 3 рыбки 🌊🐟!')
    else:
        await callback.answer('У вас недостаточно денег для обмена.')


@router.callback_query(F.data == '5 шт')
async def event_change(callback: CallbackQuery):
    if await get.get_money(callback.from_user.id) >= 1875000:
        await minus.minus_money(callback.from_user.id, 1875000)
        await add.add_fish(callback.from_user.id, 5)
        await callback.answer('Вы успешно приобрели 5 рыбок 🌊🐟!')
    else:
        await callback.answer('У вас недостаточно денег для обмена.')

@router.callback_query(F.data == '10 шт')
async def event_change(callback: CallbackQuery):
    if await get.get_money(callback.from_user.id) >= 3750000:
        await minus.minus_money(callback.from_user.id, 3750000)
        await add.add_fish(callback.from_user.id, 10)
        await callback.answer('Вы успешно приобрели 10 рыбок 🌊🐟!')
    else:
        await callback.answer('У вас недостаточно денег для обмена.')
