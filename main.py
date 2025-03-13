import os
from aiogram import Bot, Dispatcher
from handlers import exchanger, others, profile, referral_programm, clans, steal, start, states, tops, upgrade_shop, event_fishing, event_steal
from handlers.time_mes import send_message_cron
from database.models import async_main
import datetime
import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    await async_main()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    # Выводим в консоль информацию о начале запуска
    logger.info('Starting BOT')

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message_cron, trigger='cron', hour=16,
                      minute=00, start_date=datetime.datetime.now(), kwargs={'bot': bot})

    scheduler.add_job(send_message_cron, trigger='cron', hour=00,
                      minute=00, start_date=datetime.datetime.now(), kwargs={'bot': bot})

    scheduler.start()
    dp.include_router(start.router)
    dp.include_router(exchanger.router)
    dp.include_router(profile.router)
    dp.include_router(clans.router)
    dp.include_router(referral_programm.router)
    dp.include_router(steal.router)
    dp.include_router(states.router)
    dp.include_router(tops.router)
    dp.include_router(upgrade_shop.router)
    dp.include_router(event_fishing.router)
    dp.include_router(event_steal.router)
    dp.include_router(others.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
