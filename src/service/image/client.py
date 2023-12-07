import time
import pickle
from concurrent.futures import ThreadPoolExecutor
import asyncio

import aiohttp as aiohttp
import grpc
import grpc_service.structure_pb2 as pb2
import grpc_service.structure_pb2_grpc as pb2_grpc

from config import URL, count_workers


class SendCheck(object):
    def __init__(self):
        self.channel = grpc.insecure_channel(URL)
        self.stub = pb2_grpc.CheckServiceStub(self.channel)

    def send_check(self, data: dict):
        data = pickle.dumps(data)
        request = pb2.Check(check=data)
        response = self.stub.SendCheck(request)
        return response


async def rest_client(data):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/t', data={"data": 321}) as response:
            print(response.content)
            return response


def grpc_client(data):
    grpc_stub = SendCheck()
    res = grpc_stub.send_check(data)
    print(data["name"], res)


def run_grpc_client(data):
    with ThreadPoolExecutor(max_workers=count_workers) as executor:
        executor.map(lambda i: grpc_client(i), data)


def run_rest_client(data):
    with ThreadPoolExecutor(max_workers=1) as executor:
        list(executor.map(lambda i: asyncio.run(rest_client(i)), data))


if __name__ == "__main__":
    data = []
    for i in range(3):
        temp = {i: str(i ** 2) for i in range(4)}
        temp["name"] = f"stub{i}"
        data.append(temp)

    # run_grpc_client(data)
    run_rest_client(data)
