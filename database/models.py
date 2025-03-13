from sqlalchemy import BigInteger, String, Float, DateTime, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import random

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    nickname: Mapped[str] = mapped_column(String(18), default=f'{tg_id}', unique=True)
    money: Mapped[int] = mapped_column(BigInteger, default=0)
    fish: Mapped[int] = mapped_column(BigInteger, default=0)
    bear_power: Mapped[float] = mapped_column(Float(100, asdecimal=True), default=0.0)
    bear_protection: Mapped[float] = mapped_column(Float(100, asdecimal=True), default=0.0)
    alltime_money: Mapped[int] = mapped_column(BigInteger, default=0)
    money_chance: Mapped[float] = mapped_column(Float(70, asdecimal=True), default=15.0)
    boost_chance: Mapped[float] = mapped_column(Float(70, asdecimal=True), default=15.0)
    photo_id: Mapped[str] = mapped_column(String(10000), default='')
    referrer_id: Mapped[int] = mapped_column(BigInteger, default=0)
    datetime: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    upgrade1: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    upgrade2: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    upgrade3: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    referrer_count: Mapped[int] = mapped_column(Integer, default=0)
    clan: Mapped[int] = mapped_column(BigInteger, default=0)

class Clan(Base):
    __tablename__ = 'clans'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_tg_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(28), default=f'{owner_tg_id}', unique=True)
    first_vice_tg_id: Mapped[int] = mapped_column(BigInteger, default=0)
    second_vice_tg_id: Mapped[int] = mapped_column(BigInteger, default=0)
    type: Mapped[int] = mapped_column(Integer, default=0)
    code: Mapped[str] = mapped_column(String(30), default=f'{owner_tg_id}', unique=True)
    members: Mapped[int] = mapped_column(Integer, default=1)
    money: Mapped[int] = mapped_column(BigInteger, default=0)
    users_money: Mapped[int] = mapped_column(BigInteger, default=0)
    users_fish: Mapped[int] = mapped_column(BigInteger, default=0)
    money_chance_upgrade: Mapped[float] = mapped_column(Float(70, asdecimal=True), default=0.0)
    boost_chance_upgrade: Mapped[float] = mapped_column(Float(70, asdecimal=True), default=0.0)
    photo_id: Mapped[str] = mapped_column(String(10000), default='')


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    fishing_chance: Mapped[int] = mapped_column(Integer, default=25)
    fishing1: Mapped[int] = mapped_column(Integer, default=0)
    fishing2: Mapped[int] = mapped_column(Integer, default=0)
    fishing3: Mapped[int] = mapped_column(Integer, default=0)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def restart_bd():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def drop_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
