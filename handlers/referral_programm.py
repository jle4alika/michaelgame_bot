from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
import database.requests.get as get
from aiogram.enums import ParseMode


from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))


@router.message(F.text == 'Реферальная программа ✌️')
async def get_ref(message: Message):
    link = f'https://t.me/michaelgame_bot?start={message.from_user.id}'
    if await get.get_referrer_count(message.from_user.id) != None:
        await message.answer(f"Вы пригласили - <b>{await get.get_referrer_count(message.from_user.id)}</b> людей\nВаша реф. ссылка:\n{link}",
                             parse_mode=ParseMode.HTML)
    else:
        await message.answer(f"Вы пригласили - <b>0</b> людей\nВаша реф. ссылка:\n{link}", parse_mode=ParseMode.HTML)



@router.callback_query(F.data == 'Реферальная программа ✌️')
async def get_ref(callback: CallbackQuery):
    link = f'https://t.me/michaelgame_bot?start={callback.from_user.id}'
    if await get.get_referrer_count(callback.from_user.id) != None:
        await callback.message.answer(f"Вы пригласили - <b>{await get.get_referrer_count(callback.from_user.id)}</b> людей\nВаша реф. ссылка:\n{link}",
                             parse_mode=ParseMode.HTML)
    else:
        await callback.message.answer(f"Вы пригласили - <b>0</b> людей\nВаша реф. ссылка:\n{link}", parse_mode=ParseMode.HTML)