from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

import asyncio
import database.requests.get as get
import database.requests.add as add
import database.requests.minus as minus
import keyboards.inline as kb
import random


descriptions = [
        'шанс выпадения шишек увеличен на 5% на 1 минуту',
        'шансы выпадения игровой валюты и бустов увеличены на 5% на 1 минуту',
        'шансы выпадения игровой валюты и бустов увеличены на 10% на 1 минуту',
        'шансы выпадения игровой валюты и бустов навсегда увеличены на 0.1 %',
        'шансы выпадения игровой валюты и бустов увеличены на 15 % на 1 минуту'
    ]
boosts_chances = [0.0, 5.0, 10.0, 0.1, 15.0]
money_chances = [5.0, 5.0, 10.0, 0.1, 15.0]


from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))


@router.message(F.text == 'Украсть шишки 🌰')
async def steal(message: Message):
    r = random.uniform(1.0, 100.0)
    if r <= await get.get_money_chance(message.from_user.id):
        money = random.randint(100, 4100)
        r = random.uniform(1.0, 100.0)
        if r <= await get.get_boost_chance(message.from_user.id):
            ra = random.randint(0, 4)
            if ra == 0:
                await message.answer_photo(
                    photo='AgACAgIAAxkBAAJZYGZ1ui9ST0z2MoVAMW5bN0fDFSWmAAIl3TEbUYiwSzoPzVsxTI7DAQADAgADeQADNQQ',
                    caption=f'Вы попытали свою удачy!\nВы украли <b>{money}</b> шишек 🌰!\n\n Ого! Вам крупно повезло! Ваш {descriptions[ra]} ',
                    reply_markup=kb.steal, parse_mode=ParseMode.HTML)
                await add.add_money(message.from_user.id, money)
                await add.add_alltime_money(message.from_user.id, money)
                await add.update_clan_users_money(message.from_user.id, money)
                chance = money_chances[ra]
                if await get.get_money_chance(message.from_user.id) < 45.0:
                    await add.add_money_chance(message.from_user.id, chance)
                    await asyncio.sleep(60)
                    await minus.minus_money_chance(message.from_user.id, chance)
            elif ra == 3:
                await message.answer_photo(
                    photo='AgACAgIAAxkBAAJZYGZ1ui9ST0z2MoVAMW5bN0fDFSWmAAIl3TEbUYiwSzoPzVsxTI7DAQADAgADeQADNQQ',
                    caption=f'Вы попытали свою удачy!\nВы украли <b>{money}</b> шишек 🌰!\n\nОго! Вам крупно повезло! Ваши {descriptions[ra]}',
                    reply_markup=kb.steal, parse_mode=ParseMode.HTML)
                await add.add_money(message.from_user.id, money)
                await add.add_alltime_money(message.from_user.id, money)
                await add.update_clan_users_money(message.from_user.id, money)
                chance = money_chances[ra]
                if await get.get_money_chance(message.from_user.id) < 45.0:
                    await add.add_money_chance(message.from_user.id, chance)
                    if await get.get_money_chance(message.from_user.id) < 45.0:
                        await add.add_boost_chance(message.from_user.id, chance)
            else:
                await message.answer_photo(
                    photo='AgACAgIAAxkBAAJZYGZ1ui9ST0z2MoVAMW5bN0fDFSWmAAIl3TEbUYiwSzoPzVsxTI7DAQADAgADeQADNQQ',
                    caption=f'Вы попытали свою удачy!\nВы украли <b>{money}</b> шишек 🌰!\n\nОго! Вам крупно повезло! Ваши {descriptions[ra]}',
                    reply_markup=kb.steal, parse_mode=ParseMode.HTML)
                await add.add_money(message.from_user.id, money)
                await add.add_alltime_money(message.from_user.id, money)
                await add.update_clan_users_money(message.from_user.id, money)
                if await get.get_money_chance(message.from_user.id) < 45.0:
                    chance = money_chances[ra]
                    await add.add_money_chance(message.from_user.id, chance)
                    if await get.get_boost_chance(message.from_user.id) < 45.0:
                        await add.add_boost_chance(message.from_user.id, chance)
                        await asyncio.sleep(60)
                        await minus.minus_boost_chance(message.from_user.id, chance)
                        await minus.minus_money_chance(message.from_user.id, chance)
        else:
            await message.answer_photo(
                photo='AgACAgIAAxkBAAJY_mZ0Shb6-gEJ0gvWTCotNMX5wLi0AAIt4DEbfl2oS2pMPLmZ_5PCAQADAgADcwADNQQ',
                caption=f'Вы попытали свою удачy!\nВы украли <b>{money}</b> шишек 🌰!\nВам крупно повезло!',
                reply_markup=kb.steal, parse_mode=ParseMode.HTML)
            await add.add_money(message.from_user.id, money)
            await add.add_alltime_money(message.from_user.id, money)
            await add.update_clan_users_money(message.from_user.id, money)
    else:
        await message.answer_photo(
            photo='AgACAgIAAxkBAAJY_mZ0Shb6-gEJ0gvWTCotNMX5wLi0AAIt4DEbfl2oS2pMPLmZ_5PCAQADAgADcwADNQQ',
            caption='Вы попытали свою удачу!\nУ вас <b>не получилось</b> что-то украсть,\n<ins>но не расстраивайтесь</ins>,у вас всё получится!',
            reply_markup=kb.steal, parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'Украсть шишки 🌰')
async def callback_steal(callback: CallbackQuery):
    r = random.uniform(1.0, 100.0)
    if r <= await get.get_money_chance(callback.from_user.id):
        money = random.randint(100, 4100)
        r = random.uniform(1.0, 100.0)
        if r <= await get.get_boost_chance(callback.from_user.id):
            ra = random.randint(0, 4)
            if ra == 0:
                await callback.message.answer_photo(
                    photo='AgACAgIAAxkBAAJZYGZ1ui9ST0z2MoVAMW5bN0fDFSWmAAIl3TEbUYiwSzoPzVsxTI7DAQADAgADeQADNQQ',
                    caption=f'Вы попытали свою удачy!\nВы украли <b>{money}</b> шишек 🌰!\n\n Ого! Вам крупно повезло! Ваш {descriptions[ra]} ',
                    reply_markup=kb.steal, parse_mode=ParseMode.HTML)
                await add.add_money(callback.from_user.id, money)
                await add.add_alltime_money(callback.from_user.id, money)
                await add.update_clan_users_money(callback.from_user.id, money)
                if await get.get_money_chance(callback.from_user.id) < 45.0:
                    chance = money_chances[ra]
                    await add.add_money_chance(callback.from_user.id, chance)
                    await asyncio.sleep(60)
                    await minus.minus_money_chance(callback.from_user.id, chance)

            elif ra == 3:
                await callback.message.answer_photo(
                    photo='AgACAgIAAxkBAAJZYGZ1ui9ST0z2MoVAMW5bN0fDFSWmAAIl3TEbUYiwSzoPzVsxTI7DAQADAgADeQADNQQ',
                    caption=f'Вы попытали свою удачy!\nВы украли <b>{money}</b> шишек 🌰!\n\nОго! Вам крупно повезло! Ваши {descriptions[ra]}',
                    reply_markup=kb.steal, parse_mode=ParseMode.HTML)
                await add.add_money(callback.from_user.id, money)
                await add.add_alltime_money(callback.from_user.id, money)
                await add.update_clan_users_money(callback.from_user.id, money)
                if await get.get_money_chance(callback.from_user.id) < 45.0:
                    chance = money_chances[ra]
                    await add.add_money_chance(callback.from_user.id, chance)
                    if await get.get_boost_chance(callback.from_user.id) < 45.0:
                        await add.add_boost_chance(callback.from_user.id, chance)
            else:
                await callback.message.answer_photo(
                    photo='AgACAgIAAxkBAAJZYGZ1ui9ST0z2MoVAMW5bN0fDFSWmAAIl3TEbUYiwSzoPzVsxTI7DAQADAgADeQADNQQ',
                    caption=f'Вы попытали свою удачy!\nВы украли <b>{money}</b> шишек 🌰!\n\nОго! Вам крупно повезло! Ваши {descriptions[ra]}',
                    reply_markup=kb.steal, parse_mode=ParseMode.HTML)
                await add.add_money(callback.from_user.id, money)
                await add.add_alltime_money(callback.from_user.id, money)
                await add.update_clan_users_money(callback.from_user.id, money)
                if await get.get_money_chance(callback.from_user.id) < 45.0:
                    chance = money_chances[ra]
                    await add.add_money_chance(callback.from_user.id, chance)
                    if await get.get_boost_chance(callback.from_user.id) < 45.0:
                        await add.add_boost_chance(callback.from_user.id, chance)
                        await asyncio.sleep(60)
                        await minus.minus_boost_chance(callback.from_user.id, chance)
                        await minus.minus_money_chance(callback.from_user.id, chance)
        else:
            await callback.message.answer_photo(photo='AgACAgIAAxkBAAJY_mZ0Shb6-gEJ0gvWTCotNMX5wLi0AAIt4DEbfl2oS2pMPLmZ_5PCAQADAgADcwADNQQ',
                                                caption=f'Вы попытали свою удачy!\nВы украли {money} шишек 🌰!\nВам крупно повезло!',
                                                reply_markup=kb.steal, parse_mode=ParseMode.HTML)

            await add.add_money(callback.from_user.id, money)
            await add.add_alltime_money(callback.from_user.id, money)
            await add.update_clan_users_money(callback.from_user.id, money)
    else:
        await callback.message.answer_photo(
            photo='AgACAgIAAxkBAAJY_mZ0Shb6-gEJ0gvWTCotNMX5wLi0AAIt4DEbfl2oS2pMPLmZ_5PCAQADAgADcwADNQQ',
            caption='Вы попытали свою удачу!\nУ вас <b>не получилось</b> что-то украсть,\n<ins>но не расстраивайтесь</ins>,у вас всё получится!',
            reply_markup=kb.steal, parse_mode=ParseMode.HTML)
