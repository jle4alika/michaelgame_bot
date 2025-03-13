from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from handlers.states import Reg
import database.requests.get as rq
import keyboards.inline as kb
from aiogram.enums import ParseMode


from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))


@router.message(F.text == 'Профиль 👨‍💼')
async def profile(message: Message):
    photo = await rq.get_photo_id(message.from_user.id)
    money = await rq.get_money(message.from_user.id)
    fish = await rq.get_fish(message.from_user.id)
    place = [0, 0, 0, 0]
    a = 0
    b = 0
    c = 0
    d = 0
    top_alltime_money = await rq.get_top_alltime_money()
    top_money = await rq.get_top_money()
    top_referrals = await rq.get_top_referrals()
    top_fish = await rq.get_top_fish()
    for item in top_alltime_money:
        a += 1
        if item == message.from_user.id:
            place[0] = a

    for item in top_money:
        b += 1
        if item == message.from_user.id:
            place[1] = b

    for item in top_referrals:
        c += 1
        if item == message.from_user.id:
            place[2] = c

    for item in top_fish:
        d += 1
        if item == message.from_user.id:
            place[3] = d

    if len(photo) > 0:
        await message.answer_photo(
            photo=photo,
            caption=f'Приветствую, {await rq.get_user_nickname(message.from_user.id)}\n\n'
                    f'Ваш баланс: <b>{money}</b> шишек 🌰!\n\n'
                    f'<b>Ваша рыба:</b> {fish} 🐟\n'
                    f'Ваш шанс выпадения шишек 🌰:<b>{await rq.get_money_chance(message.from_user.id)}%</b>'
                    f'\nВаш шанс выпадения бустов 🔋:<b>{await rq.get_boost_chance(message.from_user.id)}%</b>'
                    f'\n\nУ вас топ <b>{place[0]}</b> по заработанному за всё время! 💸'
                    f'\nУ вас топ <b>{place[1]}</b> по деньгам! 🔥'
                    f'\nУ вас топ <b>{place[2]}</b> по приглашённым пользователям! 👨‍💼'
                    f'\nУ вас топ <b>{place[3]}</b> по выловленной рыбе! 🐟',
            reply_markup=kb.profile, parse_mode=ParseMode.HTML)
    else:
        await message.answer_photo(
            photo='AgACAgIAAxkBAAJY_mZ0Shb6-gEJ0gvWTCotNMX5wLi0AAIt4DEbfl2oS2pMPLmZ_5PCAQADAgADeQADNQQ',
            caption=f'Приветствую, {await rq.get_user_nickname(message.from_user.id)}\n\n'
                    f'Ваш баланс: {money} шишек 🌰!\n\n'
                    f'<b>Ваша рыба:</b> {fish} 🐟\n'
                    f'Ваш шанс выпадения шишек 🌰:{await rq.get_money_chance(message.from_user.id)}%'
                    f'\nВаш шанс выпадения бустов 🔋:{await rq.get_boost_chance(message.from_user.id)}%'
                    f'\n\nУ вас топ {place[0]} по заработанному за всё время! 💸'
                    f'\nУ вас топ {place[1]} по деньгам! 🔥'
                    f'\nУ вас топ {place[2]} по приглашённым пользователям! 👨‍💼'
                    f'\nУ вас топ <b>{place[3]}</b> по выловленной рыбе! 🐟',
            reply_markup=kb.profile, parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'Профиль 👨‍💼')
async def callback_profile(callback: CallbackQuery):
    photo = await rq.get_photo_id(callback.from_user.id)
    money = await rq.get_money(callback.from_user.id)
    fish = await rq.get_fish(callback.from_user.id)
    place = [0, 0, 0, 0]
    a = 0
    b = 0
    c = 0
    d = 0
    top_alltime_money = await rq.get_top_alltime_money()
    top_money = await rq.get_top_money()
    top_referrals = await rq.get_top_referrals()
    top_fish = await rq.get_top_fish()
    for item in top_alltime_money:
        a += 1
        if item == callback.from_user.id:
            place[0] = a

    for item in top_money:
        b += 1
        if item == callback.from_user.id:
            place[1] = b

    for item in top_referrals:
        c += 1
        if item == callback.from_user.id:
            place[2] = c
    for item in top_fish:
        d += 1
        if item == callback.from_user.id:
            place[3] = d
    if len(photo) > 0:
        await callback.message.answer_photo(
            photo=photo,
            caption=f'Приветствую, {await rq.get_user_nickname(callback.from_user.id)}\n\n'
                    f'Ваш баланс: <b>{money}</b> шишек 🌰!\n\n'
                    f'<b>Ваша рыба:</b> {fish} 🐟\n'
                    f'Ваш шанс выпадения шишек 🌰:<b>{await rq.get_money_chance(callback.from_user.id)}%</b>'
                    f'\nВаш шанс выпадения бустов 🔋:<b>{await rq.get_boost_chance(callback.from_user.id)}%</b>'
                    f'\n\nУ вас топ <b>{place[0]}</b> по заработанному за всё время! 💸'
                    f'\nУ вас топ <b>{place[1]}</b> по деньгам! 🔥'
                    f'\nУ вас топ <b>{place[2]}</b> по приглашённым пользователям! 👨‍💼'
                    f'\nУ вас топ <b>{place[3]}</b> по выловленной рыбе! 🐟',
            reply_markup=kb.profile, parse_mode=ParseMode.HTML)
    else:
        await callback.message.answer_photo(
            photo='AgACAgIAAxkBAAJY_mZ0Shb6-gEJ0gvWTCotNMX5wLi0AAIt4DEbfl2oS2pMPLmZ_5PCAQADAgADeQADNQQ',
            caption=f'Приветствую, {await rq.get_user_nickname(callback.from_user.id)}\n\n'
                    f'Ваш баланс: <b>{money}</b> шишек 🌰!\n\n'
                    f'<b>Ваша рыба:</b> {fish} 🐟\n'
                    f'Ваш шанс выпадения шишек 🌰:<b>{await rq.get_money_chance(callback.from_user.id)}%</b>'
                    f'\nВаш шанс выпадения бустов 🔋:<b>{await rq.get_boost_chance(callback.from_user.id)}%</b>'
                    f'\n\nУ вас топ <b>{place[0]}</b> по заработанному за всё время! 💸'
                    f'\nУ вас топ <b>{place[1]}</b> по деньгам! 🔥'
                    f'\nУ вас топ <b>{place[2]}</b> по приглашённым пользователям! 👨‍💼'
                    f'\nУ вас топ <b>{place[3]}</b> по выловленной рыбе! 🐟',
            reply_markup=kb.profile, parse_mode=ParseMode.HTML)



@router.callback_query(F.data == 'Изменить фото профиля 🖼')
async def process_callback_reg1(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Отправьте предпочитаемое фото')
    await state.set_state(Reg.photo_id)


@router.callback_query(F.data == 'Изменить никнейм 😎')
async def set_nickname(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите ваш никнейм:')
    await state.set_state(Reg.nickname)