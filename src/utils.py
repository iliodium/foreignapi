import enum

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.models import CustomerOrm


class StatusEnum(str, enum.Enum):
    good = "good"
    error = "error"


class DishEnum(str, enum.Enum):
    added = "The dish is added"
    already_in_menu = "The dish is already on the menu"
    dish_not_exist = "Dish does not exist"
    dish_exist = "Dish exist"


async def check_exist_customer(customer_name: str = "Заведение3",
                               session: AsyncSession = Depends(get_async_session)) -> dict:
    query = (
        select(CustomerOrm)
        .where(CustomerOrm.name == customer_name)
        .limit(1)
    )
    result = await session.execute(query)
    result = result.scalars().all()

    if len(result) == 0:
        raise HTTPException(status_code=404, detail={
            "status": StatusEnum.error,
            "customer_id": None,
            "details": "Customer does not exist"
        })

    return {"status": StatusEnum.good,
            "customer_id": result[0].customer_id,
            "details": "Customer exists"}
