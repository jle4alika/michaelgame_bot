from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

import asyncio
import database.requests.get as get
import database.requests.add as add
import database.requests.minus as minus
import database.requests.others as set
import keyboards.inline as kb
import random

from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))

@router.message(F.text == 'Рыбацкая бухта ⚓')
async def event_main(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAJlPGab8g_mkzx8nALZZWcbn70J7MT6AAJs9zEbw_HgSP0eMYPk5dX_AQADAgADeAADNQQ',
                               caption='Привет, рад тебя видеть! Здесь всегда происходит что-то интересное. Куда ты хотел бы отправиться?\n\n'
                                       '1. <b>Медведь</b> – Место силы медведя для авантюристов.\n'
                                       '2. <b>Кража!</b> – Настоящая авантюра для тех, кто любит пошалить.\n'
                                       '3. <b>Рыбачить</b> – Идеальное место для спокойного отдыха на природе.\n'
                                       '4. <b>Рыболовный магазин</b> – Обнови своё снаряжение лучшими новинками для успешной рыбалки.\n\n'
                                       'Выбирай своё приключение и вперед! 🎣🚣‍♂️🕵️‍♂️',
                               reply_markup=kb.event_main,
                               parse_mode=ParseMode.HTML)
    await set.set_user_event(message.from_user.id)

@router.callback_query(F.data == 'Рыбачить')
async def event_main(callback: CallbackQuery):
    chance = await get.get_fishing_chance(callback.from_user.id)
    if random.randint(0, 100) <= chance:
        await add.add_fish(callback.from_user.id, 1)
        fish = await get.get_fish(callback.from_user.id)
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAJlPGab8g_mkzx8nALZZWcbn70J7MT6AAJs9zEbw_HgSP0eMYPk5dX_AQADAgADeAADNQQ',
                                            caption='Поздравляю! Ты поймал свою рыбку! 🐟 Это\n'
                                                    'впечатляющее начало твоего рыболовного приключения.\n'
                                                    'Неважно, большая она или маленькая, сейчас ты понимаешь,\n'
                                                    'что усилия окупаются. Продолжай в том же духе, совершенствуй \n'
                                                    'свои навыки, и, кто знает, возможно, следующая рыбалка\n'
                                                    'принесёт тебе ещё больший улов. Дерзай! 🎣🚀'
                                                    f'Ваша рыба: {fish}',
                                            reply_markup=kb.event_fishing)
    else:
        await callback.message.answer_photo(photo='AgACAgIAAxkBAAJlPGab8g_mkzx8nALZZWcbn70J7MT6AAJs9zEbw_HgSP0eMYPk5dX_AQADAgADeAADNQQ',
                                            caption='Не расстраивайся, что сегодня улов не удался! 🐟 Рыбалка – это \n'
                                                    'не только о рыбе, но и о времени, проведённом на природе, о\n'
                                                    'тишине и спокойствии. Это шанс научиться терпению и\n'
                                                    'совершенствовать свои навыки. Каждый неудавшийся заброс\n'
                                                    'приближает тебя к моменту, когда клёв пойдёт как по маслу.\n'
                                                    'Продолжай практиковаться, и твой улов обязательно будет! 🎣💪\n',
                                            reply_markup=kb.event_fishing)


@router.callback_query(F.data == 'Рыболовный магазин')
async def event_main(callback: CallbackQuery):
    fishing_chance = await get.get_fishing_chance(callback.from_user.id)
    fishing1 = await get.get_fishing1(callback.from_user.id)
    fishing2 = await get.get_fishing2(callback.from_user.id)
    fishing3 = await get.get_fishing3(callback.from_user.id)
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAJlQWab9cERsvVGGqDJebtGQ_NTq4QWAAJ94jEbFTjhSBhK0SvxZ5feAQADAgADeQADNQQ',
                                        caption='Как я вижу ты настроен серьёзно. Вот тебе наш ассортимент, выбирай всё по очереди!\n\n'
                                                '• Обновка 🎣! \nНовая удочка поднимает шансы то 10% (Стоимость 5 рыб и 150тыс шишек)\n'
                                                '• Вкуснотища 🐛! \nНовая приманка поднимает шансы ловли до 15% (Стоимость 15 рыб и 250 тыс шишек)\n'
                                                '• По течению вверх 🌊! \nНовая надувная лодка для ловли, поднимает шанс выпадения до 20%. (Стоимость 25 рыб и 350 тыс шишек)\n'
                                                f'Ваш шанс поимки рыбы: {fishing_chance}%',
                                        reply_markup=kb.event_fishing_shop)

@router.callback_query(F.data == 'Обновка!')
async def event_new(callback: CallbackQuery):
    if await get.get_fishing1(callback.from_user.id) == 0:
        if await get.get_money(callback.from_user.id) >= 150000:
            if await get.get_fish(callback.from_user.id) >= 5:
                await minus.minus_money(callback.from_user.id, 150000)
                await minus.minus_fish(callback.from_user.id, 5)
                await add.update_fishing_chance(callback.from_user.id, 10)
                await add.update_fishing1(callback.from_user.id)
                await callback.message.answer_photo(photo='AgACAgIAAxkBAAJlRmacASyxSbutWudBN_8AATgmCPrh5gACe94xGzSQ4UgGHNQjoZGLKgEAAwIAA3gAAzUE',
                                                    caption='Вы успешно приобрели новую удочку 🎣 и повысили ваши шансы до 10%!\nС обновкой!',
                                                    reply_markup=kb.event_fishing_shop)
            else:
                await callback.answer('Недостаточно рыб для оплаты.', show_alert=True)
        else:
            await callback.answer('Недостаточно шишек для оплаты.', show_alert=True)
    else:
        await callback.answer('Вы уже приобрели первое улучшение.', show_alert=True)

@router.callback_query(F.data == 'Вкуснотища!')
async def event_delicious(callback: CallbackQuery):
    if await get.get_fishing1(callback.from_user.id) == 1:
        if await get.get_fishing2(callback.from_user.id) == 0:
            if await get.get_money(callback.from_user.id) >= 250000:
                if await get.get_fish(callback.from_user.id) >= 15:
                    await minus.minus_money(callback.from_user.id, 250000)
                    await minus.minus_fish(callback.from_user.id, 15)
                    await add.update_fishing_chance(callback.from_user.id, 15)
                    await add.update_fishing2(callback.from_user.id)
                    await callback.message.answer_photo(photo='AgACAgIAAxkBAAJlS2acAWFpifz9K5rZd-FCyD_1c7BfAALC4jEbFTjhSCaVhCiBV_zDAQADAgADeAADNQQ',
                                                        caption='Вы успешно приобрели новую приманку 🐛 и повысили ваши шансы до 15%!\nС обновкой!',
                                                        reply_markup=kb.event_fishing_shop)
                else:
                    await callback.answer('Недостаточно рыб для оплаты.', show_alert=True)
            else:
                await callback.answer('Недостаточно шишек для оплаты.', show_alert=True)
        else:
            await callback.answer('Вы уже пробрели приманку!', show_alert=True)
    else:
        await callback.answer('Вы не приобрели удочку!', show_alert=True)

@router.callback_query(F.data == 'По течению вверх!')
async def event_up(callback: CallbackQuery):
    if await get.get_fishing2(callback.from_user.id) == 1:
        if await get.get_fishing3(callback.from_user.id) == 0:
            if await get.get_money(callback.from_user.id) >= 350000:
                if await get.get_fish(callback.from_user.id) >= 25:
                    await minus.minus_money(callback.from_user.id, 350000)
                    await minus.minus_fish(callback.from_user.id, 25)
                    await add.update_fishing_chance(callback.from_user.id, 20)
                    await add.update_fishing3(callback.from_user.id)
                    await callback.message.answer_photo(photo='AgACAgIAAxkBAAJlUGacAYi-Mz_it1dSAqPaMfc2vGSPAALR4jEbFTjhSHCx5B7X_M9NAQADAgADeQADNQQ',
                                                        caption='Вы успешно приобрели новую лодку 🌊 и повысили ваши шансы до 20%!\nС обновкой!',
                                                        reply_markup=kb.event_fishing_shop)
                else:
                    await callback.answer('Недостаточно рыб для оплаты.', show_alert=True)
            else:
                await callback.answer('Недостаточно шишек для оплаты.', show_alert=True)
        else:
            await callback.answer('Вы уже пробрели лодку!', show_alert=True)
    else:
        await callback.answer('Вы не приобрели приманку!', show_alert=True)


@router.callback_query(F.data == 'Медведь')
async def bear(callback: CallbackQuery):
    bear_power = await get.get_bear_power(callback.from_user.id)
    bear_protection = await get.get_bear_protection(callback.from_user.id)
    fish = await get.get_fish(callback.from_user.id)
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAJlimac7Hwm5y9OC6EWS3NQ1dTaB_RRAAKv3jEbU5TpSGcaUwbbMBcrAQADAgADeAADNQQ',
                                        caption=
                                        'Медвежий угол 🐻\n\n'
                                        'Добро пожаловать в обитель могучего медведя! Здесь ты можешь усилить своего косолапого друга и сделать его непобедимым.\n\n'
                                        '---\n\n'
                                        f'<b>Ваша рыба:</b> {fish}\n'
                                        f'<b>Сила атаки:</b> {bear_power}\n'
                                        f'<b>Защита:</b> {bear_protection}\n\n'
                                        '---\n\n'
                                        'Береги своего могучего медведя и улучшай его характеристики, чтобы вместе покорять новые вершины!',
                                        reply_markup=kb.event_bear,
                                        parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'Повысить силу атаки медведя')
async def bear(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=kb.event_up_power)


@router.callback_query(F.data == 'Повысить защиту медведя')
async def bear(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=kb.event_up_protection)

@router.callback_query(F.data == '1 power')
async def event_change(callback: CallbackQuery):
    bear_power = await get.get_bear_power(callback.from_user.id)
    if bear_power < 100:
        if await get.get_fish(callback.from_user.id) >= 1:
            await minus.minus_fish(callback.from_user.id, 1)
            await add.add_bear_power(callback.from_user.id, 1)
            bear_power = await get.get_bear_power(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли силу атаки на 1%!\nСила атаки медведя: {bear_power}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять силу атаки выше 100%.')

@router.callback_query(F.data == '3 power')
async def event_change(callback: CallbackQuery):
    bear_power = await get.get_bear_power(callback.from_user.id)
    if bear_power < 98:
        if await get.get_fish(callback.from_user.id) >= 3:
            await minus.minus_fish(callback.from_user.id, 3)
            await add.add_bear_power(callback.from_user.id, 3)
            bear_power = await get.get_bear_power(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли силу атаки на 3%!\nСила атаки медведя: {bear_power}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять силу атаки выше 100%.')


@router.callback_query(F.data == '5 power')
async def event_change(callback: CallbackQuery):
    bear_power = await get.get_bear_power(callback.from_user.id)
    if bear_power < 96:
        if await get.get_fish(callback.from_user.id) >= 5:
            await minus.minus_fish(callback.from_user.id, 5)
            await add.add_bear_power(callback.from_user.id, 5)
            bear_power = await get.get_bear_power(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли силу атаки на 5%!\nСила атаки медведя: {bear_power}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять силу атаки выше 100%.')

@router.callback_query(F.data == '10 power')
async def event_change(callback: CallbackQuery):
    bear_power = await get.get_bear_power(callback.from_user.id)
    if bear_power < 91:
        if await get.get_fish(callback.from_user.id) >= 10:
            await minus.minus_fish(callback.from_user.id, 10)
            await add.add_bear_power(callback.from_user.id, 10)
            bear_power = await get.get_bear_power(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли силу атаки на 10%!\nСила атаки медведя: {bear_power}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять силу атаки выше 100%.')

@router.callback_query(F.data == '1 protection')
async def event_change(callback: CallbackQuery):
    bear_protection = await get.get_bear_protection(callback.from_user.id)
    if bear_protection < 79:
        if await get.get_fish(callback.from_user.id) >= 1:
            await minus.minus_fish(callback.from_user.id, 1)
            await add.add_bear_protection(callback.from_user.id, 1)
            bear_protection = await get.get_bear_protection(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли защиту на 1%!\n Защита: {bear_protection}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять защиту выше 80%.')

@router.callback_query(F.data == '3 protection')
async def event_change(callback: CallbackQuery):
    bear_protection = await get.get_bear_protection(callback.from_user.id)
    if bear_protection < 78:
        if await get.get_fish(callback.from_user.id) >= 3:
            await minus.minus_fish(callback.from_user.id, 3)
            await add.add_bear_protection(callback.from_user.id, 3)
            bear_protection = await get.get_bear_protection(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли защиту на 3%!\n Защита: {bear_protection}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять защиту выше 80%.')


@router.callback_query(F.data == '5 protection')
async def event_change(callback: CallbackQuery):
    bear_protection = await get.get_bear_protection(callback.from_user.id)
    if bear_protection < 76:
        if await get.get_fish(callback.from_user.id) >= 5:
            await minus.minus_fish(callback.from_user.id, 5)
            await add.add_bear_protection(callback.from_user.id, 5)
            bear_protection = await get.get_bear_protection(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли защиту на 5%!\n Защита: {bear_protection}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять защиту выше 80%.')

@router.callback_query(F.data == '10 protection')
async def event_change(callback: CallbackQuery):
    bear_protection = await get.get_bear_protection(callback.from_user.id)
    if bear_protection < 71:
        if await get.get_fish(callback.from_user.id) >= 10:
            await minus.minus_fish(callback.from_user.id, 10)
            await add.add_bear_protection(callback.from_user.id, 10)
            bear_protection = await get.get_bear_protection(callback.from_user.id)
            await callback.answer(f'Вы успешно подняли защиту на 10%!\n Защита: {bear_protection}')
        else:
            await callback.answer('У вас недостаточно рыбы для обмена.')
    else:
        await callback.answer('Вы не можете поднять защиту выше 80%.')


@router.callback_query(F.data == 'bear_back')
async def event_change(callback: CallbackQuery):
    bear_power = await get.get_bear_power(callback.from_user.id)
    bear_protection = await get.get_bear_protection(callback.from_user.id)
    fish = await get.get_fish(callback.from_user.id)
    await callback.message.edit_caption(caption=
                                        'Медвежий угол 🐻\n\n'
                                        'Добро пожаловать в обитель могучего медведя! Здесь ты можешь усилить своего косолапого друга и сделать его непобедимым.\n\n'
                                        '---\n\n'
                                        f'<b>Ваша рыба:</b> {fish} 🐟\n'
                                        f'<b>Сила атаки:</b> {bear_power}\n'
                                        f'<b>Защита:</b> {bear_protection}\n\n'
                                        '---\n\n'
                                        'Береги своего могучего медведя и улучшай его характеристики, чтобы вместе покорять новые вершины!',
                                        reply_markup=kb.event_bear,
                                        parse_mode=ParseMode.HTML)
