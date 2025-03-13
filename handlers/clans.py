import asyncio
import random

from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.chat_types import ChatTypeFilter
from handlers.states import Clan, Clan_add
import database.requests.get as get
import database.requests.add as add
import database.requests.minus as minus
import database.requests.others as set
import keyboards.inline as kb
from aiogram.enums import ParseMode

router = Router()
router.message.filter(ChatTypeFilter(['private']))
async def owner_main_kb(tg_id: int):
    if tg_id == await get.get_clan_owner(tg_id):
        return kb.clan_owner
    else:
        return kb.clan_main

@router.message(F.text == 'Кланы 🛡️')
async def clans(message: Message):
    if await get.get_user_clan(message.from_user.id) != 0 and int(str(await get.get_user_clan(message.from_user.id))[:6]) != 892352:
        type = await get.get_clan_type(message.from_user.id)
        if type == 0:
            type = 'OPEN'
        else:
            type = 'PRIVATE'
        if await get.get_clan_photo(message.from_user.id) == '':
            name = await get.get_clan_name(message.from_user.id)
            money = await get.get_clan_money(message.from_user.id)
            count = await get.get_clan_members(message.from_user.id)
            users_money = await get.get_clan_users_money(message.from_user.id)
            money_chance = await get.get_clan_money_chance(message.from_user.id)
            boost_chance = await get.get_clan_boost_chance(message.from_user.id)
            code = await get.get_clan_code(message.from_user.id)
            await message.answer_photo(
                photo='AgACAgIAAxkBAAJgPWaP6DS_Mee7DI9CGYUGd-RHHqY2AALP3jEbNceASMYNm_KYutUrAQADAgADeQADNQQ',
                caption=f'Название клана: {name}\n\n'
                        f'Денег в казне: {money}\n'
                        f'Кол-во участников: {count}\n'
                        f'Деньги всех участников: {users_money}\n'
                        f'Доп. шанс выпадения игровой валюты: {money_chance}\n'
                        f'Доп. шанс выпадения бустов: {boost_chance}\n'
                        f'Ваш тип клана - {type}\n'
                        f'Код для вступления: {code}',
                reply_markup=await owner_main_kb(message.from_user.id))
        else:
            name = await get.get_clan_name(message.from_user.id)
            photo = await get.get_clan_photo(message.from_user.id)
            money = await get.get_clan_money(message.from_user.id)
            count = await get.get_clan_members(message.from_user.id)
            users_money = await get.get_clan_users_money(message.from_user.id)
            money_chance = await get.get_clan_money_chance(message.from_user.id)
            boost_chance = await get.get_clan_boost_chance(message.from_user.id)
            code = await get.get_clan_code(message.from_user.id)
            await message.answer_photo(
                photo=f'{photo}',
                caption=f'Название клана: {name}\n\n'
                        f'Денег в казне: {money}\n'
                        f'Кол-во участников: {count}\n'
                        f'Деньги всех участников: {users_money}\n'
                        f'Доп. шанс выпадения игровой валюты: {money_chance}\n'
                        f'Доп. шанс выпадения бустов: {boost_chance}\n'
                        f'Ваш тип клана - {type}\n'
                        f'Код для вступления: {code}',
                reply_markup=await owner_main_kb(message.from_user.id))
    else:
        await message.answer_photo(photo='AgACAgIAAxkBAAJgPWaP6DS_Mee7DI9CGYUGd-RHHqY2AALP3jEbNceASMYNm_KYutUrAQADAgADeQADNQQ',
                                   caption='<b>Вы не состоите в клане.</b>\n'  
                                'Кланы – это группы игроков, объединенных общей целью и\n'
                              ' интересами. Вступив в клан, вы получите доступ к специальным\n'
                              ' клановым заданиям, чатам и событиям, которые позволят вам\n'
                              ' получать уникальные награды и бонусы.\n\n'

                                '✨ <b>Преимущества участия в клане:</b>\n'
                                '- Совместные квесты и мероприятия.\n'
                                '- Обмен ресурсами и советы от более опытных игроков.\n'
                                '- Возможность участвовать в клановых войнах и завоевывать территорию.\n'
                                '- Эксклюзивные награды и баффы (усиления).\n\n'

                                '📜 <b>Как вступить в клан:</b>\n'
                                '1. Откройте раздел "Вступить в открытый клан".\n'
                                '2. Выберите клан, который вам интересен.\n'
                                '3. Отправьте заявку на вступление или свяжитесь с лидером\n'
                                'клана для получения приглашения.\n\n'

                                '🌟 <b>Или создайте свой клан:</b>\n'
                                'Если вы хотите создать свой собственный клан и собрать команду единомышленников, у вас есть возможность создать новый клан. Для этого перейдите в раздел "Создание клана" и следуйте инструкциям.\n'
                                'Не упустите шанс стать частью дружной и сильной команды! 🌟',
                                   reply_markup=kb.clan_start,
                                   parse_mode=ParseMode.HTML)

@router.callback_query(F.data == 'Создать клан')
async def clan_create(callback: CallbackQuery, state: FSMContext):
    # название тип аватар
    await set.set_clan(callback.from_user.id)
    await add.add_clan_name(callback.from_user.id, str(callback.from_user.username))
    await callback.message.answer('Введите название клана:')
    await state.set_state(Clan.name)

@router.callback_query(F.data == 'Удалить клан')
async def clan_del(callback: CallbackQuery):
    if callback.from_user.id == await get.get_clan_owner(callback.from_user.id):
        if await get.get_clan_photo(callback.from_user.id) == '':
            name = await get.get_clan_name(callback.from_user.id)
            money = await get.get_clan_money(callback.from_user.id)
            count = await get.get_clan_members(callback.from_user.id)
            users_money = await get.get_clan_users_money(callback.from_user.id)
            money_chance = await get.get_clan_money_chance(callback.from_user.id)
            boost_chance = await get.get_clan_boost_chance(callback.from_user.id)
            await callback.message.edit_caption(
                                    caption=f'Название клана: {name}\n\n'
                                    f'Денег в казне: {money}\n'
                                    f'Кол-во участников: {count}\n'
                                    f'Деньги всех участников: {users_money}\n'
                                    f'Доп. шанс выпадения игровой валюты: {money_chance}\n'
                                    f'Доп. шанс выпадения бустов: {boost_chance}\n\n'
                                    'ВЫ УВЕРЕНЫ, ЧТО ХОТИТЕ УДАЛИТЬ КЛАН?',
                                    reply_markup=kb.clan_delete)
        else:
            name = await get.get_clan_name(callback.from_user.id)
            money = await get.get_clan_money(callback.from_user.id)
            count = await get.get_clan_members(callback.from_user.id)
            users_money = await get.get_clan_users_money(callback.from_user.id)
            money_chance = await get.get_clan_money_chance(callback.from_user.id)
            boost_chance = await get.get_clan_boost_chance(callback.from_user.id)
            await callback.message.edit_caption(
                caption=f'Название клана: {name}\n\n'
                        f'Денег в казне: {money}\n'
                        f'Кол-во участников: {count}\n'
                        f'Деньги всех участников: {users_money}\n'
                        f'Доп. шанс выпадения игровой валюты: {money_chance}\n'
                        f'Доп. шанс выпадения бустов: {boost_chance}\n\n\n\n'
                        'ВЫ УВЕРЕНЫ, ЧТО ХОТИТЕ УДАЛИТЬ КЛАН?',
                reply_markup=kb.clan_delete)
    else:
        await callback.answer('Вы не владелец клана.',
                              show_alert=True)

@router.callback_query(F.data == 'Удалить')
async def clan_delete(callback: CallbackQuery, bot: Bot):
    name = await get.get_clan_name(callback.from_user.id)
    users = await get.get_clan_users(callback.from_user.id)
    await set.delete_clan(callback.from_user.id)
    await callback.answer('Ваш клан успешно удалён...', show_alert=True)
    for user in users:
        await bot.send_message(chat_id=user, text=f'Клан {name} был удалён создателем.')
        await set.set_user_clan(user, 0)

@router.callback_query(F.data == 'Не удалять')
async def clan_delete(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup= await owner_main_kb(callback.from_user.id))

async def del_from_clan(callback: CallbackQuery):
    all_members = await get.get_clan_name_members(callback.from_user.id)
    length = len(all_members)
    if callback.data.startswith('next_') or callback.data.startswith('back_'):
        if str(callback.data[:5]) == 'next_':
            i = int(callback.data[5:])
            i += 1
        else:
            i = int(callback.data[5:])
            i -= 1
    else:
        i = 1
    print(i)
    kb = InlineKeyboardBuilder()
    if i == 1:
        for member in all_members[:8]:
            clans = kb.add(InlineKeyboardButton(text=f'{member}', callback_data=f'nickname_{member}'))
            clans.adjust(2)
        if length / i > 8:
            next = kb.add(InlineKeyboardButton(text='Далее', callback_data=f'next_{i}'))
            next.adjust(2)
    else:
        if i * 8 >= length:
            for member in all_members[(i - 1) * 8:i * 8]:
                clans = kb.add(InlineKeyboardButton(text=f'{member}', callback_data=f'nickname_{member}'))
                clans.adjust(2)
            if length / i > 8:
                next = kb.add(InlineKeyboardButton(text='Далее', callback_data=f'next_{i}'))
                next.adjust(2)
        elif i * 8 <= length:
            if length < (i + 1) * 8:
                for member in all_members[(i - 1) * 8:length]:
                    clans = kb.add(InlineKeyboardButton(text=f'{member}', callback_data=f'nickname_{member}'))
                    clans.adjust(2)
            for member in all_members[(i - 1) * 8:length - 1]:
                clans = kb.add(InlineKeyboardButton(text=f'{member}', callback_data=f'nickname_{member}'))
                clans.adjust(2)
            if length / i > 8:
                next = kb.add(InlineKeyboardButton(text='Далее', callback_data=f'next_{i}'))
                next.adjust(2)
        back = kb.add(InlineKeyboardButton(text='Назад', callback_data=f'back_{i}'))
        back.adjust(2)

    if length == 0:
        await callback.answer('Нету пользователей кроме вас.', show_alert=True)
        return await owner_main_kb(callback.from_user.id)
    else:
        return clans.as_markup()


@router.callback_query(F.data == 'Изгнать из клана')
async def clan_delete_from_clan(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await del_from_clan(callback))


@router.callback_query(F.data.startswith('nickname'))
async def clan_delete_from_clan(callback: CallbackQuery):
    Clan_add.nickname = str(callback.data.replace('nickname_', ''))
    delete = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Изгнать', callback_data='Изгнать'),
                InlineKeyboardButton(text='Назад', callback_data='delete_back')
            ]
        ]
    )
    nickname = Clan_add.nickname
    user = await get.user_tg_id_by_nickname(nickname)
    money = await get.get_money(user)
    place = [0, 0, 0]
    a = 0
    b = 0
    c = 0
    top_alltime_money = await get.get_top_alltime_money()
    top_money = await get.get_top_money()
    top_referrals = await get.get_top_referrals()
    for item in top_alltime_money:
        a += 1
        if item == user:
            place[0] = a

    for item in top_money:
        b += 1
        if item == user:
            place[1] = b

    for item in top_referrals:
        c += 1
        if item == user:
            place[2] = c
    await callback.message.edit_caption(
        caption=f'Игрок {nickname}\n\n'
                f'Баланс игрока: <b>{money}</b> шишек 🌰!\n\n'
                f'Шанс выпадения шишек 🌰:<b>{await get.get_money_chance(user)}%</b>'
                f'\nШанс выпадения бустов 🔋:<b>{await get.get_boost_chance(user)}%</b>'
                f'\n\nИгрок топ <b>{place[0]}</b> по заработанному за всё время! 💸'
                f'\nИгрок топ <b>{place[1]}</b> по деньгам! 🔥'
                f'\nИгрок топ <b>{place[2]}</b> по приглашённым пользователям! 👨‍💼',
        reply_markup=delete, parse_mode=ParseMode.HTML)

@router.callback_query(F.data == 'Изгнать')
async def clan_type_clan(callback: CallbackQuery, bot: Bot):
    nickname = Clan_add.nickname
    user = await get.user_tg_id_by_nickname(nickname)
    name = await get.get_clan_name(callback.from_user.id)
    await minus.minus_clan_member(user)
    await set.set_user_clan(user, 0)

    await callback.answer(f'Вы изгнали из клана {nickname}...', show_alert=True)
    await bot.send_message(user, f'Вас изгнали из клана {name}...')
@router.callback_query(F.data == 'delete_back')
async def clan_type_clan(callback: CallbackQuery):
    await clans(callback.message)


@router.callback_query(F.data == 'Тип клана')
async def clan_type_clan(callback: CallbackQuery):
    # закрытый (по приглашениям) открытый
    type = await get.get_clan_type(callback.from_user.id)
    if type == 0:
        type = 'OPEN'
    else:
        type = 'PRIVATE'
    await callback.message.answer(f'Ваш тип клана - {type}', reply_markup=kb.clan_type)

@router.callback_query(F.data == 'change_type')
async def clan_type_change(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=kb.clan_type_change)

@router.callback_query(F.data == 'private')
async def clan_type_private(callback: CallbackQuery):
    await add.add_clan_type(callback.from_user.id, 1)
    await clan_type_clan(callback)

@router.callback_query(F.data == 'open')
async def clan_type_open(callback: CallbackQuery):
    await add.add_clan_type(callback.from_user.id, 0)
    await clan_type_clan(callback)

@router.callback_query(F.data == 'type_back')
async def clan_type_back(callback: CallbackQuery):
    await clans(callback.message)


@router.callback_query(F.data == 'Изменить название клана')
async def clan_change_clan_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите новое название клана:')
    await state.set_state(Clan.name_again)

@router.callback_query(F.data == 'Изменить фото клана')
async def clan_change_photo(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Отправьте новое фото клана:')
    await state.set_state(Clan.clan_photo)


@router.callback_query(F.data == 'Улучшения')
async def clan_upgrades(callback: CallbackQuery):
    await callback.message.edit_caption('Вы за улучшениями для своих друзей? Ну тогда вы по адресу!'
                                        '1. РУЛЕТКА: +9.75% к шансам выпадения всех соклановцев на 12 часов, но щанс на это только 35%!\nСнижение шансов выпадения до нуля с шансом 65% на 12 часов.'
                                        '2. мини-шишка: 3 млн поднятие шанса выпадения шишек для всех соклановцев на 3% на 8 часов.'
                                        '3. мини-бустик: За 5 млн поднятие шанса выпадения бустов для всех соклановцев на 4% на 8 часов.'
                                        '4. ИП: За 7 млн поднятие шансов выпадения на 0.4% навсегда для всех соклановцев.'
                                        '5. ПРЕДПРИНИМАТЕЛЬ: За 15 млн поднятие шансов выпадения на 7% навсегда для всех соклановцев.'
                                        '6. МАЖОР: За 50 млн поднятие шансов выпадения на 15% навсегда для всех соклановцев.',
                                        reply_markup=kb.clan_upgrades)
    # await callback.answer('В разработке', show_alert=True)

@router.callback_query(F.data == 'РУЛЕТКА')
async def clan_upgrades(callback: CallbackQuery):
    users = await get.get_clan_users(callback.from_user.id)
    money_chance, boost_chance = await get.get_clan_money_chance(callback.from_user.id), await get.get_clan_boost_chance(callback.from_user.id)
    if random.randint(0, 100) <= 35:
        await add.update_clan_money_chance(callback.from_user.id, 9.75)
        await add.update_clan_boost_chance(callback.from_user.id, 9.75)
        for user in users:
            await add.add_money_chance(user, 9.75)
            await add.add_boost_chance(user, 9.75)
        await callback.answer('Поздравляю! Вам выпало +9.75% ко всем шансам.', show_alert=True)
        await asyncio.sleep(60*60*12)
        await minus.minus_clan_money_chance(callback.from_user.id, 9.75)
        await minus.minus_clan_boost_chance(callback.from_user.id, 9.75)
        for user in users:
            await minus.minus_money_chance(user, 9.75)
            await minus.minus_boost_chance(user, 9.75)

    else:
        await add.update_clan_money_chance(callback.from_user.id, 0)
        await add.update_clan_boost_chance(callback.from_user.id, 0)
        for user in users:
            await minus.minus_money_chance(user, money_chance)
            await minus.minus_boost_chance(user, boost_chance)
        await callback.answer('Шансы выпадения снижены до 0...', show_alert=True)
        await asyncio.sleep(60*60*12)
        await add.update_clan_money_chance(callback.from_user.id, money_chance)
        await add.update_clan_boost_chance(callback.from_user.id, boost_chance)
        for user in users:
            await add.add_money_chance(user, money_chance)
            await add.add_boost_chance(user, boost_chance)

@router.callback_query(F.data == 'мини-шишка')
async def clan_upgrades(callback: CallbackQuery):
    clan_money = await get.get_clan_money(callback.from_user.id)
    users = await get.get_clan_users(callback.from_user.id)
    if clan_money >= 3000000:
        await minus.minus_clan_money(callback.from_user.id, 3000000)
        await add.update_clan_money_chance(callback.from_user.id, 3)
        for user in users:
            await add.add_money_chance(user, 3)
        await callback.answer('Вы успешно купили улучшение!', show_alert=True)
        await asyncio.sleep(60 * 60 * 8)
        await minus.minus_clan_money_chance(callback.from_user.id, 3)
        for user in users:
            await minus.minus_money_chance(user, 3)
    else:
        await callback.answer('Недостаточно денег в казне клана', show_alert=True)

@router.callback_query(F.data == 'мини-бустик')
async def clan_upgrades(callback: CallbackQuery):
    clan_money = await get.get_clan_money(callback.from_user.id)
    users = await get.get_clan_users(callback.from_user.id)
    if clan_money >= 5000000:
        await minus.minus_clan_money(callback.from_user.id, 5000000)
        await add.update_clan_boost_chance(callback.from_user.id, 4)
        for user in users:
            await add.add_boost_chance(user, 4)
        await callback.answer('Вы успешно купили улучшение!', show_alert=True)
        await asyncio.sleep(60 * 60 * 8)
        await minus.minus_clan_boost_chance(callback.from_user.id, 4)
        for user in users:
            await minus.minus_boost_chance(user, 4)
    else:
        await callback.answer('Недостаточно денег в казне клана', show_alert=True)


@router.callback_query(F.data == 'ИП')
async def clan_upgrades(callback: CallbackQuery):
    clan_money = await get.get_clan_money(callback.from_user.id)
    users = await get.get_clan_users(callback.from_user.id)
    if clan_money >= 7000000:
        await minus.minus_clan_money(callback.from_user.id, 7000000)
        await add.update_clan_money_chance(callback.from_user.id, 0.4)
        await add.update_clan_boost_chance(callback.from_user.id, 0.4)
        for user in users:
            await add.add_money_chance(user, 0.4)
            await add.add_boost_chance(user, 0.4)
        await callback.answer('Вы успешно купили улучшение!', show_alert=True)
    else:
        await callback.answer('Недостаточно денег в казне клана', show_alert=True)

@router.callback_query(F.data == 'ПРЕДПРИНИМАТЕЛЬ')
async def clan_upgrades(callback: CallbackQuery):
    clan_money = await get.get_clan_money(callback.from_user.id)
    users = await get.get_clan_users(callback.from_user.id)
    if clan_money >= 15000000:
        await minus.minus_clan_money(callback.from_user.id, 15000000)
        await add.update_clan_money_chance(callback.from_user.id, 7)
        await add.update_clan_boost_chance(callback.from_user.id, 7)
        for user in users:
            await add.add_money_chance(user, 7)
            await add.add_boost_chance(user, 7)
        await callback.answer('Вы успешно купили улучшение!', show_alert=True)
    else:
        await callback.answer('Недостаточно денег в казне клана', show_alert=True)

@router.callback_query(F.data == 'МАЖОР')
async def clan_upgrades(callback: CallbackQuery):
    clan_money = await get.get_clan_money(callback.from_user.id)
    users = await get.get_clan_users(callback.from_user.id)
    if clan_money >= 50000000:
        await minus.minus_clan_money(callback.from_user.id, 50000000)
        await add.update_clan_money_chance(callback.from_user.id, 15)
        await add.update_clan_boost_chance(callback.from_user.id, 15)
        for user in users:
            await add.add_money_chance(user, 15)
            await add.add_boost_chance(user, 15)
        await callback.answer('Вы успешно купили улучшение!', show_alert=True)
    else:
        await callback.answer('Недостаточно денег в казне клана', show_alert=True)

@router.callback_query(F.data == 'Пополнить казну')
async def clan_bank_up(callback: CallbackQuery, state: FSMContext):
    agree = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Отмена', callback_data='nope')
            ]
        ]
    )
    user_money = await get.get_money(callback.from_user.id)
    await callback.message.answer(f'Ваш баланс: {user_money}\nВведите ссумму пополнения:', reply_markup=agree)
    await state.set_state(Clan.money)


async def clan_kb(callback: CallbackQuery):
    all_clans = await get.get_clans()
    length = len(all_clans)
    if callback.data.startswith('Далее_') or callback.data.startswith('Назад_'):
        if str(callback.data[:6]) == 'Далее_':
            i = int(callback.data[6:])
            i += 1
        else:
            i = int(callback.data[6:])
            i -= 1
    else:
        i = 1

    key = InlineKeyboardBuilder()
    if i == 1:
        for clan in all_clans[:8]:
            members = await get.get_members(clan)
            clans = key.add(InlineKeyboardButton(text=f'{clan} {members}/20', callback_data=f'name_{clan}'))
            clans.adjust(2)
        if length / i > 8:
            next = key.add(InlineKeyboardButton(text='Далее', callback_data=f'Далее_{i}'))
            next.adjust(2)
    else:
        if i*8 >= length:
            for clan in all_clans[(i-1)*8:i*8]:
                members = await get.get_members(clan)
                clans = key.add(InlineKeyboardButton(text=f'{clan} {members}/20', callback_data=f'name_{clan}'))
                clans.adjust(2)
            if length / i > 8:
                next = key.add(InlineKeyboardButton(text='Далее', callback_data=f'Далее_{i}'))
                next.adjust(2)
        elif i*8 <= length:
            if length < (i+1)*8:
                for clan in all_clans[(i-1)*8:length]:
                    members = await get.get_members(clan)
                    clans = key.add(InlineKeyboardButton(text=f'{clan} {members}/20', callback_data=f'name_{clan}'))
                    clans.adjust(2)
            for clan in all_clans[(i-1)*8:length-1]:
                members = await get.get_members(clan)
                clans = key.add(InlineKeyboardButton(text=f'{clan} {members}/20', callback_data=f'name_{clan}'))
                clans.adjust(2)
            if length / i > 8:
                next = key.add(InlineKeyboardButton(text='Далее', callback_data=f'Далее_{i}'))
                next.adjust(2)
        back = key.add(InlineKeyboardButton(text='Назад', callback_data=f'Назад_{i}'))
        back.adjust(2)
    if length == 0:
        await callback.answer('Открытых кланов нету.', show_alert=True)
        return None
    else:
        return clans.as_markup()


@router.callback_query(F.data == 'Вступить в открытый клан')
async def clan_open_clan(callback: CallbackQuery):
    if await clan_kb(callback) != None:
        await callback.message.edit_reply_markup(reply_markup=await clan_kb(callback))

@router.callback_query(F.data.startswith('name_'))
async def clan_open_clan(callback: CallbackQuery):
    Clan_add.name = str(callback.data.replace('name_', ''))
    yes = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Вступить', callback_data='Вступить'),
                InlineKeyboardButton(text='Назад', callback_data='Назад')
            ]
        ]
    )
    clan_name = str(callback.data.replace('name_', ''))
    clan_owner_tg_id = await get.get_clan_owner_by_name(clan_name)
    type = await get.get_clan_type(clan_owner_tg_id)
    if type == 0:
        type = 'OPEN'
    else:
        type = 'PRIVATE'
    if await get.get_clan_photo(clan_owner_tg_id) == '':
        name = await get.get_clan_name(clan_owner_tg_id)
        money = await get.get_clan_money(clan_owner_tg_id)
        count = await get.get_clan_members(clan_owner_tg_id)
        users_money = await get.get_clan_users_money(clan_owner_tg_id)
        money_chance = await get.get_clan_money_chance(clan_owner_tg_id)
        boost_chance = await get.get_clan_boost_chance(clan_owner_tg_id)
        code = await get.get_clan_code(clan_owner_tg_id)
        await callback.message.answer_photo(
            photo='AgACAgIAAxkBAAJgPWaP6DS_Mee7DI9CGYUGd-RHHqY2AALP3jEbNceASMYNm_KYutUrAQADAgADeQADNQQ',
            caption=f'Название клана: {name}\n\n'
                    f'Денег в казне: {money}\n'
                    f'Кол-во участников: {count}\n'
                    f'Деньги всех участников: {users_money}\n'
                    f'Доп. шанс выпадения игровой валюты: {money_chance}\n'
                    f'Доп. шанс выпадения бустов: {boost_chance}\n'
                    f'Тип клана - {type}\n'
                    f'Код для вступления: {code}',
            reply_markup=yes)
    else:
        name = await get.get_clan_name(clan_owner_tg_id)
        photo = await get.get_clan_photo(clan_owner_tg_id)
        money = await get.get_clan_money(clan_owner_tg_id)
        count = await get.get_clan_members(clan_owner_tg_id)
        users_money = await get.get_clan_users_money(clan_owner_tg_id)
        money_chance = await get.get_clan_money_chance(clan_owner_tg_id)
        boost_chance = await get.get_clan_boost_chance(clan_owner_tg_id)
        code = await get.get_clan_code(clan_owner_tg_id)
        await callback.message.answer_photo(
            photo=f'{photo}',
            caption=f'Название клана: {name}\n\n'
                    f'Денег в казне: {money}\n'
                    f'Кол-во участников: {count}\n'
                    f'Деньги всех участников: {users_money}\n'
                    f'Доп. шанс выпадения игровой валюты: {money_chance}\n'
                    f'Доп. шанс выпадения бустов: {boost_chance}\n'
                    f'Тип клана - {type}\n'
                    f'Код для вступления: {code}',
            reply_markup=yes)


@router.callback_query(F.data == 'Вступить')
async def clan_private_clan(callback: CallbackQuery, bot: Bot):
    clan_name = Clan_add.name
    owner = await get.get_clan_owner_by_name(clan_name)
    name = await get.get_clan_name(owner)
    nickname = await get.get_user_nickname(callback.from_user.id)
    await set.set_user_clan(callback.from_user.id, int(f'892352{owner}'))
    await callback.message.answer(f'Вы подали заявку в клан {name}')
    await bot.send_message(owner, f'Новая заявка на вступление в клан от {nickname}')


@router.callback_query(F.data == 'Вступить по коду')
async def clan_private_clan(callback: CallbackQuery, state: FSMContext):
    break_input = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Отмена', callback_data='break_code')
            ]
        ]
    )
    await callback.message.answer('Введите код клана:', reply_markup=break_input)
    await state.set_state(Clan.code)
    await asyncio.sleep(300)
    await state.clear()

@router.callback_query(F.data == 'break_code')
async def clan_private_clan(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer('Вы успешно отменили ввод кода')


@router.callback_query(F.data.startswith('Далее_'))
async def clan_next(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await clan_kb(callback))

@router.callback_query(F.data.startswith('Назад_'))
async def clan_back(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await clan_kb(callback))


@router.callback_query(F.data.startswith('next_'))
async def clan_next(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await del_from_clan(callback))

@router.callback_query(F.data.startswith('back_'))
async def clan_back(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await del_from_clan(callback))


@router.callback_query(F.data == 'Выйти из клана')
async def clan_delete(callback: CallbackQuery):
    agree = InlineKeyboardMarkup(
            inline_keyboard=[
            [
                InlineKeyboardButton(text='Да', callback_data='Выйти'),
                InlineKeyboardButton(text='Нет', callback_data='Не выходить')
            ]
        ]
    )
    type = await get.get_clan_type(callback.from_user.id)
    if type == 0:
        type = 'OPEN'
    else:
        type = 'PRIVATE'
    name = await get.get_clan_name(callback.from_user.id)
    money = await get.get_clan_money(callback.from_user.id)
    count = await get.get_clan_members(callback.from_user.id)
    users_money = await get.get_clan_users_money(callback.from_user.id)
    money_chance = await get.get_clan_money_chance(callback.from_user.id)
    boost_chance = await get.get_clan_boost_chance(callback.from_user.id)
    await callback.message.edit_caption(
        caption=f'Название клана: {name}\n\n'
                f'Денег в казне: {money}\n'
                f'Кол-во участников: {count}\n'
                f'Деньги всех участников: {users_money}\n'
                f'Доп. шанс выпадения игровой валюты: {money_chance}\n'
                f'Доп. шанс выпадения бустов: {boost_chance}\n'
                f'Тип клана - {type}\n\n'
                'ВЫ УВЕРЕНЫ, ЧТО ХОТИТЕ ПОКИНУТЬ КЛАН??',
        reply_markup=agree)


@router.callback_query(F.data == 'Выйти')
async def clan_delete(callback: CallbackQuery):
    name = await get.get_clan_name(callback.from_user.id)
    await minus.minus_clan_member(callback.from_user.id)
    await set.set_user_clan(callback.from_user.id, 0)

    await callback.message.answer(f'Вы покинули клан {name}...')

@router.callback_query(F.data == 'Не выходить')
async def clan_delete(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await owner_main_kb(callback.from_user.id))


async def add_to_clan(callback: CallbackQuery):
    all_members = await get.get_clan_name_to_add_members(callback.from_user.id)
    length = len(all_members)
    if callback.data.startswith('add_next_') or callback.data.startswith('add_back_'):
        if str(callback.data[:9]) == 'add_next_':
            i = int(callback.data[9:])
            i += 1
        else:
            i = int(callback.data[9:])
            i -= 1
    else:
        i = 1
    key = InlineKeyboardBuilder()
    if i == 1:
        for member in all_members[:8]:
            clans = key.add(InlineKeyboardButton(text=f'{member}', callback_data=f'_add_{member}'))
            clans.adjust(2)
        if length / i > 8:
            next = key.add(InlineKeyboardButton(text='Далее', callback_data=f'add_next_{i}'))
            next.adjust(2)
    else:
        if i * 8 >= length:
            for member in all_members[(i - 1) * 8:i * 8]:
                clans = key.add(InlineKeyboardButton(text=f'{member}', callback_data=f'_add_{member}'))
                clans.adjust(2)
            if length / i > 8:
                next = key.add(InlineKeyboardButton(text='Далее', callback_data=f'add_next_{i}'))
                next.adjust(2)
        elif i * 8 <= length:
            if length < (i + 1) * 8:
                for member in all_members[(i - 1) * 8:length]:
                    clans = key.add(InlineKeyboardButton(text=f'{member}', callback_data=f'_add_{member}'))
                    clans.adjust(2)
            for member in all_members[(i - 1) * 8:length - 1]:
                clans = key.add(InlineKeyboardButton(text=f'{member}', callback_data=f'_add_{member}'))
                clans.adjust(2)
            if length / i > 8:
                next = key.add(InlineKeyboardButton(text='Далее', callback_data=f'add_next_{i}'))
                next.adjust(2)
        back = key.add(InlineKeyboardButton(text='Назад', callback_data=f'add_back_{i}'))
        back.adjust(2)
    if length == 0:
        await callback.answer('Заявок нет.', show_alert=True)
        return await owner_main_kb(callback.from_user.id)
    else:
        return clans.as_markup()


@router.callback_query(F.data == 'Заявки')
async def clan_delete(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await add_to_clan(callback))

@router.callback_query(F.data.startswith('_add'))
async def clan_add(callback: CallbackQuery):
    Clan_add.nickname_add = str(callback.data.replace('_add_', ''))
    add = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Принять', callback_data='Принять'),
                InlineKeyboardButton(text='Отклонить', callback_data='Отклонить')
            ]
        ]
    )
    nickname = Clan_add.nickname_add
    user = await get.user_tg_id_by_nickname(nickname)
    money = await get.get_money(user)
    place = [0, 0, 0]
    a = 0
    b = 0
    c = 0
    top_alltime_money = await get.get_top_alltime_money()
    top_money = await get.get_top_money()
    top_referrals = await get.get_top_referrals()
    for item in top_alltime_money:
        a += 1
        if item == user:
            place[0] = a

    for item in top_money:
        b += 1
        if item == user:
            place[1] = b

    for item in top_referrals:
        c += 1
        if item == user:
            place[2] = c
    await callback.message.edit_caption(
        caption=f'Игрок {nickname}\n\n'
                f'Баланс игрока: <b>{money}</b> шишек 🌰!\n\n'
                f'Шанс выпадения шишек 🌰:<b>{await get.get_money_chance(user)}%</b>'
                f'\nШанс выпадения бустов 🔋:<b>{await get.get_boost_chance(user)}%</b>'
                f'\n\nИгрок топ <b>{place[0]}</b> по заработанному за всё время! 💸'
                f'\nИгрок топ <b>{place[1]}</b> по деньгам! 🔥'
                f'\nИгрок топ <b>{place[2]}</b> по приглашённым пользователям! 👨‍💼',
        reply_markup=add, parse_mode=ParseMode.HTML)

@router.callback_query(F.data.startswith('add_next_'))
async def clan_add_next(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await add_to_clan(callback))

@router.callback_query(F.data.startswith('add_back_'))
async def clan_add_back(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=await add_to_clan(callback))


@router.callback_query(F.data == 'Принять')
async def clan_type_clan(callback: CallbackQuery, bot: Bot):
    nickname = Clan_add.nickname_add
    user = await get.user_tg_id_by_nickname(nickname)
    name = await get.get_clan_name(callback.from_user.id)
    alltime_money = await get.get_alltime_money(callback.from_user.id)
    await add.update_clan_users_money(callback.from_user.id, alltime_money)
    await add.add_clan_member(callback.from_user.id)
    await set.set_user_clan(user, callback.from_user.id)

    await callback.answer(f'Вы приняли в клан {nickname}!', show_alert=True)
    await bot.send_message(user, f'Вас приняли в клан {name}')


@router.callback_query(F.data == 'Отклонить')
async def clan_type_clan(callback: CallbackQuery, bot: Bot):
    nickname = Clan_add.nickname_add
    user = await get.user_tg_id_by_nickname(nickname)
    name = await get.get_clan_name(callback.from_user.id)
    await set.set_user_clan(user, 0)

    await callback.answer(f'Вы отклонили заявку в клан {nickname}!', show_alert=True)
    await bot.send_message(user, f'Вашу заявку в клан {name} отклонили...')