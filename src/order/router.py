import pickle
import json

from sqlalchemy import select
from fastapi import APIRouter, Depends
from google.protobuf.json_format import MessageToJson

from src.database import get_async_session
from src.models import CustomerOrm
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.bookkeeping_service_grpc.client import BookkeepingServiceClient as BookkeepingGRPC
from src.services.config import HOST, PORT, aiohttp_session
from src.services.utils import calculate_tax
from src.utils import check_exist_customer

router = APIRouter(
    prefix="/order",
    tags=["Order"],
)


@router.get("/v1")
async def get_order(customer_name: str = "Заведение3",
                    order: str = "Цезарь с курицей&гречка&Роллы с тунцом&Суп с фрикадельками",
                    session: AsyncSession = Depends(get_async_session),
                    customer_id: dict = Depends(check_exist_customer)) -> dict:
    order = order.split("&")
    query = (
        select(CustomerOrm)
        .where(CustomerOrm.name == customer_name)
        .limit(1)
    )

    result = await session.execute(query)
    result = result.scalars().all()

    check = {i.dish.name: i.cost / 100 for i in result[0].menu if i.dish.name in order}

    async with aiohttp_session.get(f'http://{HOST}:{PORT + 1}/BookkeepingService/v1', data=pickle.dumps(check)) as resp:
        result_rest = await resp.text()

    bookkeeping = BookkeepingGRPC()
    response_grpc = bookkeeping.send_check(check)
    result_grpc = json.loads(MessageToJson(response_grpc))

    summa = sum(check.values())

    for i in set(order) ^ set(check.keys()):
        check[i] = None

    check["summa"] = summa

    check["summa_after_tax_rest"] = float(result_rest) / 100
    check["summa_after_tax_grpc"] = result_grpc['tax'] / 100

    return check
