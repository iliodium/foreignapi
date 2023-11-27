import random
from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import async_session_factory
from src.models import CustomerOrm

router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"]
)


@router.get("")
async def get_dishes(customer: str = "Заведение3") -> dict:
    async with async_session_factory() as session:
        query = (
                select(CustomerOrm.customer_id, CustomerOrm.auth)
                .where(CustomerOrm.name == customer)
                .limit(1)
        )

        result = await session.execute(query)
        customer_id, auth = result.one()
        print(customer_id, auth)



    # result = {
    #     "dishes": dict(),
    # }
    # for dish in dishes:
    #     result["dishes"][dish] = random.randint(100, 1000)

    return {}

# @router.post("")
# async def add_specific_operations(session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(operation).values(**new_operation.dict())
#     a = await session.execute(stmt)
#     #await session.commit()
#     print(a)
#     return {"status": "success"}