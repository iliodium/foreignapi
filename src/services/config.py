import enum

import aiohttp


class CountWorkersService(enum.IntEnum):
    BookkeepingService = 10


class BookkeepingServiceResponce(str, enum.Enum):
    pay_tax = "ПЛАТИ НАЛОГИ"


class StatusServer(str, enum.Enum):
    start = "running the gRPC server {}"
    success = "the gRPC server {} is successful running"
    error = "the gRPC server {} has crashed"


HOST = "localhost"
PORT = 50123
URL = f"{HOST}:{PORT}"

aiohttp_session = aiohttp.ClientSession()
