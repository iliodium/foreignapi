from typing import Annotated, AsyncGenerator

from sqlalchemy import create_engine, String
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column

from config import DATABASE_URL_syncpg, DATABASE_URL_asyncpg

sync_engine = create_engine(
    url=DATABASE_URL_syncpg,
    echo=True,
    pool_size=10,
    max_overflow=5
)
async_engine = create_async_engine(
    url=DATABASE_URL_asyncpg,
    echo=False,
    pool_size=10,
    max_overflow=5
)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


def get_sync_session() -> Session:
    with sync_session_factory() as session:
        return session


class Base(DeclarativeBase):
    pass


str_60 = Annotated[str, 60]
str_60_unique = Annotated[str, mapped_column(String(60), unique=True)]
intpk = Annotated[int, mapped_column(primary_key=True)]
