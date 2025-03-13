from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

import asyncio
import database.requests.get as get
import database.requests.add as add
import database.requests.minus as minus
import keyboards.inline as kb
import random
import datetime

from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))


@router.message(F.text == 'Магазин улучшений 🛒')
async def upgrades(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAJZgGZ2o8m_UwkvtAXsPmsvmF2ALchLAAJX3DEbbPu5S7uj9r8hNqHZAQADAgADeQADNQQ',
                               caption='Ты заходишь в старую хижину мага и слышишь звон входного колокола и старика мага.'
                                       'Приветствую, мой посетитель! Чувствуй себя как дома!'
                                       '\nТы же от Михаила? Ох, да, можешь не отвечать...'
                                       '\nВ моём магазине есть кое-что для тебя... Пойдём за мной...'
                                       '\nПеред твоим взором появляется список с товарами:'
                                       '\n1. Повышение шанса выпадения бустов на <b>0.2% навсегда за 350 тысяч</b>.'
                                       '\n2. Повышение шанса выпадения бустов на <b>0.3% навсегда за 550 тысяч</b>.'
                                       '\n3. Повышение шанса выпадения бустов на <b>0.1% на 8 часов (раз в сутки)</b>.'
                                       '\n4. Чёрная магия: <ins>50% шанс</ins> +0.75% к шансу выпадения бустов, <ins>но 50% шанс</ins> <b> -0.5% к шансу выпадения бустов,действует 12 часов. (раз в сутки)</b>.'
                                       '\n5. Волшебнный напиток Михалычу за 1 млн., <b>даёт +1% к шансу выпадения бустов, действует 1 час</b>.'
                                       '\n6. Талисман удачи за 3 млн., <b>повышает шанс выпадения бустов на 1.5%, действует 5 часов.</b>',
                               reply_markup=kb.upgrades, parse_mode=ParseMode.HTML)

@router.callback_query(F.data == 'Магазин улучшений 🛒')
async def upgrades(callback: CallbackQuery):
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAJZgGZ2o8m_UwkvtAXsPmsvmF2ALchLAAJX3DEbbPu5S7uj9r8hNqHZAQADAgADeQADNQQ',
                               caption='Ты заходишь в старую хижину мага и слышишь звон входного колокола и старика мага.'
                                       'Приветствую, мой посетитель! Чувствуй себя как дома!'
                                       '\nТы же от Михаила? Ох, да, можешь не отвечать...'
                                       '\nВ моём магазине есть кое-что для тебя... Пойдём за мной...'
                                       '\nПеред твоим взором появляется список с товарами:'
                                       '\n1. Повышение шанса выпадения бустов на <b>0.2% навсегда за 350 тысяч</b>.'
                                       '\n2. Повышение шанса выпадения бустов на <b>0.3% навсегда за 550 тысяч</b>.'
                                       '\n3. Повышение шанса выпадения бустов на <b>0.1% на 8 часов (раз в сутки)</b>.'
                                       '\n4. Чёрная магия: <ins>50% шанс</ins> +0.75% к шансу выпадения бустов, <ins>но 50% шанс</ins> <b> -0.5% к шансу выпадения бустов,действует 12 часов. (раз в сутки)</b>.'
                                       '\n5. Волшебнный напиток Михалычу за 1 млн., <b>даёт +1% к шансу выпадения бустов, действует 1 час</b>.'
                                       '\n6. Талисман удачи за 3 млн., <b>повышает шанс выпадения бустов на 1.5%, действует 5 часов.</b>',
                               reply_markup=kb.upgrades, parse_mode=ParseMode.HTML)


@router.callback_query(F.data == '1')
async def upgrade1(callback: CallbackQuery):
    if await get.get_boost_chance(callback.from_user.id) < 45.0:
        if await get.get_money(callback.from_user.id) >= 350000:
            await minus.minus_money(callback.from_user.id, 350000)
            await add.add_boost_chance(callback.from_user.id, 0.2)
            await callback.answer('К вашему шансу выпадения бустов успешно добавлено 0.2%.', show_alert=True)
        else:
            await callback.answer('У вас недостаточно денег на балансе.', show_alert=True)
    else:
        await callback.answer('У вас максимальное значение шанса выпадения бустов.')


@router.callback_query(F.data == '2')
async def upgrade2(callback: CallbackQuery):
    if await get.get_boost_chance(callback.from_user.id) < 45.0:
        if await get.get_money(callback.from_user.id) >= 550000:
            await minus.minus_money(callback.from_user.id, 550000)
            await add.add_boost_chance(callback.from_user.id, 0.3)
            await callback.answer('К вашему шансу выпадения бустов успешно добавлено 0.3%.', show_alert=True)
        else:
            await callback.answer('У вас недостаточно денег на балансе.', show_alert=True)
    else:
        await callback.answer('У вас максимальное значение шанса выпадения бустов.')


@router.callback_query(F.data == '3')
async def upgrade3(callback: CallbackQuery):
    if await get.get_boost_chance(callback.from_user.id) < 45.0:
        user = await get.get_upgrade1(callback.from_user.id)
        remaining_time = user - datetime.datetime.now()
        if remaining_time.total_seconds() <= 0:
            await add.add_boost_chance(callback.from_user.id, 0.1)
            await callback.answer('Вы забрали ежедневный бонус и получили',show_alert=True)
            await add.add_upgrade1(callback.from_user.id, 24)
            await asyncio.sleep(60 * 60 * 5)
            await minus.minus_boost_chance(callback.from_user.id, 0.1)
        else:
            await callback.answer(f'Оставшееся время: {round(remaining_time.total_seconds() / (60 * 60))} часов')
    else:
        await callback.answer('У вас максимальное значение шанса выпадения бустов.')


@router.callback_query(F.data == '4')
async def upgrade4(callback: CallbackQuery):
    if await get.get_boost_chance(callback.from_user.id) < 45.0:
        user = await get.get_upgrade2(callback.from_user.id)
        remaining_time = user - datetime.datetime.now()
        if remaining_time.total_seconds() <= 0:
            chance = random.randint(1, 100)
            await callback.message.answer_dice()
            await asyncio.sleep(4)
            if chance <= 50:
                await add.add_boost_chance(callback.from_user.id, 0.75)
                await callback.answer('+0.75% к шансу выпадения бустов! Да вы везунчик!\nМои поздравления!', show_alert=True)
                await add.add_upgrade2(callback.from_user.id, 24)
                await asyncio.sleep(60 * 60 * 12)
                await minus.minus_boost_chance(callback.from_user.id, 0.75)
            else:
                await minus.minus_boost_chance(callback.from_user.id, 0.5)
                await callback.answer('-0.5% к шансу выпадения бустов!\nМои соболезнования...', show_alert=True)
                await add.add_upgrade2(callback.from_user.id, 24)
                await asyncio.sleep(60*60*12)
                await add.add_boost_chance(callback.from_user.id, 0.5)
        else:
            await callback.answer(f'Оставшееся время: {round(remaining_time.total_seconds() / (60*60))} часов')
    else:
        await callback.answer('У вас максимальное значение шанса выпадения бустов.')


@router.callback_query(F.data == '5')
async def upgrade5(callback: CallbackQuery):
    if await get.get_boost_chance(callback.from_user.id) < 45.0:
        if await get.get_money(callback.from_user.id) >= 1000000:
            await minus.minus_money(callback.from_user.id, 1000000)
            if await get.get_boost_chance(callback.from_user.id) < 45.0:
                await add.add_boost_chance(callback.from_user.id, 1.0)
                await callback.answer('К вашему шансу выпадения бустов успешно добавлено 1%.', show_alert=True)
                await asyncio.sleep(60*60)
                await minus.minus_boost_chance(callback.from_user.id, 1.0)
        else:
            await callback.answer('У вас недостаточно денег на балансе.', show_alert=True)
    else:
        await callback.answer('У вас максимальное значение шанса выпадения бустов.')


@router.callback_query(F.data == '6')
async def upgrade6(callback: CallbackQuery):
    if await get.get_boost_chance(callback.from_user.id) < 45.0:
        if await get.get_money(callback.from_user.id) >= 3000000:
            await minus.minus_money(callback.from_user.id, 3000000)
            await add.add_boost_chance(callback.from_user.id, 1.5)
            await callback.answer('К вашему шансу выпадения бустов успешно добавлено 1.5%.', show_alert=True)
            await asyncio.sleep(60 * 60 * 5)
            await minus.minus_boost_chance(callback.from_user.id, 1.5)
        else:
            await callback.answer('У вас недостаточно денег на балансе.', show_alert=True)
    else:
        await callback.answer('У вас максимальное значение шанса выпадения бустов.')
