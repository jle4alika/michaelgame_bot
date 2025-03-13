from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
from aiogram.enums import ParseMode
from handlers.chat_types import ThreadFilter
import asyncio
import database.requests.get as get
import database.requests.add as add
import database.requests.minus as minus
import database.requests.others as set
import keyboards.inline as kb
import random


router = Router()
router.message.filter(ThreadFilter(14))

@router.message(F.text.lower() == 'украсть')
async def event_steal(message: Message, bot: Bot):
    user = await get.get_user_bool(message.reply_to_message.from_user.id)
    atacker = await get.get_user_bool(message.from_user.id)

    if atacker:
        if message.reply_to_message.from_user.id == message.from_user.id:
            await message.answer('Вы не можете воровать у самого себя.')
        else:
            if user:
                user_money, user_fish = await get.get_money(
                    message.reply_to_message.from_user.id), await get.get_fish(
                    message.reply_to_message.from_user.id)
                power = await get.get_bear_power(message.from_user.id)
                max_money = 50000
                max_fish = 10
                money = max_money * (power / 100)
                fish = round(max_fish * (power / 100))
                if user_money >= money and user_fish >= fish:
                    if power != 0:
                        protection = await get.get_bear_protection(message.reply_to_message.from_user.id)
                        if random.randint(0, 100) <= 50 - (protection / 2):
                            await message.answer(f'Вы украли у пользователя {int(money)} 🌰 и {int(fish)} 🐟!')
                            await minus.minus_money(message.reply_to_message.from_user.id, money)
                            await minus.minus_fish(message.reply_to_message.from_user.id, fish)
                            await add.add_fish(message.from_user.id, fish)
                            await add.add_money(message.from_user.id, money)
                            await bot.send_message(message.reply_to_message.from_user.id,
                                                   f'У вас украли {int(money)} 🌰 и {int(fish)} 🐟',
                                                   reply_markup=kb.event_steal)
                        else:
                            await message.answer('У вас не получилось украсть деньги у пользователя.')
                    else:
                        await message.answer('Ваша сила атаки = 0.\n Для атаки необходим минимум 1%.')
                else:
                    await message.answer('У пользователя недостаточно шишек или рыбы 🐟.')
            else:
                await message.answer('Пользователь не найден.')
    else:
        await message.answer('Вы не зарегистрированы в боте.', reply_markup=kb.not_reg)


@router.edited_message(F.text.lower() == 'украсть')
async def event_steal(message: Message, bot: Bot):
    user = await get.get_user_bool(message.reply_to_message.from_user.id)
    atacker = await get.get_user_bool(message.from_user.id)

    if atacker:
        if message.reply_to_message.from_user.id == message.from_user.id:
            await message.answer('Вы не можете воровать у самого себя.')
        else:
            if user:
                user_money, user_fish = await get.get_money(
                    message.reply_to_message.from_user.id), await get.get_fish(
                    message.reply_to_message.from_user.id)
                power = await get.get_bear_power(message.from_user.id)
                max_money = 50000
                max_fish = 10
                money = max_money * (power / 100)
                fish = round(max_fish * (power / 100))
                if user_money >= money and user_fish >= fish:
                    if power != 0:
                        protection = await get.get_bear_protection(message.reply_to_message.from_user.id)
                        if random.randint(0, 100) <= 50 - (protection / 2):
                            await message.answer(f'Вы украли у пользователя {int(money)} 🌰 и {int(fish)} 🐟!')
                            await minus.minus_money(message.reply_to_message.from_user.id, money)
                            await minus.minus_fish(message.reply_to_message.from_user.id, fish)
                            await add.add_fish(message.from_user.id, fish)
                            await add.add_money(message.from_user.id, money)
                            await bot.send_message(message.reply_to_message.from_user.id,
                                                   f'У вас украли {int(money)} 🌰 и {int(fish)} 🐟',
                                                   reply_markup=kb.event_steal)
                        else:
                            await message.answer('У вас не получилось украсть деньги у пользователя.')
                    else:
                        await message.answer('Ваша сила атаки = 0.\n Для атаки необходим минимум 1%.')
                else:
                    await message.answer('У пользователя недостаточно шишек или рыбы 🐟.')
            else:
                await message.answer('Пользователь не найден.')
    else:
        await message.answer('Вы не зарегистрированы в боте.', reply_markup=kb.not_reg)
