import random
from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import async_session_factory
from src.models import CustomerOrm

router = APIRouter(
    prefix="/registration",
    tags=["Registration"]
)


@router.post("")
async def registration_restaurant(restaurant: str, auth: str) -> str:
    new_restaurant = CustomerOrm(name=restaurant, auth=auth)
    async with async_session_factory() as session:
        session.add(new_restaurant)
        await session.commit()

    restaurant += '_stmt'
    auth += '_stmt'

    async with async_session_factory() as session:
        stmt = (
            insert(CustomerOrm)
            .values(name=restaurant, auth=auth)
        )

        await session.execute(stmt)
        await session.commit()

    return "OK"

@router.post("/123")
async def registration_restaurant1(id:int, cost: float) -> str:
    new_restaurant = test_pOrm(id=id, cost=cost)
    async with async_session_factory() as session:
        session.add(new_restaurant)
        await session.commit()

    # restaurant += '_stmt'
    # auth += '_stmt'
    #
    # async with async_session_factory() as session:
    #     stmt = (
    #         insert(CustomerOrm)
    #         .values(name=restaurant, auth=auth)
    #     )
    #
    #     await session.execute(stmt)
    #     await session.commit()

    return "OK"