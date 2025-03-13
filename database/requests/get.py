from database.models import async_session
from database.models import User, Clan, Event
from sqlalchemy import select


async def get_user_nickname(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.nickname).where(User.tg_id == tg_id))
        return result


async def get_money_chance(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.money_chance).where(User.tg_id == tg_id))
        return float(result)


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


async def get_top_money():
    async with async_session() as session:
        query = await session.scalars(select(User.tg_id).where(User.money != 0).order_by(User.money.desc()).limit(100))
        result = query.fetchall()
        return result


async def get_user(tg_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        return result


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


async def get_clan_name(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.name).where(Clan.owner_tg_id == clan))
        return result


async def get_clan_owner(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.owner_tg_id).where(Clan.owner_tg_id == clan))
        return result


async def get_clan_owner_nickname(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(User.nickname).where(User.tg_id == clan))
        return result


async def get_clan_first_vice(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.first_vice_tg_id).where(Clan.owner_tg_id == clan))
        return result


async def get_clan_first_vice_nickname(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        nickname = await session.scalar(select(Clan.first_vice_tg_id).where(Clan.owner_tg_id == clan))
        result = await session.scalar(select(User.nickname).where(User.tg_id == nickname))
        return result


async def get_clan_second_vice(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.second_vice_tg_id).where(Clan.owner_tg_id == clan))
        return result


async def get_clan_second_vice_nickname(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        nickname = await session.scalar(select(Clan.second_vice_tg_id).where(Clan.owner_tg_id == clan))
        result = await session.scalar(select(User.nickname).where(User.tg_id == nickname))
        return result


async def get_clan_members(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.members).where(Clan.owner_tg_id == clan))
        return result


async def get_user_clan(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        return result


async def get_clan_photo(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.photo_id).where(Clan.owner_tg_id == clan))
        return result


async def get_clan_money(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.money).where(Clan.owner_tg_id == clan))
        return result


async def get_clan_money_chance(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.money_chance_upgrade).where(Clan.owner_tg_id == clan))
        return float(result)


async def get_clan_boost_chance(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.boost_chance_upgrade).where(Clan.owner_tg_id == clan))
        return float(result)


async def get_clan_users_money(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        result = await session.scalar(select(Clan.users_money).where(Clan.owner_tg_id == clan))
        return result


async def get_clans():
    async with async_session() as session:
        query = await session.scalars(select(Clan.name).where(Clan.members != 20, Clan.type != 1).order_by(Clan.members.desc()))
        result = query.fetchall()
        return result


async def get_members(name: str):
    async with async_session() as session:
        query = await session.scalar(select(Clan.members).where(Clan.name == name))
        return query


async def get_clan_type(tg_id: int):
    async with async_session() as session:
        query = await session.scalar(select(Clan.type).where(Clan.owner_tg_id == tg_id))
        return query


async def get_clans_codes(tg_id: int):
    async with async_session() as session:
        query = await session.scalars(select(Clan.code).where(Clan.owner_tg_id != tg_id))
        result = query.fetchall()
        return result


async def get_clans_names(tg_id: int):
    async with async_session() as session:
        query = await session.scalars(select(Clan.name).where(Clan.owner_tg_id != tg_id))
        result = query.fetchall()
        return result


async def get_clan_code(tg_id: int):
    async with async_session() as session:
        clan = await session.scalar(select(User.clan).where(User.tg_id == tg_id))
        query = await session.scalar(select(Clan.code).where(Clan.owner_tg_id == clan))
        return query

async def get_clan_users(tg_id: int):
    async with async_session() as session:
        query = await session.scalars(select(User.tg_id).where(User.clan == tg_id))
        result = query.fetchall()
        return result

async def get_clan_name_members(tg_id: int):
    async with async_session() as session:
        query = await session.scalars(select(User.nickname).where(User.clan == tg_id, User.clan != User.tg_id))
        result = query.fetchall()
        return result

async def get_clan_owner_by_code(code: str):
    async with async_session() as session:
        result = await session.scalar(select(Clan.owner_tg_id).where(Clan.code == code))
        return result

async def get_clans_all_codes():
    async with async_session() as session:
        query = await session.scalars(select(Clan.code).where(Clan.members != 20))
        result = query.fetchall()
        return result

async def get_clan_owner_by_name(name: str):
    async with async_session() as session:
        result = await session.scalar(select(Clan.owner_tg_id).where(Clan.name == name))
        return result

async def user_tg_id_by_nickname(nickname: str):
    async with async_session() as session:
        result = await session.scalar(select(User.tg_id).where(User.nickname == nickname))
        return result

async def get_users():
    async with async_session() as session:
        query = await session.scalars(select(User.tg_id))
        result = query.fetchall()
        print(result)
        return result


async def get_clan_name_to_add_members(tg_id: int):
    async with async_session() as session:
        query = await session.scalars(select(User.nickname).where(User.clan == int(f'892352{tg_id}')))
        result = query.fetchall()
        return result



async def get_bear_power(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.bear_power).where(User.tg_id == tg_id))
        return float(result)


async def get_bear_protection(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.bear_protection).where(User.tg_id == tg_id))
        return float(str(result))


async def get_fish(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.fish).where(User.tg_id == tg_id))
        return int(result)


async def get_fishing1(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(Event.fishing1).where(Event.tg_id == tg_id))
        return int(result)

async def get_fishing2(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(Event.fishing2).where(Event.tg_id == tg_id))
        return int(result)

async def get_fishing3(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(Event.fishing3).where(Event.tg_id == tg_id))
        return int(result)


async def get_fishing_chance(tg_id: int):
    async with async_session() as session:
        result = await session.scalar(select(Event.fishing_chance).where(Event.tg_id == tg_id))
        return float(str(result))


async def get_top_fish():
    async with async_session() as session:
        query = await session.scalars(select(User.tg_id).where(User.fish != 0).order_by(User.fish.desc()).limit(100))
        result = query.fetchall()
        return result