from database.models import async_session
from database.models import User, Clan, Event
from sqlalchemy import select, update, text, delete

import datetime


async def set_user(tg_id: int, referrer_id=None) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            if referrer_id != None:
                session.add(User(tg_id=tg_id, referrer_id=referrer_id))
                await session.commit()
            else:
                session.add(User(tg_id=tg_id))
                await session.commit()


async def set_clan(tg_id: int) -> None:
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))

        if not clan:
            session.add(Clan(owner_tg_id=tg_id))
            await session.execute(update(User).where(User.tg_id == tg_id).values(clan=tg_id))
            await session.commit()

async def delete_clan(tg_id: int):
    async with async_session() as session:
        await session.execute(delete(Clan).where(Clan.owner_tg_id == tg_id))
        await session.commit()

async def set_user_clan(tg_id: int, clan: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(clan=clan))
        await session.commit()

async def set_user_event(tg_id: int) -> None:
    async with async_session() as session:
        event = await session.scalar(select(Event).where(Event.tg_id == tg_id))

        if not event:
            session.add(Event(tg_id=tg_id))
            await session.commit()
