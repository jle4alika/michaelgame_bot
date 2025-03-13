from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
import database.requests.get as get
import keyboards.inline as kb


from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))


@router.message(F.text == 'Топ игроков 🔥')
async def top(message: Message):
    await message.answer('Выберите топ, который хотите посмотреть...', reply_markup=kb.choose_top)


@router.callback_query(F.data == 'Топ игроков 🔥')
async def top(callback: CallbackQuery):
    await callback.message.answer('Выберите топ, который хотите посмотреть...', reply_markup=kb.choose_top)


@router.callback_query(F.data == '👨‍💼')
async def top(callback: CallbackQuery):
    top_money = await get.get_top_referrals()
    id = 0
    count = 100
    msg = ''
    for item in top_money:
        id += 1
        if id <= count:
            user = await get.get_user(item)
            if user:
                referral = await get.get_referrer_count(item)
                nickname = await get.get_user_nickname(item)
                mention = f'<a href="tg://user?id={item}">{nickname}</a>'
                m = f'{id}. {mention} - <b>{referral}</b>👨‍💼\n'
                msg += m
            else:
                id -= 1
        else:
            break
    await callback.message.answer(f'Топ игроков <u>по приглашениям</u>:\n{msg}', reply_markup=kb.top, parse_mode=ParseMode.HTML)


@router.callback_query(F.data == '🔥')
async def process_callback_top(callback: CallbackQuery):
    top_money = await get.get_top_money()
    id = 0
    count = 100
    msg = ''
    for item in top_money:
        id += 1
        if id <= count:
            user = await get.get_user(item)
            if user:
                money = await get.get_money(item)
                nickname = await get.get_user_nickname(item)
                mention = f'<a href="tg://user?id={item}">{nickname}</a>'
                m = f'{id}. {mention} - <b>{money}</b>🌰\n'
                msg += m
            else:
                id -= 1
        else:
            break
    await callback.message.answer(f'Топ 100 по <u>заработанным шишкам</u> 🌰:\n{msg}', reply_markup=kb.top, parse_mode=ParseMode.HTML)


@router.callback_query(F.data == '💸')
async def process_callback_top(callback: CallbackQuery):
    top_money = await get.get_top_alltime_money()
    id = 0
    count = 100
    msg = ''
    for item in top_money:
        id += 1
        if id <= count:
            user = await get.get_user_bool(item)
            if user:
                alltime_money = await get.get_alltime_money(item)
                nickname = await get.get_user_nickname(item)
                mention = f'<a href="tg://user?id={item}">{nickname}</a>'
                m = f'{id}. {mention} - <b>{alltime_money}</b>🌰\n'
                msg += m
            else:
                id -= 1
        else:
            break
    await callback.message.answer(f'Топ 100 по <u>заработанным шишкам за всё время</u>:\n{msg}', reply_markup=kb.top, parse_mode=ParseMode.HTML)


@router.callback_query(F.data == '🐟')
async def process_callback_top(callback: CallbackQuery):
    top_fish = await get.get_top_fish()
    id = 0
    count = 100
    msg = ''
    for item in top_fish:
        id += 1
        if id <= count:
            user = await get.get_user(item)
            if user:
                fish = await get.get_fish(item)
                nickname = await get.get_user_nickname(item)
                mention = f'<a href="tg://user?id={item}">{nickname}</a>'
                m = f'{id}. {mention} - <b>{fish}</b>🐟\n'
                msg += m
            else:
                id -= 1
        else:
            break
    await callback.message.answer(f'Топ 100 по <u>выловленной рыбе</u> 🐟:\n{msg}', reply_markup=kb.top, parse_mode=ParseMode.HTML)