from typing import Annotated

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
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
    echo=True,
    pool_size=10,
    max_overflow=5
)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass


str_60 = Annotated[str, 60]
intpk = Annotated[int, mapped_column(primary_key=True)]
