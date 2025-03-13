import random
from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import database.requests.get as get
import database.requests.add as add
import database.requests.minus as minus
import database.requests.others as set
import keyboards.reply as kb
from aiogram.enums import ParseMode


from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))

class Reg(StatesGroup):
    nickname = State()
    photo_id = State()

class Clan(StatesGroup):
    name = State()
    name_again = State()
    clan_photo = State()
    code = State()
    money = State()

class Clan_add(StatesGroup):
    name = State()
    nickname = State()
    nickname_add = State()

async def create_code(message: Message):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 8
    code = ''
    counter = 0
    for i in range(length):
        code += random.choice(chars)
    for codes in await get.get_clans_codes(message.from_user.id):
        if codes == code:
            counter += 1
    if counter == 0:
        await add.add_clan_code(message.from_user.id, code)
    else:
        await create_code(message)

@router.message(Reg.nickname)
async def nickname(message: Message, state: FSMContext):
    nicknames = await get.get_all_nicknames(message.from_user.id)
    await state.update_data(nickname=message.text)
    data = message.text
    counter = 0
    for item in nicknames:
        if item == data:
            counter += 1
    if len(str(data)) > 18:
        await message.answer('Максимальная длинна ника - <ins>18 символов</ins>. Введите новый никнейм.', parse_mode=ParseMode.HTML)
    elif counter == 1:
        await message.answer('Данный ник уже <ins>занят</ins>. Введите другой никнейм.', parse_mode=ParseMode.HTML)
    else:
        await add.add_nickname(message.from_user.id, str(data))
        await state.clear()
        await message.answer(f'<b>{data}</b>, ваш никнейм успешно сохранён.\nТак же вы можете поменять ваш никнейм в любое время в профиле.', reply_markup=kb.main, parse_mode=ParseMode.HTML)


@router.message(F.photo, Reg.photo_id)
async def reg2(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await add.add_photo_id(message.from_user.id, message.photo[-1].file_id)
    await message.answer('Ваше фото профиля успешно изменено!')
    await state.clear()


@router.message(Clan.name)
async def clan_name(message: Message, state: FSMContext):
    nicknames = await get.get_clans_names(message.from_user.id)
    await state.update_data(name=message.text)
    data = message.text
    counter = 0
    for item in nicknames:
        if item == data:
            counter += 1
    if len(str(data)) > 18:
        await message.answer('Максимальная длинна названия - <ins>28 символов</ins>. Введите новое название.', parse_mode=ParseMode.HTML)
    elif counter == 1:
        await message.answer('Данное название уже <ins>занятo</ins>. Введите другое название.', parse_mode=ParseMode.HTML)
    else:
        await add.add_clan_name(message.from_user.id, str(data))
        await state.clear()
        await message.answer(f'<b>{data}</b>, название клана успешно сохранено.\nТак же вы можете поменять название клана в его настройках.', reply_markup=kb.main, parse_mode=ParseMode.HTML)

        await create_code(message)

        alltime_money = await get.get_alltime_money(message.from_user.id)
        await add.update_clan_users_money(message.from_user.id, alltime_money)

@router.message(Clan.name_again)
async def clan_name(message: Message, state: FSMContext):
    nicknames = await get.get_clans_names(message.from_user.id)
    await state.update_data(name=message.text)
    data = message.text
    counter = 0
    for item in nicknames:
        if item == data:
            counter += 1
    if len(str(data)) > 18:
        await message.answer('Максимальная длинна названия - <ins>28 символов</ins>. Введите новое название.', parse_mode=ParseMode.HTML)
    elif counter == 1:
        await message.answer('Данное название уже <ins>занятo</ins>. Введите другое название.', parse_mode=ParseMode.HTML)
    else:
        await add.add_clan_name(message.from_user.id, str(data))
        await state.clear()
        await message.answer(f'<b>{data}</b>, название клана успешно сохранено.\nТак же вы можете поменять название клана в его настройках.', reply_markup=kb.main, parse_mode=ParseMode.HTML)

        await create_code(message)

@router.message(F.photo, Clan.clan_photo)
async def clan_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await add.add_clan_photo(message.from_user.id, message.photo[-1].file_id)
    await message.answer('Ваше фото клана успешно установлено!')
    await state.clear()


@router.message(Clan.code)
async def clan_code(message: Message, state: FSMContext):
    await state.update_data(code=message.text)
    codes = await get.get_clans_all_codes()
    counter = 0
    kb_code = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Верно', callback_data='verno'),
                InlineKeyboardButton(text='Неверно', callback_data='neverno')
            ]
        ]
    )
    for code in codes:
        if code == message.text:
            counter += 1
    if counter == 1:
        owner = await get.get_clan_owner_by_code(message.text)
        name = await get.get_clan_name(owner)
        await message.answer(f'Название клана: {name}', reply_markup=kb_code)
    else:
        await message.answer('Такого клана не существует.')
        await state.clear()

@router.callback_query(F.data == 'verno')
async def verno(callback: CallbackQuery, state: FSMContext, bot: Bot):
    code = await state.get_data()
    owner = await get.get_clan_owner_by_code(code['code'])
    name = await get.get_clan_name(owner)
    nickname = await get.get_user_nickname(callback.from_user.id)
    if await get.get_clan_members(owner) < 20:
        await set.set_user_clan(callback.from_user.id, int(f'892352{owner}'))
        await callback.message.answer(f'Вы подали заявку в клан {name}')
        await bot.send_message(owner, f'Новая заявка на вступление в клан от {nickname}')
    else:
        await callback.message.answer('Клан полный.')
    await state.clear()

@router.callback_query(F.data == 'neverno')
async def neverno(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer('Введите новый код')
    await state.set_state(Clan.code)

@router.message(Clan.money)
async def add_money(message: Message, state: FSMContext):
    await state.update_data(money=int(message.text))
    money = await state.get_data()
    user_money = await get.get_money(message.from_user.id)
    if user_money >= money['money']:
        add = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Выбрать другую сумму', callback_data='again')
                ],
                [
                    InlineKeyboardButton(text='Подтверждаю', callback_data='yep'),
                    InlineKeyboardButton(text='Отмена', callback_data='nope')
                ]
            ]
        )
        await message.answer('Подтверждаете пополнение?', reply_markup=add)
    else:
        await message.answer(f'Недостаточно денег.\n Ваш баланс: {user_money}')

@router.callback_query(F.data == 'again')
async def again(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer('Введите новую сумму пополнения')
    await state.set_state(Clan.money)

@router.callback_query(F.data == 'yep')
async def yep(callback: CallbackQuery, state: FSMContext):
    money = await state.get_data()
    await minus.minus_money(callback.from_user.id, money['money'])
    await add.update_clan_money(callback.from_user.id, money['money'])
    await callback.message.answer(f'С вашего счёта было снято - {money["money"]}.')
    await state.clear()

@router.callback_query(F.data == 'nope')
async def nope(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Вы отменили пополнение.')
    await state.clear()
