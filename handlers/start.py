from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from handlers.states import Reg
import database.requests.get as get
import database.requests.add as add
import database.requests.others as set
import keyboards.inline as kb


from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))


@router.message(CommandStart())
async def start(message: Message, state: FSMContext, bot: Bot):
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в мини-игру с Михаилом!', reply_markup=kb.start)
    user_bool = await get.get_user_bool(message.from_user.id)
    if not user_bool:
        start_command = message.text
        referrer_id = str(start_command[7:])
        if str(referrer_id) != '':
            if str(referrer_id) != str(message.from_user.id):
                await set.set_user(message.from_user.id, int(referrer_id))
                await add.add_referrer_count(referrer_id, 1)
                await bot.send_message(chat_id=referrer_id, text='По вашей реферальной ссылке зашёл новый пользователь.\n'
                                                                 f'Приглашено людей: {await get.get_referrer_count(referrer_id)}')
            else:
                await message.answer('<ins>Нельзя</ins> регистрироваться по собственной ссылке!', parse_mode=ParseMode.HTML)
                await set.set_user(message.from_user.id)
        else:
            await set.set_user(message.from_user.id)

        await add.add_nickname(message.from_user.id, str(message.from_user.username))
        await message.answer('Введите ваш никнейм:')
        await state.set_state(Reg.nickname)

