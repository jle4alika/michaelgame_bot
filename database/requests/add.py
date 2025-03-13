from database.models import async_session
from database.models import User, Clan, Event
from sqlalchemy import select, update, text
import datetime


async def add_bear_power(tg_id: int, power: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(bear_power=User.bear_power + power))
        await session.commit()


async def add_bear_protection(tg_id: int, protection: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(bear_protection=User.bear_protection + protection))
        await session.commit()


async def add_clan_photo(tg_id: int, photo: str):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(photo_id=photo))
        await session.commit()


async def add_clan_member(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        await session.execute(update(Clan).where(Clan.owner_tg_id == clan).values(members=Clan.members+1))
        await session.commit()

async def add_clan_type(tg_id: int, typ: int):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(type=typ))
        await session.commit()

async def add_clan_code(tg_id: int, code: str):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(code=code))
        await session.commit()

async def add_clan_name(tg_id: int, name: str):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(name=name))
        await session.commit()


async def update_clan_money_chance(tg_id: int, money_chance: float):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(money_chance_upgrade=Clan.money_chance_upgrade+money_chance))
        await session.commit()


async def update_clan_boost_chance(tg_id: int, boost_chance: float):
    async with async_session() as session:
        await session.execute(update(Clan).where(Clan.owner_tg_id == tg_id).values(boost_chance_upgrade=Clan.boost_chance_upgrade+boost_chance))
        await session.commit()


async def update_clan_users_money(tg_id: int, users_money: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        await session.execute(update(Clan).where(Clan.owner_tg_id == clan).values(users_money=Clan.users_money+users_money))
        await session.commit()


async def update_clan_users_fish(tg_id: int, users_fish: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        await session.execute(update(Clan).where(Clan.owner_tg_id == clan).values(users_fish=Clan.users_fish+users_fish))
        await session.commit()


async def update_clan_money(tg_id: int, money: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        await session.execute(update(Clan).where(Clan.owner_tg_id == clan).values(money=Clan.money+money))
        await session.commit()




async def add_photo_id(tg_id: int, photo: str):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(photo_id=photo))
        await session.commit()


async def update_upgrade1(tg_id: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(upgrade1=datetime.datetime.now()))
        await session.commit()


async def update_upgrade2(tg_id: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(upgrade2=datetime.datetime.now()))
        await session.commit()


async def update_upgrade3(tg_id: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(upgrade3=datetime.datetime.now()))
        await session.commit()


async def add_upgrade1(tg_id: int, hours: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(upgrade1=datetime.datetime.now() + datetime.timedelta(hours=hours)))
        await session.commit()


async def add_upgrade2(tg_id: int, hours: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(upgrade2=datetime.datetime.now() + datetime.timedelta(hours=hours)))
        await session.commit()


async def add_upgrade3(tg_id: int, hours: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(upgrade3=datetime.datetime.now() + datetime.timedelta(hours=hours)))
        await session.commit()


async def add_money_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(money_chance=User.money_chance + chance))
        await session.commit()


async def add_boost_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(boost_chance=User.boost_chance + chance))
        await session.commit()

async def add_money(tg_id: int, money: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(money=User.money+money))
        await session.commit()


async def add_fish(tg_id: int, fish: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(fish=User.fish+fish))
        await session.commit()

async def add_nickname(tg_id: int, nickname: str):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(nickname=nickname))
        await session.commit()


async def add_alltime_money(tg_id: int, money: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(alltime_money=User.alltime_money+money))
        await session.commit()

async def add_referrer_count(tg_id: int, referrer_count: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(referrer_count=User.referrer_count + referrer_count))
        await session.commit()


async def set_nickname(tg_id: int, nickname: str):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(nickname=nickname))
        await session.commit()


async def update_fishing_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(Event).where(Event.tg_id == tg_id).values(fishing_chance=chance))
        await session.commit()


async def update_fishing1(tg_id: int):
    async with async_session() as session:
        await session.execute(update(Event).where(Event.tg_id == tg_id).values(fishing1=1))
        await session.commit()

async def update_fishing2(tg_id: int):
    async with async_session() as session:
        await session.execute(update(Event).where(Event.tg_id == tg_id).values(fishing2=1))
        await session.commit()

async def update_fishing3(tg_id: int):
    async with async_session() as session:
        await session.execute(update(Event).where(Event.tg_id == tg_id).values(fishing3=1))
        await session.commit()


async def add_column():
    async with async_session() as session:
        await session.execute(text('alter table users add column referrer_count integer default 0'))
        await session.commit()

