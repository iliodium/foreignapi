import random
from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"]
)


@router.get("")
async def get_dishes(dishes: List[str] = Query(None)) -> dict:
    result = {
        "dishes": dict(),
    }
    for dish in dishes:
        result["dishes"][dish] = random.randint(100, 1000)

    return result

@router.post("")
async def add_specific_operations(session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    a = await session.execute(stmt)
    #await session.commit()
    print(a)
    return {"status": "success"}