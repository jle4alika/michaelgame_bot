from aiogram import Router, Bot, F
from aiogram.types import Message
import database.requests.get as get
import keyboards.reply as kb
import asyncio


from handlers.chat_types import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(['private']))


@router.message(F.text == 'kB')
async def kb_give(message: Message, bot: Bot):
    users = await get.get_users()
    for user in users:
        await bot.send_message(chat_id=user, text='Вы получили обновлённую версию клавиатуры!', reply_markup=kb.main)
        await asyncio.sleep(3)


@router.message(F.text.lower() == 'клавиатура')
async def kb_give(message: Message):
    await message.answer('Вы получили обновлённую версию клавиатуры!', reply_markup=kb.main)