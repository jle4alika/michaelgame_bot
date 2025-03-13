from aiogram import Bot
import database.requests.get as get

async def send_message_cron(bot: Bot):
    users = await get.get_users()
    for user in users:
        await bot.send_message(chat_id=user, text="Хей 🖖, шишек на всех не хватит! Скорей беги собирать шишки!)")
