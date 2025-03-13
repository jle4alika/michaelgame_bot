from database.models import async_session
from database.models import User
from sqlalchemy import select, update, text

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


async def get_user_nickname(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.nickname).where(User.tg_id == tg_id))
        return result


async def get_money_chance(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.money_chance).where(User.tg_id == tg_id))
        return float(str(result))


async def get_boost_chance(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.boost_chance).where(User.tg_id == tg_id))
        return float(str(result))


async def get_alltime_money(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.alltime_money).where(User.tg_id == tg_id))
        return int(str(result))


async def get_money(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.money).where(User.tg_id == tg_id))
        return int(str(result))


async def get_photo_id(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.photo_id).where(User.tg_id == tg_id))
        return str(result)


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


async def minus_money_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(money_chance=User.money_chance - chance))
        await session.commit()


async def add_boost_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(boost_chance=User.boost_chance + chance))
        await session.commit()


async def minus_boost_chance(tg_id: int, chance: float):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(boost_chance=User.boost_chance - chance))
        await session.commit()


async def add_money(tg_id: int, money: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(money=User.money+money))
        await session.commit()


async def minus_money(tg_id: int, money: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(money=User.money-money))
        await session.commit()


async def get_top_money():
    async with async_session() as session:
        query = await session.scalars(select(User.tg_id).where(User.money != 0).order_by(User.money.desc()).limit(100))
        result = query.fetchall()
        return result


async def get_user(tg_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        return result


async def add_nickname(tg_id: int, nickname: str):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(nickname=nickname))
        await session.commit()


async def get_referrals(tg_id: int):
    async with async_session() as session:
        query = await session.execute(select(User.tg_id).where(User.referrer_id == tg_id))
        result = query.fetchall()
        return len(result)


async def get_upgrade1(tg_id: int):
    async with async_session() as session:
        query = await session.execute(select(User.upgrade1).where(User.tg_id == tg_id))
        result = query.fetchall()
        for item in result:
            for x in item:
                return x


async def get_upgrade2(tg_id: int):
    async with async_session() as session:
        query = await session.execute(select(User.upgrade2).where(User.tg_id == tg_id))
        result = query.fetchall()
        for item in result:
            for x in item:
                return x


async def get_upgrade3(tg_id: int):
    async with async_session() as session:
        query = await session.execute(select(User.upgrade3).where(User.tg_id == tg_id))
        result = query.fetchall()
        for item in result:
            for x in item:
                return x


async def get_user_bool(tg_id: int):
    async with async_session() as session:
        query = await session.execute(select(User).where(User.tg_id == tg_id))
        result = query.fetchall()
        return bool(len(result))


async def add_alltime_money(tg_id: int, money: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(alltime_money=User.alltime_money+money))
        await session.commit()


async def get_top_alltime_money():
    async with async_session() as session:
        query = await session.scalars(select(User.tg_id).where(User.alltime_money != 0).order_by(User.alltime_money.desc()).limit(100))
        result = query.fetchall()
        return result


async def get_all_nicknames(tg_id: int):
    async with async_session() as session:
        query = await session.scalars(select(User.nickname).where(User.tg_id != tg_id))
        result = query.fetchall()
        return result


async def get_top_referrals():
    async with async_session() as session:
        query = await session.scalars(select(User.tg_id).where(User.referrer_count != 0).order_by(User.referrer_count.desc()).limit(100))
        result = query.fetchall()
        return result


async def get_referrer_count(tg_id: int):
    async with async_session() as session:
        query = await session.scalar(select(User.referrer_count).where(User.tg_id == tg_id, User.referrer_count != 0))
        return query


async def add_referrer_count(tg_id: int, referrer_count: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(referrer_count=User.referrer_count + referrer_count))
        await session.commit()


async def add_column():
    async with async_session() as session:
        await session.execute(text('alter table users add column referrer_count integer default 0'))
        await session.commit()


async def set_nickname(tg_id: int, nickname: str):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(nickname=nickname))
        await session.commit()