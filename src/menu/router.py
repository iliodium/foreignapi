from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update, delete

from src.database import get_async_session
from src.models import CustomerOrm, MenuOrm, DishOrm
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils import StatusEnum, DishEnum, check_exist_customer

router = APIRouter(
    prefix="/menu",
    tags=["Menu"],
)


async def check_exist_dish(dish_name: str = "Суп",
                           session: AsyncSession = Depends(get_async_session)) -> dict:
    query = (
        select(DishOrm)
        .where(DishOrm.name == dish_name)
        .limit(1)
    )
    result = await session.execute(query)
    result = result.scalars().all()

    if len(result) == 0:
        return {
            "status": StatusEnum.error,
            "dish_id": None,
            "details": DishEnum.dish_not_exist
        }

    return {
        "status": StatusEnum.good,
        "dish_id": result[0].dish_id,
        "details": DishEnum.dish_exist
    }


async def add_dish(dish_name: str,
                   session: AsyncSession = Depends(get_async_session)) -> dict:
    dish = DishOrm(name=dish_name)
    session.add(dish)
    await session.flush()
    dish_id = dish.dish_id

    return {
        "status": StatusEnum.good,
        "dish_id": dish_id,
        "details": DishEnum.added,
    }


@router.get("/v1")
async def get_menu(customer_name: str = "Заведение3",
                   session: AsyncSession = Depends(get_async_session),
                   customer_id: dict = Depends(check_exist_customer)
                   ) -> dict:
    query = (
        select(CustomerOrm)
        .where(CustomerOrm.name == customer_name)
        .limit(1)
    )

    result = await session.execute(query)
    result = result.scalars().all()

    menu = {i.dish.name: i.cost / 100 for i in result[0].menu}

    return menu


@router.put("/v1/cost")
async def update_cost(customer_name: str = "Заведение3",
                      dish_name: str = "Щи",
                      price: float | int = 322.12,
                      session: AsyncSession = Depends(get_async_session),
                      customer_id: dict = Depends(check_exist_customer),
                      dish_id: dict = Depends(check_exist_dish)) -> dict:
    customer_id = customer_id["customer_id"]
    dish_id = dish_id["dish_id"]

    price = int(price * 100)

    stmt = (
        update(MenuOrm)
        .values(cost=price)
        .filter_by(customer_id=customer_id, dish_id=dish_id)
    )

    await session.execute(stmt)
    await session.commit()

    return {"status": 1}


@router.put("/v1/name")
async def rename_dish(customer_name: str = "Заведение3",
                      old_dish_name: str = "крутые перцы12345",
                      new_dish_name: str = "супер крутые перцы",
                      session: AsyncSession = Depends(get_async_session),
                      customer_id: dict = Depends(check_exist_customer)) -> dict:
    customer_id = customer_id["customer_id"]

    query = (
        select(DishOrm)
        .where(DishOrm.name == new_dish_name)
        .limit(1)
    )
    result = await session.execute(query)
    result = result.scalars().all()

    query = (
        select(DishOrm)
        .where(DishOrm.name == old_dish_name)
        .limit(1)
    )
    old_dish_id = await session.execute(query)
    old_dish_id = old_dish_id.scalars().all()
    old_dish_id = old_dish_id[0].dish_id

    if len(result) == 0:
        responce = await add_dish(new_dish_name, session)
        new_dish_id = responce["dish_id"]
        stmt = (
            update(MenuOrm)
            .values(dish_id=new_dish_id)
            .filter_by(customer_id=customer_id, dish_id=old_dish_id)
        )

    else:
        new_dish_id = result[0].dish_id
        stmt = (
            update(MenuOrm)
            .values(dish_id=new_dish_id)
            .filter_by(customer_id=customer_id, dish_id=old_dish_id)
        )
    await session.execute(stmt)

    query = (
        select(MenuOrm)
        .where(MenuOrm.dish_id == old_dish_id)
    )
    all_dish_id = await session.execute(query)
    all_dish_id = all_dish_id.scalars().all()
    if len(all_dish_id) == 0:
        stmt = (
            delete(DishOrm)
            .filter_by(dish_id=old_dish_id)
        )
        await session.execute(stmt)

    await session.commit()

    return {"status": 1}


@router.post("/v1")
async def add_dish_to_menu(customer_name: str = "Заведение3",
                           dish_name: str = "Щи",
                           price: float | int = 100.12,
                           session: AsyncSession = Depends(get_async_session),
                           customer_id: dict = Depends(check_exist_customer)) -> dict:
    customer_id = customer_id["customer_id"]
    responce = await check_exist_dish(dish_name, session)
    if responce["status"] == "good":
        dish_id = responce["dish_id"]
    else:
        responce = await add_dish(dish_name, session)
        dish_id = responce["dish_id"]

    query = (
        select(MenuOrm)
        .where(MenuOrm.dish_id == dish_id and MenuOrm.customer_id == customer_id)
        .limit(1)
    )
    result = await session.execute(query)
    result = result.scalars().all()

    if len(result) == 0:
        menu_dish = MenuOrm(customer_id=customer_id, dish_id=dish_id, cost=int(price * 100))
        session.add(menu_dish)
        await session.commit()
    else:
        return {
            "status": StatusEnum.error,
            "details": DishEnum.already_in_menu,
        }

    return {
        "status": StatusEnum.good,
        "details": DishEnum.added,
    }
