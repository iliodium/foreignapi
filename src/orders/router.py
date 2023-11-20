import random
from typing import List

from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/dishes",
    tags=["Dishes"]
)


@router.get("")
async def get_dishes(dishes: List[str] = Query(None))-> dict:
    result = {
        "dishes": dict(),
    }
    for dish in dishes:
        result["dishes"][dish] = random.randint(100, 1000)

    return result
