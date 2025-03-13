from database.models import async_session
from database.models import User, Clan
from sqlalchemy import select, update, text

import datetime


async def minus_money_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(money_chance=User.money_chance - chance))
        await session.commit()


async def minus_boost_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(boost_chance=User.boost_chance - chance))
        await session.commit()


async def minus_money(tg_id: int, money: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(money=User.money-money))
        await session.commit()


async def minus_fish(tg_id: int, fish: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(fish=User.fish-fish))
        await session.commit()


async def minus_clan_money(tg_id: int, money: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        await session.execute(update(Clan).where(Clan.owner_tg_id == clan).values(money=Clan.money-money))
        await session.commit()


async def minus_clan_member(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        await session.execute(update(Clan).where(Clan.owner_tg_id == clan).values(members=Clan.members - 1))
        await session.commit()


async def minus_clan_money_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(money_chance=User.money_chance - chance))
        await session.commit()


async def minus_clan_boost_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(boost_chance=User.boost_chance - chance))
        await session.commit()